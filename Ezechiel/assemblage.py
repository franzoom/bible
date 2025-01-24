import fitz  # PyMuPDF

# Ouvrir les documents PDF
doc_a = fitz.open("Ez 33-37 TOB.pdf")
doc_b = fitz.open("Ez 33-37 Heb.pdf")

# Créer un nouveau PDF pour le document final
final_doc = fitz.open()

# Ajouter les 3 premières pages du document A au document final
for page_num in range(4):
    final_doc.insert_pdf(doc_a, from_page=page_num, to_page=page_num)

# Alterner les pages des documents A et B à partir de la page 4
page_num_a = 4
page_num_b = 0

while page_num_a < len(doc_a) or page_num_b < len(doc_b):
    if page_num_a < len(doc_a):
        final_doc.insert_pdf(doc_a, from_page=page_num_a, to_page=page_num_a)
        page_num_a += 1
    if page_num_b < len(doc_b):
        final_doc.insert_pdf(doc_b, from_page=page_num_b, to_page=page_num_b)
        page_num_b += 1

# Enregistrer le PDF final dans un fichier
final_doc.save("final_document.pdf")

print("Le PDF final a été créé et enregistré sous le nom 'final_document.pdf'.")