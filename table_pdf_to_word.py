
from docx import Document
import pdfplumber
import pandas as pd

table_settings = {"vertical_strategy": 'text', 'horizontal_strategy': 'text'}
pdf = pdfplumber.open('0_deep_survey.pdf')
table = pdf.pages[17].extract_table(table_settings)
df_main = pd.DataFrame(table[1::], columns= table[0])

doc = Document()
# add a table to the end and create a reference variable
# extra row is so we can add the header row
t = doc.add_table(df_main.shape[0] + 1, df_main.shape[1])
# add the header rows.
for j in range(df_main.shape[-1]):
    t.cell(0, j).text = df_main.columns[j]
# add the rest of the data frame
for i in range(df_main.shape[0]):
    for j in range(df_main.shape[-1]):
        t.cell(i + 1, j).text = str(df_main.values[i, j])
# save the doc
doc.save('wordfile.docx')