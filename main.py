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
def menu():
    user_response = input('What would you like to do? \n>'
                        '1. Add note\n>'
                        '2. Print a note\n>'
                        '3. Exit'    )
    return user_response

def note_create():
    content = input('What is the note? \n >')
    global counter
    note_id = counter
    note = (note_id, str(now), content)
    notebook.append(note)
    counter += 1
    return notebook
def noteprint():
    for note in notebook:
            print(f'Id: {note[0]} | Note: {note[1]}')
    


def run():
    while True:
        choice = menu()
    if choice == '1':
        note_create()
    elif choice == '2':
        noteprint()
    elif choice == '3':
        exit()
    else:
        print('invalid input')    
    
    
if __name__ == '__main__': 
    run()