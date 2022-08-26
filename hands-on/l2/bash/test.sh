#!/bin/csh -f
set s = 1
while ( "$s" <= 5)

set j = 1
while ( "$j" <= 5)
set pt = `expr 1000 \* $s `
echo "$pt"

@ j = $j + 1
end
@ s = $s + 1
end


