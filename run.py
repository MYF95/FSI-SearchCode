# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
lh = search.GPSProblem('L', 'H', search.romania)
no = search.GPSProblem('N', 'O', search.romania)
gz = search.GPSProblem('G', 'Z', search.romania)
ca = search.GPSProblem('C', 'A', search.romania)


print search.sinHeuristica(ab).path()
print search.conHeuristica(ab).path()

print "--------------------------------------------"

print search.sinHeuristica(lh).path()
print search.conHeuristica(lh).path()

print "--------------------------------------------"

print search.sinHeuristica(no).path()
print search.conHeuristica(no).path()

print "--------------------------------------------"

print search.sinHeuristica(gz).path()
print search.conHeuristica(gz).path()

print "--------------------------------------------"

print search.sinHeuristica(ca).path()
print search.conHeuristica(ca).path()

