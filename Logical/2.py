real_id = "egoing"
real_pwd = "1234"
input_id = input("아이디를 입력해주세요.\n")
input_pwd = input("비밀번호를 입력해주세요.\n")
if input_id == real_id:
    if input_pwd == real_pwd:
        print("Hello! ")
    else:
        print("비밀번호가 틀립니다 ")
else:
    print("아이디가 틀립니다")
