from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.template.context_processors import media
import requests
import os
import shutil


#create views here
@csrf_exempt
def insertdata(request):
    #request parameter and location of file to be returned
    #the render looks in templates directory for the below mentioned file
    #but other apps will also have a templates directory
    #django will collect files from all the application templates and place it at a single folder
    #so if 2 templates have the same file name, it will be conflicting
    #so again create a subdirectory ('webapp') to place files inside templates
    teamid = request.POST.get('team_id')
    cheque_number= request.POST.get('cheque_number')
    amount_words= request.POST.get('amount_words')
    amount_digits= request.POST.get('amount_digits')
    date= request.POST.get('date')
    MICR_code= request.POST.get('MICR_code')
    act_type= request.POST.get('act_type')
    san_no= request.POST.get('san_no')
    ben_name= request.POST.get('ben_name')
    acc_no= request.POST.get('acc_no')
    amt_match= request.POST.get('amt_match')
    cheque_stale= request.POST.get('cheque_stale')
    encoding= request.POST.get('encoding')
    size = request.POST.get('size')

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(os.getcwd() +uploaded_file_url)
        f = open(os.getcwd() +uploaded_file_url, "rb")
        binary = f.read()
        requests.post(
            url="http://apiplatformcloudse-gseapicssbisecond-uqlpluu8.srv.ravcloud.com:8001/InsertChqDetails",
            headers={
                "CHQ_NUM": cheque_number,
                "TEAM_ID": teamid,
                "MIME_TYPE": "image/jpeg",
                "api-key": "238fceef-17e0-4835-abdf-f162448390be",
                "AMOUNT_WORDS":amount_words,
                "AMOUNT_DIGIT":amount_digits,
                "CHQ_DATE":date,
                "MICR_CODE":MICR_code,
                "ACT_TYPE":act_type,
                "SAN_NO":san_no,
                "BEN_NAME":ben_name,
                "PAYEE_AC_NO":acc_no,
                "AMT_MATCH":amt_match,
                "CHQ_STALE":cheque_stale,
                "ENCODING":encoding,
                "IMG_SIZE":size,
            },
            data=binary,
        )
    return render(request, 'webapp/insertdata.html')

@csrf_exempt
def receivedata(request):
    #the content dictionary will be available to contact html file (basic.html)
    teamid1 = request.POST.get('team_id1')
    cheque_number1 = request.POST.get('cheque_number1')
    if request.method == 'POST':
        headers = {
            'Content-Type': 'application/json',
            'api-key': '1a2c684a-6bb6-49d8-9846-680b40575abb'
        }
        url = 'http://apiplatformcloudse-gseapicssbisecond-uqlpluu8.srv.ravcloud.com:8001/ChequeInfo/'
        url = url+teamid1+'/'+cheque_number1+'/CHEQUE_IMAGE'

        ret = requests.get(url, headers=headers, stream=True)
        # response_body = urlopen(request).read()
        # print(ret.content)
        with open(os.getcwd() +'/media/'+'img.jpeg', 'wb') as out_file:
            shutil.copyfileobj(ret.raw, out_file)
        del ret
    return render(request, 'webapp/receivedata.html',{'content':''})
