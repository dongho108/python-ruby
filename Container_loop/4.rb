puts("아이디를 입력해주세요.\n")
input_id = gets.chomp()
members = ['egoing', 'k8805', 'leezche']
for member in members do
    if input_id == member
        print("Hello!, " + member)
        exit
    end
end
puts('who are you?')
