from django.shortcuts import render,redirect
from apps.proi import client
from django.http import HttpResponse
from .image import *
from .utlis import *
def func1(request):
    if request.method == "GET":
        # Handle GET request, e.g., render a form or return some data
        return render(request, "he.html")
    if request.method == "POST":
        data = request.POST.get("text", "")
        print(data)
        data=data.split(",")
        print(data)
        doc=list(data)
        res=client.analyze_sentiment(documents=doc)
        print(res)
        l=[]
        for j in res:
            print(j.sentiment)
            l.append(j.sentiment)
        ele=0
        dec=[]
        for i in doc:
            print(i)
            temp={"feed":i,"pos":l[ele]}
            dec.append(temp)
            ele+=1
        print(dec)
        return render(request,"he.html",{"data":dec})
def func2(request):
    data= ""
    if request.method == "POST":
        data = request.POST.get("text", "")  # Defaults to an empty string if 'text' is not found
    return render(request, "ai.html", {"data1": data})
def func3(request):
    extracted_text = ""
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data["image"]
            print(image_file)
    else:
        form = ImageUploadForm()
    
    return render(request, "text.html", {
        "form": form,
        "extracted_text": extracted_text,
    })
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# Define your Azure Form Recognizer endpoint and API key
endpoint = ""
api_key = ""
# Define your Azure Form Recognizer endpoint and API key
def upload_image(request):
    if request.method == "GET":
        # Render the form or initial page
        return render(request, "fin.html", {})

    if request.method == 'POST':
        # Get the uploaded image
        image = request.FILES['image']
        file_path = default_storage.save('images/' + image.name, image)  # Save the image file

        # Create a client for Azure Form Recognizer
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(api_key)
        )

        # Path to access the saved image
        image_path = default_storage.path(file_path)

        # Read the saved image in binary mode
        with open(image_path, "rb") as image_file:
            # Use the OCR API to analyze the image
            poller = document_analysis_client.begin_analyze_document("prebuilt-read", image_file)
            result = poller.result()

        # Extract and print the text content from the image
        extracted_text = ""
        for page in result.pages:
            for line in page.lines:
                extracted_text += line.content + " "  # Space for readability

        # Pass extracted text to the template
        context = {"data": extracted_text}
        return render(request, "fin.html", context=context)

   





    

