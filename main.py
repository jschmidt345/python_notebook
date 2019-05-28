from datetime import date


'''
Note Book App

Notes will habe three parts an
ID
Content
Date/Time
'''

notebook = []
counter = 1
now = date.today()

while counter <= 5: 
    note_id = counter 
    counter += 1
    content = input('What is the note? \n >')
    note = (note_id, str(now), content)
    notebook.append(note)
    print(notebook)