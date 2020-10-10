for i in 1...10
    print i, " "
end
print "\n"
for animal in ['monkey', 'dog', 'cat', 'cow', 'bird']
    print animal, " "
  end
print "\n"
for i in (1...100).step(3)
    print i, " "
end
print "\n"
x = 0
begin
    puts "begin #{x}"
    x += 1
end while x != 5
