# pracdtical python에 나오는 설명 모음 

___________________________________________________________
## 1.6 파일관리

### 파일 입력과 출력

파일을 연다.
>f = open('foo.txt', 'rt') # 읽기를 위해 열기 (텍스트)  
>g = open('bar.txt', 'wt') # 쓰기를 위해 열기 (텍스트)

모든 데이터를 읽는다.
>data = f.read()  
>data = f.read([maxbytes]) # 'maxbytes' 바이트까지만 읽음

텍스트를 기록한다.
>g.write('some text')

마쳤으면 파일을 닫는다.
>f.close()  
>g.close()  

파일을 열었으면 제대로 닫아야 하는데, 이 단계를 잊어버리기 쉽다.  
따라서, 다음과 같이 with 문을 사용하면 좋다.
>with open(filename, 'rt') as file:  # file 파일을 사용  
>...  
    # 명시적으로 닫지않아도 된다  

### 파일 데이터를 읽는 일반적인 방법

파일 전체를 한번에 읽어 문자열로 처리한다.  
>with open('foo.txt', 'rt') as file:  
>data = file.read()  # data는 foo.txt의 텍스트 전체로된 문자열이다'

파일을 한 행씩 읽어 내려가기.  
>with open(filename, 'rt') as file:  
>for line in file:  # 행을 처리

### 파일에 쓰는 일반적인 방법

문자열 데이터를 기록한다.  
>with open('outfile', 'wt') as out:  
>out.write('Hello World\n')  
>...

print 함수의 출력을 재지정 (redirect) 한다.  
>with open('outfile', 'wt') as out:  
>print('Hello World', file=out)  
>...

