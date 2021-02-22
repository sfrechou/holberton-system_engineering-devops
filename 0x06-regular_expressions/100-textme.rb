#!/usr/bin/env ruby
$stdout.sync = true
puts ARGV[0].scan(/.*\[from:(\+*.*)\].*\[to:(\+*\d+)\].*\[flags:(.*?)\]/).join(",")
