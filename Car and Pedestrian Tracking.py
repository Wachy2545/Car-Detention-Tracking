import cv2
#img_file='imageCar2.jfif'
video= cv2.VideoCapture('video.mp4')
classifier_file='cars.xml'
car_tracker=cv2.CascadeClassifier(classifier_file)

while True:
    read_successful, frame=video.read()
    
    

    if read_successful:
        grayscaled_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    
    cars= car_tracker.detectMultiScale(grayscaled_frame)

    for(x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    

    cv2.imshow('CLever Car Detector', frame)
    cv2.waitKey(1)

print("code completed")
"""
img= cv2.imread(img_file)



car_tracker=cv2.CascadeClassifier(classifier_file)
black_n_white=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars= car_tracker.detectMultiScale(black_n_white)

for(x,y,w,h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('Clever Programmer Car', img)

cv2.waitKey()
"""
print('open code')
