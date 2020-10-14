class BookInStock
    attr_reader :isbn
    attr_accessor :price
  
    def initialize (isbn, price)
      @isbn = isbn
      @price = Float(price)
    end
  
    def price_in_cents
      Integer(price*100)
    end
  
    def price_in_cents=(cents)
      @price = cents / 100.0
    end
  
    def to_s
      "ISBN: #{@isbn}, price: #{@price}"
    end
  end
  
  b1 = BookInStock.new("isbn-1", 34.50)
  puts "Price             = #{b1.price}"
  puts "Price in cents    = #{b1.price_in_cents}"
  b1.price_in_cents       = 1234
  puts "Price             = #{b1.price}"
  puts "Price in cents    = #{b1.price_in_cents}"