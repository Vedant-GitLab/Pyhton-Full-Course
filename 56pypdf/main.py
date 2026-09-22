from pypdf import PdfReader

reader = PdfReader(r"C:\Users\tiwar\OneDrive\Desktop\100 days of python\56pypdf\Python_Complete_Notes.pdf")

print("Pages:", len(reader.pages))

text = reader.pages[0].extract_text()
print(text)