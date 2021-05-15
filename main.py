from tkinter import *

seed = '93eRbqJFL9TEeSHVNpxwwzvmau8RtWjJmTpOkfz8IQYShJiQw77WfJAy2twkGQkY5cNJAlqRQA9a8rUTK0wbo86qCztzFHJN5QjR'

def Key_to_password(program, account):
    p_key = list_creater(program)
    A_key = list_creater(account)
    Passwd = []
    low = 0
    supper = 0
    num = 0
    marker = 0
    for i in range(0, 16):
        corner_marker = int(p_key[i] + A_key[i])
        # print(corner_marker)
        if seed[corner_marker].islower():
            low+=1
        if seed[corner_marker].isupper():
            supper+=1
        if seed[corner_marker].isdigit():
            num+=1
        text = seed[corner_marker]
        if marker == 13 and low ==0:
            text = 'z'
        if marker == 14 and supper ==0:
            text = 'Z'
        if marker == 15 and num ==0:
            text=  '9'

        Passwd.append(text)
        marker+=1
    Passwd_check(Passwd)
    passwd = list_2_str(Passwd)
    passwd_return.set(passwd)
    return 0

def Passwd_check(passwd):
    low = 0
    high = 0
    num = 0
    Low = []
    High = []
    Num = []
    for i in passwd:
        if i.islower():
            Low.append(i)
            low += 1
    for i in passwd:
        if i.isupper():
            High.append(i)
            high += 1
    for i in passwd:
        if i.isdigit():
            Num.append(i)
            num += 1
    if low==0 or high ==0 or num ==0:
        return '生成密码错误'
    return '密码生成成功'


def list_2_str(passwd):
    password_final = ''
    for i in passwd:
        password_final += i
    print(password_final)
    return password_final


def list_creater(input):
    input = bytes(input, 'UTF-8')
    HEX_output = input.hex()
    HEX_output = str(int(HEX_output, 16))
    num = 0
    list = []
    while (True):
        if len(HEX_output) < 16:
            HEX_output += HEX_output
        else:
            # print(HEX_output)
            break
    for i in HEX_output:
        if num > 15:
            break
        list.append(i)
        num += 1
    # print(list)
    return list


def Hex_format(Hex_input):
    if len(Hex_input) < 32:
        adada = 1


def process():
    personal_mark = p_mark.get()
    program_name = p_name.get()
    account = A_name.get()
    print(personal_mark)
    print(program_name)
    print(account)
    if personal_mark =='':
        personal_mark = 'def'
    if program_name == '':
        program_name == 'soft'
    if account == '':
        account = 'keyia'
    mark1 = personal_mark + program_name
    Key_to_password(mark1, account)




windows = Tk()
windows.title('密码生成器')
windows.geometry()
#####################个人标识##################################
p_mark = StringVar()
text_tag = Label(windows, text='标识').grid(row=0, column=0)
tag_input = Entry(windows, textvariable=p_mark).grid(row=0, column=1)
#####################软件名称###############################
p_name = StringVar()
text2 = Label(windows, text='软件名称').grid(row=1, column=0)
pic_num = Entry(windows, textvariable=p_name).grid(row=1, column=1)
####################账号################################
A_name = StringVar()
text3 = Label(windows, text='账号助记符').grid(row=2, column=0)
poet_num = Entry(windows, textvariable=A_name).grid(row=2, column=1)
#################返回信息######################################
passwd_return = StringVar()
Label(windows, text='返回信息').grid(row=3, column=0)
Text_show = Entry(windows,textvariable=passwd_return,state='readonly')
Text_show.grid(row=3, column=1)
################开始案件########################################
start_buttom = Button(windows, text='生成', command=process).grid(row=4, column=1)

windows.mainloop()