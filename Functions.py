from PyPDF2 import PdfReader
from docx import Document
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM




# ------------------------------------------------------------Extracting PDF & Docx File-------------------------------------------------------------
def text_extractor(file):
  if file.type=='application/vnd.openxmlformats-officedocument.wordprocessingml.document':
    extracted_docx=[]
    document = Document(file)
    paragraph=document.paragraphs
    for p in document.paragraphs:
      extracted_docx.append(p.text)
    wholeText = ' ' 
    paragraph = wholeText.join(extracted_docx)
    return paragraph
  elif file.type=='application/pdf':
    Extracted_page_list=[]
    text,textN='',''
    reader=PdfReader(file)
    for i in range(len(reader.pages)):
      pageObj = reader.pages[i]
      text=pageObj.extract_text()
      textN=text.replace('\n',' ')
      Extracted_page_list.append(textN)

    wholeText = ' ' 
    result = wholeText.join(Extracted_page_list)
    return result
  else:
    return None
  
# ----------------------------------------------------------------- Pegasus Model ------------------------------------------------------------
def sum_pegasus(text):
  
  tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
  model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-xsum")
  text=text
  tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
  summary = model.generate(**tokens)
  return tokenizer.decode(summary[0])