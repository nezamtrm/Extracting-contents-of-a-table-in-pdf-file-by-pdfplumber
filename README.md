# OCR/table_pdf_to_word.py

The code imports the necessary libraries for working with Microsoft Word (.docx) and PDF files, namely Document from docx, pdfplumber, and pandas as pd.

Then, the code sets up some settings for extracting a table from a PDF file. It specifies that the table should be extracted using 'text' strategies for both vertical and horizontal orientation. It then opens a PDF file called "0_deep_survey.pdf" using pdfplumber and extracts a table from the 18th page of the PDF file using the previously defined table_settings. The extracted table is stored in a variable called table.

Next, the code creates a pandas dataframe (df_main) from the table data. It takes all rows from table except the first row (which is the header row) and sets them as data rows in the dataframe. The first row of table is set as the header row for the dataframe.

After that, the code creates a new Word document using Document(). It then adds a table to the end of the document using doc.add_table(), which takes the number of rows and columns as arguments. The number of rows is set to df_main.shape[0] + 1 (adding one extra row for the header row) and the number of columns is set to df_main.shape[1].

The code then adds the header row to the table by iterating through the columns of the df_main dataframe and setting the values of the first row of the Word table using the .cell() method of the t object (which is a reference to the table we added to the Word document earlier). The text value of the jth column in the df_main dataframe is set as the text value of the corresponding cell in the Word table.

Finally, the code adds the rest of the data from the df_main dataframe to the Word table by iterating through all rows and columns of the dataframe and setting the text value of each corresponding cell in the Word table using the .cell() method.

Finally, the code saves the Word document as a file called "wordfile.docx" using doc.save().
