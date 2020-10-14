require_relative 'csv_reader'


reader = CsvReader.new

ARGV.each do |file_name|
  STDERR.puts "Processing  #{file_name}"
  reader.read_in_csv_data(file_name)
end

puts "Total value = #{reader.total_value_in_stock}"