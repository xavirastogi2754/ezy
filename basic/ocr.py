import requests
import time
from PIL import Image

# subscription_key = "e85691b1ed974eab8b37631e40a1ad43"
# assert subscription_key

# vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
# text_recognition_url = vision_base_url + "recognizeText"

# location = 'C:/ezy/work/forms/'
# front_location = location + image1 + '.jpg'
# back_location = location + image2 + '.jpg'


# back_image_path = resizeLocation + image2 + '_crop.jpg'

def resizeImage(path = '', dest = ''):
    im = Image.open(path)
    size = 1240, 1753
    imx = im.resize(size, Image.ANTIALIAS)
    imx.save(dest)

 # image_path = "C:/ezy/work/forms/crops/cropy.jpg"
def frontSections(path = ''):
    im = Image.open(path)
    
    sizex1 = (363, 462, 1123, 879)
    page1a = im.crop(sizex1)
    pathx1 = 'C:/career/ezyschooling/backend/images/page1a.jpg'
    page1a.save(pathx1)

    sizex2 = (363, 880, 562, 942)
    page1b = im.crop(sizex2)
    pathx2 = 'C:/career/ezyschooling/backend/images/page1b.jpg'
    page1b.save(pathx2)

    sizex3 = (363, 941, 1123, 1356)
    page1c = im.crop(sizex3)
    pathx3 = 'C:/career/ezyschooling/backend/images/page1c.jpg'
    page1c.save(pathx3)

    sizex4 = (363, 1358, 450, 1599)
    page1d = im.crop(sizex4)
    pathx4 = 'C:/career/ezyschooling/backend/images/page1d.jpg'
    page1d.save(pathx4)

    pathsx = [pathx1, pathx2, pathx3, pathx4]
    return pathsx

# its working for 10 api requests per program so far !
def backSections(path = ''):
    im = Image.open(path)
    
    size1 = (363, 186, 1160, 433)
    page2a = im.crop(size1)
    path1 = 'C:/career/ezyschooling/backend/images/page2a.jpg'
    page2a.save(path1)

    size2 = (363, 431, 543, 478)
    page2b = im.crop(size2)
    path2 = 'C:/career/ezyschooling/backend/images/page2b.jpg'
    page2b.save(path2)

    size3 = (363, 476, 1160, 754)
    page2c = im.crop(size3)
    path3 = 'C:/career/ezyschooling/backend/images/page2c.jpg'
    page2c.save(path3)

    size4 = (363, 785, 1160, 1031)
    page2d = im.crop(size4)
    path4 = 'C:/career/ezyschooling/backend/images/page2d.jpg'
    page2d.save(path4)

    size5 = (363, 1031, 542, 1078)
    page2e = im.crop(size5)
    path5 = 'C:/career/ezyschooling/backend/images/page2e.jpg'
    page2e.save(path5)

    size6 = (363, 1074, 1160, 1351)
    page2f = im.crop(size6)
    path6 = 'C:/career/ezyschooling/backend/images/page2f.jpg'
    page2f.save(path6)

    # size7 = (363, 1385, 1160, 1535)
    # page2g = im.crop(size7)
    # path7 = 'C:/ezy/work/forms/crops/page2g.jpg'
    # page2g.save(path7)

    paths = [path1, path2, path3, path4, path5, path6]
    return paths


def ocrExtraction(path = ''):
    subscription_key = "e85691b1ed974eab8b37631e40a1ad43"
    assert subscription_key

    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
    text_recognition_url = vision_base_url + "recognizeText"

    image_data = open(path, "rb").read()

    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type' : 'application/octet-stream'}
    params  = {'mode' : 'Handwritten'}
    response = requests.post(text_recognition_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    operation_url = response.headers["Operation-Location"]

    analysis = {}
    while "recognitionResult" not in analysis:
        response_final = requests.get(operation_url, headers=headers)
        analysis = response_final.json()
        time.sleep(1)

    # polygons = [line['boundingBox'] for line in analysis["recognitionResult"]["lines"]]
    # print(polygons)
    polygons = [line['text'] for line in analysis["recognitionResult"]["lines"]]
    # print(polygons)
    return polygons

# location = 'C:/ezy/work/forms/'
# resizeLocation = 'C:/ezy/work/forms/crops/'

# x = raw_input('Submit the first page; Enter file name : ')
# front_location = location + x + '.jpg'
# front_image_path = resizeLocation + x + '_crop.jpg'
# resizeImage(front_location, front_image_path)
# frontList = frontSections(front_image_path)

# dataList1 = []

# if (len(frontList) != 0): 
#     for f in frontList:
#         pol = ocrExtraction(f)
#         dataList1.append(pol)
# # print(dataList1)

# # time.sleep(1)

# dataList2 = []

# y = raw_input('Submit the second page; Enter file name : ')
# back_location = location + y + '.jpg'
# back_image_path = resizeLocation + y + '_crop.jpg'
# resizeImage(back_location, back_image_path)
# backList = backSections(back_image_path)

# if (len(backList) != 0):
#     for b in backList:
#         polx = ocrExtraction(b)
#         dataList2.append(polx)

# # dataList = [dataList1, dataList2]
# # print(dataList2)

# personal_details_list = ['FULL NAME', 'APPLYING FOR', 'D.O.B', 'GENDER', 'AADHAR NUMBER', 'BLOOD GROUP', 'RELIGION', 'CATEGORY', 'NATIONALITY', 'ADDRESS', 'CITY', 'STATE', 'PIN CODE', 'COUNTRY', 'SINGLE CHILD?', 'FIRST CHILD?', 'SINGLE PARENT?', 'NO PARENT?']
# father_details_list = ['FULL NAME', 'AGE', 'EDUCATION', 'OCCUPATION', 'DESIGNATION', 'ANNUAL INCOME', 'OFFICE ADDRESS', 'OFFICE NUMBER', 'MOBILE NUMBER', 'EMAIL-ID']
# mother_details_list = father_details_list
# emergency_details_list = ['FULL NAME', 'CONTACT NUMBER', 'RELATIONSHIP']

# p1s1 = dataList1[0]
# p1s2 = dataList1[1]
# p1s3 = dataList1[2]
# p1s4 = dataList1[3]

# p2s1 = dataList2[0]
# p2s2 = dataList2[1]
# p2s3 = dataList2[2]
# p2s4 = dataList2[3]
# p2s5 = dataList2[4]
# p2s6 = dataList2[5]
# # p2s7 = dataList2[6]


# full_nam1 = p1s1[0]
# apply_for = p1s1[1]
# dob = p1s1[2]
# gender = p1s1[3]
# aadhar = p1s1[4]
# bg = p1s1[5]
# religion = p1s1[6]

# cat = p1s2[0]

# nat = p1s3[0]
# addr = p1s3[1] + ', ' + p1s3[2]
# city = p1s3[3]
# state = p1s3[4]
# code = p1s3[5]
# country = p1s3[6]

# sc = p1s4[0]
# fc = p1s4[1]
# sp = p1s4[2]
# np = p1s4[3]

# full_nam2 = p2s1[0]
# age = p2s1[1]
# edu = p2s1[2]
# occ = p2s1[3]
# des = p2s1[4]

# inc = p2s2[0] + ' LACS'

# email = p2s3[-1]
# mob_num = p2s3[-2]
# off_num = p2s3[-3]
# addr2 = []
# for i in p2s3:
#     if i not in [email, mob_num, off_num]:
#         addr2.append(i) 

# addr2 = ', '.join(addr2)

# full_nam3 = p2s4[0]
# age2 = p2s4[1]
# edu2 = p2s4[2]
# occ2 = p2s4[3]
# des2 = p2s4[4]

# inc2 = p2s5[0] + ' LACS'

# email2 = p2s6[-1]
# mob_num2 = p2s6[-2]
# off_num2 = p2s6[-3]
# addr3 = []
# for i in p2s6:
#     if i not in [email2, mob_num2, off_num2]:
#         addr3.append(i) 

# addr3 = ', '.join(addr3)

# # full_nam4 = p2s7[0]
# # contact = p2s7[1]
# # relation = p2s7[2]

# personal_data_list = [full_nam1, apply_for, dob, gender, aadhar, bg, religion, cat, nat, addr, city, state, code, country, sc, fc, sp, np]
# father_data_list = [full_nam2, age, edu, occ, des, inc, addr2, off_num, mob_num, email]
# mother_data_list = [full_nam3, age2, edu2, occ2, des2, inc2, addr3, off_num2, mob_num2, email2]
# # emergency_data_list = [full_nam4, contact, relation]

# personal_data_list = [str(x) for x in personal_data_list]
# father_data_list = [str(x) for x in father_data_list]
# mother_data_list = [str(x) for x in mother_data_list]


# personal_dict = dict(zip(personal_details_list, personal_data_list))
# father_dict = dict(zip(father_details_list, father_data_list))
# mother_dict = dict(zip(mother_details_list, mother_data_list))
# # emergency_dict = dict(zip(emergency_details_list, emergency_data_list))

# print "\n"

# for i in personal_details_list:
#     print(i + " : " + personal_dict[i])
# print("\n")
# for i in father_details_list:
#     print(i + " : " + father_dict[i])
# print("\n")
# for i in mother_details_list:
#     print(i + " : " + mother_dict[i])
# print("\n")

# print(personal_dict)
# print "\n"
# print(father_dict)
# print "\n"
# print(mother_dict)
# print "\n"
# print emergency_dict
# print "\n"
