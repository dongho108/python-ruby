real_id = "egoing"
real_pwd = "1234"

puts("아이디를 입력해주세요")
input_id = gets.chomp()
puts("비밀번호를 입력해주세요")
input_pwd = gets.chomp()

if input_id == real_id
  if input_pwd == real_pwd
    puts("Hello! ")
  else
    puts("비밀번호가 틀립니다")
  end
else
  puts("아이디가 틀립니다")
end
