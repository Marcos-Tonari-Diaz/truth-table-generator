import ttg
import numpy as np

#exp = '((-A) and (-D)) or (B and (-D)) or (E and B and C) or (E and C and (-D)) or ((-E) and (-B) and (-C) and D)'
exp = '(B and C and E) or (C and (-D) and E) or ((-A) and (-B) and (-C) and (-E)) or ((-B) and (-C) and D and (-E)) or (B and (-C) and (-D) and (-E))'
table = ttg.Truths(['A','B','C','D','E'], [exp])
print(table.as_prettytable())
print(np.array(table.as_pandas_minterms()[exp].tolist())*list(range(len(table.as_pandas_minterms()))))

#printTrue =  lambda l: print([l.index(i) for i in l if i==1])
#printTrue(table.as_pandas()[exp].tolist())
