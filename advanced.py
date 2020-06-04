# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:29:05 2020

@author: 18127
"""

if __name__ == "__main__":

    # sum = input("输入一个表达式：")
    # #计算一个表达式
    # sum = eval(sum)
    # print(sum)
    # #保留四位小数
    # a = 0.56789
    # print(round(a, 4))
    # print(0.4-0.3)
    #补齐长度
    # print("%20s" % "hello")
    # print("%-20s" % "hello")

    with open("teleAddressBook.txt", "r", encoding="UTF-8") as file1:
        with open("emailBook.txt", "r", encoding="UTF-8") as file2:
            #跳过第一行
            file1.readline()
            file2.readline()
            #按行形成两个列表
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            list1_name = []
            list1_tel = []
            list2_name = []
            list2_email = []

            # print(lines1)

            for line in lines1:
                elements = line.split()
                # print(elements)
                list1_name.append(elements[0])
                list1_tel.append(elements[1])
                # print(list1_name)
            for line in lines2:
                elements = line.split()
                list2_name.append(elements[0])
                list2_email.append(elements[1])
                
            lines = []
            lines.append("姓名\t电话\t\t邮箱\n")

            for i in range(len(list1_name)):
                s = ""
                if list1_name[i] in list2_name:
                    j = list2_name.index(list1_name[i])
                    s = "\t".join([list1_name[i], list1_tel[i], list2_email[j]])
                    s += "\n"
                else:
                    s = "\t".join([list1_name[i], list1_tel[i], str("---------")])
                    s += "\n"
                lines.append(s)
            for i in range(len(list2_name)):
                s = ""
                if list2_name[i] not in list1_name:
                    s = "\t".join([list1_name[i], str("---------"), list2_email[i]])
                    s += "\n"
                    lines.append(s)
            file3 = open("addressBook.txt", "w+", encoding="UTF-8")
            file3.writelines(lines)
    file3.close()


                    

    