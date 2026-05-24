import uvicorn
from fastapi import FastAPI, File, UploadFile
import shutil
import os
import csv

app = FastAPI()

# 저장폴더 상대경로
upload_dict = 'save'


@app.post("/join-ana")
async def upload_file(name:str,student_number:str,phone_number:str,why_wnat_to_join:str,portfolio: UploadFile = File(...)):
    content = await portfolio.read()
    
    # 실제로 모든 데이터가 저장될 경로 설정
    file_path = os.path.join(upload_dict, portfolio.filename)

    file_name = f"{student_number}_{name}_지원정보"
    csv_path = os.path.join(upload_dict, f"{file_name}.csv")
    file_exists = os.path.exists(csv_path) # 파일이 존재 하는지 확인 


    # ai 사용 했습니다. 설명은 모두할 수 있습니다 ====================================
    with open(csv_path, mode="a", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        # 파일이 처음 생성되는 순간에만 맨 위에 제목(헤더)을 달아줍니다.

        if not file_exists: # 파일이 처음 만들어졌을때만 추가
            writer.writerow(["이름", "학번", "전화번호", "지원동기"])

        # 데이터를 한줄로 기록
        writer.writerow([
            name, 
            student_number, 
            phone_number, 
            why_wnat_to_join
        ])
    # ai 사용 했습니다. 설명은 모두할 수 있습니다 ====================================



    # 포트폴리오 파일 저장
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(f"{student_number}_{name}_포트폴리오", buffer)


    return {"status": 'success', "massage": '모든 데이터가 정상적으로 업로드 되었습니다!'}

if __name__ == '__main__':
     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)