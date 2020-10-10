h = { 'dog' => 'canine', 'cat' => 'feline', 'donkey' => 'asinine' }
h.length
h['dog']
h['cow'] = 'bovine'
h[12] = 'dodecine'
h['cat'] = 99
puts h

h = { dog:'canine', cat: 'feline', donkey: 'asinine' }
h.length
print h[:dog], "\n"
h['cow'] = 'bovine'
h[12] = 'dodecine'
h['cat'] = 99
puts h