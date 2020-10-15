class Parent
    def say_hello
      puts "Hello from #{self}"
    end
  end
  p = Parent.new
  p.say_hello
  
  
  class Child < Parent
  end
  c = Child.new
  c.say_hello

#Mixin
  class Person
    include Comparable
    attr_reader :name
  
    def initialize(name)
      @name = name
    end
  
    def to_s
      "#{@name}"
    end
  
    def <=>(other)
      self.name <=> other.name end
  end
  
  p1 = Person.new("Matz")
  p2 = Person.new("Guido")
  p3 = Person.new("Larry")
  
  # Comparing names
  if p1 > p2
    puts "#{p1.name}'s name > #{p2.name}'s name"
  end
  
  # Sorting an array of Person objects
  puts "Lista ordenada:"
  puts [ p1, p2, p3].sort