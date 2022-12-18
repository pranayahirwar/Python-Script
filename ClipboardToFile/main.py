import pyperclip

with open('CopyData.txt', 'a') as openfile:
    s = ''
    flag = False
    print('To BREAK this copy bb in your clipboard.')
    
    openfile.write('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n')
    openfile.write('Keywords of the session --> \n \n')
    while True:
        s = pyperclip.waitForNewPaste()
        if s != 'bb':
            if flag == True:
                # s = pyperclip.waitForNewPaste()
                openfile.write(f"{s} \n\n")
                print("Defination of word copied to file.")
                flag = False
            else:
                # s = pyperclip.waitForNewPaste()
                openfile.write(f'{s}: ')
                flag = True
                print("Word copied to file.")
        else:
            break
        # print('Done')
    
    print("WORDS ARE COPIED.")
