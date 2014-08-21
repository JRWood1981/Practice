name=raw_input('What is your name?: ')
birthday=raw_input('What month were you born?: ')
lastname=raw_input('Last name?: ')

print ("Hi %s, Let us be friends!") % name;

malefemale = raw_input('Male or female?: ')
if malefemale == "m":
    print ('Mr. %s, Hello!') % lastname;
elif malefemale == 'male':
    print ('Mr. %s, Hello!') % lastname;
elif malefemale == "f":
    print ('Mrs. %s, Hello!') % lastname;
elif malefemale == "female":
    print ('Mrs. %s, Hello!') % lastname;
else:
    print ('%s..? really??') % malefemale;

def rerun():
    choice = raw_input('Enter your choice [1-4]: ');
    choice = int(choice);

print ('***')
print (' MAIN MENU ')
print ('1. Back-up')
print ('2. User agreement')
print ('3. Reboot')
print ('4. Make love to your husband')
choice = raw_input('Enter your choice [1-4]: ')
choice = int(choice)


    

if choice == 1:
    print ("Starting backup....")
elif choice == 2:
    print ('Starting user agreement...')
elif choice == 3:
    print ('Rebooting the server...')
elif choice == 4:
    print ('%s YES LETS GO UP STAIRS NOW!!!') % name;
else:
    print ('Invalid number, try again..')
    rerun()
        
          

