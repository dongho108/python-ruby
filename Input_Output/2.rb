real_egoing = "11"
real_k8805 = "ab"
puts("아이디를 입력해주세요")
input = gets.chomp()
if input == real_egoing
  puts("Hello! "+ "egoing")
elsif input == real_k8805
  puts("Hello! "+ "k8805")
else
  puts("who are you")
end
