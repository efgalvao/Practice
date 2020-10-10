ifi = []
y = 0
while y < 10    
    if y < 10
        ifi << y
        y = y + 1
    end
    print(ifi," ifi ", "\n")
end

unlesse = []
x=0
while x < 10    
    unless x > 10
      unlesse << x
      x = x + 1
    end
    print(unlesse," unlesse ", "\n")
end


def to_seconds(unity, qtdy)
    case unity
    when :hour
        qtdy * 3600
    when "minute"
        qtdy * 60
    when :day
        qtdy * 86400
    else
        puts "invalid command"
    end
end

puts to_seconds(:day, 2)