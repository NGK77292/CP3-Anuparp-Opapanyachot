'''
ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง)
หากสำเร็จ โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ
หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด
'''

userName = input("User Name: ")
passWord = input("Password: ")
rayongPkg = 3200
phuketPkg = 5500
chengmaiPkg = 4500
if userName == "note" and passWord == "123":
    print("================================")
    print("Welcome to ABC shop :))")
    print("1. Rayong Package :", rayongPkg, "THB")
    print("2. Phuket Package :", phuketPkg, "THB")
    print("3. Chengmai package :", chengmaiPkg, "THB")
    print("================================")
    userSelect = int(input("Please Select Package: "))
    if userSelect == 1:
        totalPeople = int(input("No of People: "))
        result = totalPeople * rayongPkg
        print("================================")
        print("Your Package is Rayong Package!!")
        print("Package price :", rayongPkg, "THB")
        print("Total people : ", totalPeople)
        print("================================")
        print("Total amount : ", result, "THB")
    elif userSelect == 2:
        totalPeople = int(input("No of People: "))
        result = totalPeople * phuketPkg
        print("================================")
        print("Your Package is Phuket Package!!")
        print("Package price :", phuketPkg, "THB")
        print("Total people : ", totalPeople)
        print("================================")
        print("Total amount : ", result, "THB")
    elif userSelect == 3:
        totalPeople = int(input("No of People: "))
        result = totalPeople * chengmaiPkg
        print("================================")
        print("Your Package is Chengmai Package!!")
        print("Package price :", chengmaiPkg, "THB")
        print("Total people : ", totalPeople)
        print("================================")
        print("Total amount : ", result, "THB")
    else:
        print("Your selected package is unavailable!!")
else:
    print("Your user name or password is INCORRECT!!")
    print("Please retry again")