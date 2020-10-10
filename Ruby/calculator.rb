def calculator
    puts "Digite um numero ou um operador matemático(+, -, *, /):"
    digits =[]
    while (input = gets)
        if /^[0-9]+$/.match input
            digits << input.chomp.to_i
        else
            #operator = String
            operator = input.chomp
            result = nil
            operands = [digits.pop, digits.pop]
            if operator == "+"
                result = operands[0] + operands[1]
            elsif operator == "*"
                result = operands[0] * operands[1]
            elsif operator == "-"
                result = operands[1] - operands[0]
            else
                result = operands[1] / operands[0]
            end
        puts result
        digits << result
        end
    end
end        

a, b, c, d = 1, 2, 3, 4
puts a * b + c / b ** d