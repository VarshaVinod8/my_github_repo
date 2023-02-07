import os
turn = &#39; X &#39;
win = False
spaces = 9
def draw ( board ):
for i in range ( 6 , - 1 , - 3 ):
print (&#39; &#39; + board [ i ] + &#39; | &#39; +
board [ i + 1 ] + &#39; | &#39; + board [ i + 2 ])

def takeinput ( board , spaces , turn ):
pos = - 1
print ( turn + &quot; &#39;s turn: &quot;)
while pos == - 1 :
try :
print (&quot; Pick position 1-9: &quot;)
pos = int ( input ())
if ( pos &lt; 1 or pos &gt; 9 ):
pos = - 1
elif board [ pos - 1 ] != &#39; &#39;:
pos = - 1

except :
print (&quot; enter a valid position &quot;)

spaces -= 1
board [ pos - 1 ] = turn
if turn == &#39; X &#39;:
turn = &#39; O &#39;
else :
turn = &#39; X &#39;
return board , spaces , turn
def checkwin ( board ):
# could probably make this better
for i in range ( 0 , 3 ):
# rows
r = i * 3
if board [ r ] != &#39; &#39;: