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
note_id = counter 
counter += 1


now = date.today()
print(now)
content = 'This is content'

note = (note_id, str(now), content)
print(note)

notebook.append(note)
print(notebook)