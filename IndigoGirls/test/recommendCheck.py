import IndigoGirls.dispatch as dispatch

validJson = '{"op": "recommend", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))


