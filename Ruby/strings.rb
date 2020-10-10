Song = Struct.new(:title, :name, :length)
File.open("songdata") do |song_file|
  songs = []
  song_file.each do |line|
    file, length, name, title = line.chomp.split(/\s*\|\s*/)
    name.squeeze!(" ")
    mins, secs = length.scan(/\d+/)
    songs << Song.new(title, name, mins.to_i*60 + secs.to_i)
  end
  puts songs
end

a = (1..10).to_a
print(a, "\n")
puts('a'..'z')
puts(0..."cat".length)

puts (1 +2 +2 -6) === 5       
puts (1..10) === 15      

str = "gato no mato"
str.sub!(/a/, "**")
str.gsub!(/o/, "O")
puts str