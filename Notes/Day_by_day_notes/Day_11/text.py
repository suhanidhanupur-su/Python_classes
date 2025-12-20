Day: 11


language = "Programming"


Positive Indexing:-

0 1 2 3 4 5 6 7 8 9 10
P r o g r a m m i n g

Negative  Indexing:-
  P     r      o    g     r    a    m    m    i    n     g
-11  -10   -9   -8   -7   -6   -5    -4   -3   -2    -1

String slicing:-
=> Cake : String  ( Big part)
=> one slice of Cake  : Substring  ( small Part)

Note:-
=> Slice : Two Parameters, Three parameters
=> ending points will always be excluded.
=> By default the starting point will be 0.
=> by default the ending point will be the last index.

Two parameters:
=> first parameter is starting point
=> The second parameter is the ending point.


print(language[0:8]) 
=> 0 => starting point
=> 8 => ending point (excluded)




0 1 2 3 4 5 6 7 8 9 10
P r o g r a m m i n g

language = "Programming"
print(language[2:9])


OUTPUT:-   ogrammi

starting point => 2
ending point => 9 (excluded)

print(language[0: ]) 
starting point = 0
ending point => last index 


print(language[ : ])
starting point => 0
ending point => last index 


print(language[ 4: -1])
starting point => 4
ending point => -1 OR 10 (excluded)


0 1 2 3 4 5 6 7 8 9 10
P r o g r a m m i n g

  P       r     o     g      r     a     m    m     i      n      g
-11    -10  -9    -8    -7    -6    -5    -4    -3    -2     -1

print(language[-8: ])
starting point => -8
ending point => last index

Slicing: Three parameters
=> first paraemeter => starting point
=> second parameter => ending point
=> third parameter => Gap (N-1)
=> By default gap = 1

#-----------------------------------------------

starting point => 0
ending point => 9
gap = 2 , N-1 => 2-1 => 1 , GAP = 1
