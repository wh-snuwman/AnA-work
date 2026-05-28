

## :: 오퍼레이터

변환하고자 하는 값이나 컬럼 뒤에 `::데이터타입`을 붙여주면 형변환(Casting)이 완료됨.

```sql
SELECT '100'::INTEGER + 50; -- 결과: 150
```

---
## LEFT & RIGHT 함수

LEFT('문자열', 개수): 왼쪽(처음)부터 지정한 개수만큼 글자를 잘라옴.
RIGHT('문자열', 개수): 오른쪽(끝)부터 지정한 개수만큼 글자를 잘라옴

```sql
SELECT LEFT('김대홍', 1); -- 결과: '김'

SELECT RIGHT('010-1234-5678', 4); -- 결과: '5678'
```

---
## LOWER & UPPER  함수

LOWER('문자열'): 모든 알파벳을 소문자로 바꿔줌
UPPER('문자열'): 모든 알파벳을 대문자로 바꿔줌
```sql
SELECT * FROM users WHERE LOWER(input_id) = 'AnAisBest';
```