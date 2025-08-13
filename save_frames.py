import cv2
import sqlite3
import os
import time
os.makedirs('captured_frames',exist_ok=True)
conn=sqlite3.connect('frame_metadata_db')
cursor=conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS 
frame_info(
               id INTEGER PRIMARY KEY,
               timestamp TEXT,
               filename TEXT
               );
""")
conn.commit()

cap=cv2.VideoCapture(0)
frame_count=0
total_frames=5
while frame_count<total_frames:
    ret,frame=cap.read()
    if not ret:
        print('failed')
        break
    timestamp=time.strftime("%y%m%d-%H%M%S")
    filename=f"captured_frames/frame_{frame_count}_{timestamp}.jpg"
    cv2.imwrite(filename,frame)

    cursor.execute("INSERT INTO frame_info(timestamp,filename)VALUES(?,?)",(timestamp,filename))
    conn.commit()

    cv2.imshow('Camera()',frame)
    frame_count+=1

    if cv2.waitKey(1000) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
conn.close()