from django.core.files.storage import FileSystemStorage
def index(request):
    return render(request, 'translator/index.html')

from django.shortcuts import render


'''def home_page(request):
    # POST - обязательный метод
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        #fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        return render(request, 'home_page.html', {
            'file_url': file_url
        })
    return render(request, '/home_page.html')'''
import requests
import base64
def encode_file(file_path):
  with open(file_path, "rb") as fid:
      file_content = fid.read()
  return base64.b64encode(file_content).decode("utf-8")
def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'translator/upload.html', {'file_url': file_url})
    return render(request, 'translator/upload.html')

def transfer(mytext,lang):
   IAM_TOKEN = ''
   folder_id = ''
   target_language = lang
   texts = mytext

   body = {
    "targetLanguageCode": target_language,
    "texts": texts,
    "folderId": folder_id,
    }

    headers = {
     "Content-Type": "application/json",
     "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    r = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
    json = body,
    headers = headers
    )
    if r['code'] == 200:
        return r['text'][0]
    else:
        return 'error'
def translate_app(request):
 try:
    if request.method == "POST":
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)
        tr = transfer(txt,lang)

        return render(request, 'translator/index.html', {"result":tr})

    return render(request, 'translator/index.html')
 except Exception as e:
     return
