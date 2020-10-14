class BookInStock
    attr_reader :isbn
    attr_accessor :price
  
    def initialize (isbn, price)
      @isbn = isbn
      @price = Float(price)
    end
  
    def to_s
      "ISBN: #{@isbn}, price: #{price}"
    end
  end
  
  b1 = BookInStock.new("123456890", 34.50)
  puts "ISBN     = #{b1.isbn}"
  puts "Price    = #{b1.price}"
  b1.price = b1.price * 0.85;
  puts "New price = #{b1.price}"