import qrcode
import cv2
import numpy as np
import time
import os
import db

machineTyp = input('請輸入機型: ')
machineNo = input('請輸入機號: ')
place1 = input('請輸入機台場區,0:展示場 、 1:一廠 、 2:二廠 、 3:三廠: ')
loc1 = input('請輸入機台位置')
chk_place1 = int(place1[0:4])
print(chk_place1)
if chk_place1 <= 4:
    # 建立qr code時，將機台寫入機台表內
    if machineTyp and machineNo and place1 and loc1 != "":
        sql = f"""
            insert into mac_loc (machineTyp1 , machineNo1 , place1 , loc1, enable1)
            values('{machineTyp}' , '{machineNo}' , '{place1}' , '{loc1}' , '1')
        """
        print(sql)
        db.insert_or_update_data(sql)
        url = 'http://192.168.50.133:5000/' + machineTyp + '/'+machineNo
    print(url)
    # 改變qrcode的大小
    qr = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    # img2 = qrcode.make(url)    # 要轉換成 QRCode 的文字
    time.sleep(1)
    img2 = qr.make_image()
    img2.save(machineTyp+'No'+machineNo+'.png')
    folder_path = machineTyp+'No'+machineNo+'.png'

    # 建立一空白區域
    shape = (256, 490, 3)
    img1 = np.full(shape, 255).astype(np.uint8)
    time.sleep(1)
    # cv2.imshow('img1', img1)
    # cv2.waitKey(0)
    img2 = cv2.imread(folder_path)
    time.sleep(1)
    # cv2.imshow('img2', img2)
    # cv2.waitKey(0)
    img = np.vstack((img2, img1))
    # cv2.imshow('img', img)
    # cv2.waitKey(0)

    text = machineTyp+' \nNo:'+machineNo
    y0, dy = 550, 100
    # org = (0,600)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color = (0, 0, 0)
    thickness = 5
    lineType = cv2.LINE_AA
    for i, text in enumerate(text.split('\n')):
        y = y0+i*dy
        cv2.putText(img, text, (30, y), fontFace,
                    fontScale, color, thickness, lineType)
    cv2.imwrite(machineTyp+'No'+machineNo+'.jpg', img)
    os.remove(folder_path)
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
else:
    print("請輸入正確廠區位置")
