#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([A-Za-z]+|\+?\d{11})\] \[to:(\+?\d{11}|[A-za-z]+)\] \[flags:([\W+\d]+\])/).join(',')
puts "\n"
puts "\n"
