import ttg

exp='(B AND C AND E) OR (C AND NOT D AND E) OR (NOT A AND NOT B AND NOT C AND NOT E) OR (NOT B AND NOT C AND D AND NOT E) OR (B AND NOT C AND NOT D AND NOT E)'

toLowerExp = lambda s: s.lower() if s in ["AND","OR","NOT","(NOT"] else s
exp=" ".join([toLowerExp(i) for i in exp.split(" ")])

table=ttg.Truths(['A','B','C','D','E'])
tableSOP=ttg.Truths(['A','B','C','D','E'], [table.SOP([0,2,5,8,13,15,18,21,24,29,31])])
print("SOP")
print(tableSOP.as_prettytable())

tableMin=ttg.Truths(['A','B','C','D','E'], [exp])
print("MIN")
print(tableMin.as_prettytable())

toUpperExp = lambda s: s.upper() if s in ["and","or","not","(not"] else s
outExp = table.SOP([0,2,5,8,13,15,18,21,24,29,31])
outExp = " ".join([toUpperExp(i) for i in outExp.split(" ")])
outExp = outExp.replace("~", "NOT ")
print(outExp)
