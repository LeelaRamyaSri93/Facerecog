import cv2 as cv
import face_recognition
import numpy as np
import os
from datetime import datetime


path = 'Images'
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curImg = cv.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)


def find_encodings(images):
    encode_list = []
    for img in images:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

def markAttendance(name):
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    filename = f'attendance_{date_str}.csv'
    
   
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.writelines("Name,Time\n")

    with open(filename,"r+") as f:
        myDataList=f.readlines()
        nameList=[]
        for line in myDataList:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            time_str=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{time_str}')


encode_list_known = find_encodings(images)
print('Encoding complete')


cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
    
   
    img_small = cv.resize(img, (0, 0), fx=0.25, fy=0.25)
    img_small = cv.cvtColor(img_small, cv.COLOR_BGR2RGB)

    
    faces_cur_frame = face_recognition.face_locations(img_small)
    encodes_cur_frame = face_recognition.face_encodings(img_small, faces_cur_frame)

    for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
        face_distances = face_recognition.face_distance(encode_list_known, encode_face)
        best_match_index = np.argmin(face_distances)
        
        if face_distances[best_match_index] < 0.6:  
            name = classNames[best_match_index].upper()
            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv.rectangle(img, (x1, y1 - 35), (x2, y1), (0, 255, 0), cv.FILLED)
            cv.putText(img, name, (x1 + 6, y1 - 6), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv.imshow('Webcam', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
