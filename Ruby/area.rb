# def rectangular(side1, side2)
#     if side1 * side 2 <= 1.2
#         puts "L: #{side1} x #{side2}"
#     else
#         break
#     end
# end

# rectangular((0.8..1.2).step(0.1),(0.8..1.2).step(0.1))

(0.8..1.2).step(0.05).each do |x|
    (0.8..1.2).step(0.1).each do |y|
        if x * y > 0.95 && x * y < 1.5
            puts "L: #{x} x #{y} = #{x * y}"
        end 
    end
end

(0.5..1).step(0.05).each do |x|
    if (Math::PI * (x * x)) > 0.95 && (Math::PI * (x * x)) < 1.5
    puts "Raio: #{x} x #{x} = #{Math::PI * (x * x)}"
    end
end

