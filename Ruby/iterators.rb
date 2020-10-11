# class File
#   def self.open_and_process(*args)
#     f = File.open(*args)
#     yield f
#     f.close()
#   end
# end

# File.open_and_process("songdata", "r") do |file|
#   while line = file.gets
#     puts line
#   end
# end

# class ProcExample

#   def pass_in_block(&action)
#     @stored_proc = action
#   end

#   def use_proc(parameter)
#     @stored_proc.call(parameter)
#   end

# end

# eg = ProcExample.new
# eg.pass_in_block { |param| puts "The parameter is #{param}" }
# eg.use_proc(77)

# def create_block_object(&block)
#   block
# end

# bo = create_block_object { |param| puts "You called me with #{param}" }
# bo.call 99
# bo.call "cat"

# bo = lambda { |param| puts "You called me with #{param}" }
# bo.call 69
# bo.call "dog"

# def n_times(thing)
#     lambda {|n| thing * n }
#   end

# p1 = n_times(23)
# puts p1.call(3) 
# puts p1.call(4) 
# p2 = n_times("Hello ")
# puts p2.call(3)

# proc1 = -> arg { puts "In proc1 with #{arg}" }
# proc2 = -> arg1, arg2 { puts "In proc2 with #{arg1} and #{arg2}" }
# proc3 = ->(arg1, arg2) { puts "In proc3 with #{arg1} and #{arg2}" }

# proc1.call "ant"
# proc2.call "bee", "cat"
# proc3.call "dog", "elk"
# proc1.call "jujuba"


# def my_if(condition, small, big)
#   if condition
#     small.call
#   else
#     big.call
#   end
# end

# 5.times do |val|
#   my_if val < 3,
#   -> { puts "#{val} is small" },
#   -> { puts "#{val} is big" }
# end

def my_while(cond, &body)
  while cond.call
    body.call
  end
end

a = 0

my_while -> { a < 5 } do
  puts a
  a += 1
end