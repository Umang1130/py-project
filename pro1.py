import os

def create_file(filename):
    try :
        with open(filename, 'x') as f :
            print(f'The file {filename} created successfully !')
    except FileExistsError :
        print('The file already exist !')
    except Exception as e :
        print('An error has occured !')

def read_file(filename) :
    try :
        with open(filename, 'r') as f :
            content = f.read()
            print(f'The content of the file {filename} : \n{content}')
    except FileNotFoundError :
        print(f"The file {filename} not found !")
    except Exception as e :
        print(f'An error has occured !')

def delete_file(filename) :
    try :
        os.remove(filename)
        print(f"The file '{filename} deleted successfully !")
    except FileNotFoundError :
        print(f"The file '{filename}' not found !")
    except Exception as e :
        print('An error has occured !')

def view():
    files = os.listdir()
    if not files :
        print('file not found !')
    else :
        print('These are all files - ')
        for f in files :
            print(f)

def edit_file(filename):
    try :
        with open(filename, 'a') as f :
            content = input('Enter the data : ')
            f.write(content)
            print('The data entered successfully !')
    except FileNotFoundError :
        print(f"The file {filename} not found !")
    except Exception as e :
        print('An error has occured !')

def main():
    while True :
        print('- FILE MANAGEMENT SYSTEM -')
        print('1. Create file' \
              '\n2. View all files' \
              '\n3. delete file' \
              '\n4. Read file' \
              '\n5. Edit file' \
              '\n6. EXit')

        c = int(input('Enter your choice : '))

        if c == 1 :
            filename = input('Enter the name to create a file : ')
            create_file(filename)
        elif c == 2 :
            view()

        elif c == 3 :
            filename = input('Enter the name of the file to delete :')
            delete_file(filename)                                            
        elif c == 4 :
            filename = input('Enter the file to read the content : ')
            read_file(filename)
        elif c == 5 :
            filename = input('Enter the file to edit : ')
            edit_file(filename)
        elif c == 6 :
            print('Closing the system...')
            break
        else :
            print('In-valid choice ! ')
        print('\n')    

if __name__ : '__main__'          
main()          