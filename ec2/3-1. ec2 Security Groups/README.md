---
style: |
  img {
    display: block;
    float: none;
    margin-left: auto;
    margin-right: auto;
  }
marp: true
paginate: true
---
### 단계1: Instance의 Security Group 확인 
![alt text](./img/image.png)

---
### 단계2: Inbound rules 확인
- 외부에서 내부(ec2)에 접속할 수 있는 Rule 정의 

![alt text](./img/image-1.png)

---
### 단계3: Outbound rules 확인 
- 내부(ec2)에서 외부로 접속할 수 있는 Rule 정의

![alt text](./img/image-2.png)

---
### 단계4: Inbound rules 변경 
![alt text](./img/image-3.png)

---
- 예제: http 프로토콜 & Apache Tomcat Server 추가 

![alt text](./img/image-4.png)

---
- 변경 내용 확인 

![alt text](./img/image-5.png)

