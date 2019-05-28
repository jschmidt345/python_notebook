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
while True:
    user_response = input('What would you like to do? \n>'
                        '1. Add note\n>'
                        '2. Print a note\n>'
                        '3. Exit'    )
    if user_response == '1':
            note_id = counter 
            counter += 1
            content = input('What is the note? \n >')
            note = (note_id, str(now), content)
            notebook.append(note)
            print(notebook)
    elif user_response == '2':
        for note in notebook:
            print(f'Id: {note[0]} | Note: {note[1]}')
    elif user_response == '3':
        exit()
    else:
            print('invalid input')    
    
    
print(notebook)