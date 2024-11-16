from azure.ai.textanalytics import TextAnalyticsClient 
from azure.core.credentials import AzureKeyCredential
endpoint="https://botservicehhj.cognitiveservices.azure.com/"
key="4b26c31adfaa4080b09d9abcb9c46210"
cred=AzureKeyCredential(key)
client=TextAnalyticsClient(endpoint=endpoint,credential=cred)