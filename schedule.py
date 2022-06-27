from z3 import Int, And, Distinct, Solver, If, print_matrix, sat

X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(5) ] 
      for i in range(9) ]

# each cell contains a value in {1, ..., 9}
cells_c  = [ And(0 <= X[i][j], X[i][j] <= 10) 
             for i in range(9) for j in range(5) ]

# Lunch time constraint
lunch_c = [X[4][j] == 1 for j in range(5)]

schedule_c = cells_c + lunch_c

instance = ((0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0))

# Initialization (Convert instance to Z3 format)
instance_c = [ If(instance[i][j] == 0, 
                  True, 
                  X[i][j] == instance[i][j]) 
               for i in range(9) for j in range(5) ]

s = Solver()
s.add(schedule_c + instance_c)
if s.check() == sat:
    m = s.model()
    r = [ [ m.evaluate(X[i][j]) for j in range(5) ] 
          for i in range(9) ]
    print_matrix(r)
else:
    print("failed to solve")