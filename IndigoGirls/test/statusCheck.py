import IndigoGirls.dispatch as dispatch

validJson = '{"op": "status", "tile": 2048, " ": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {" ": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": "4", "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 0, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 1000, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, " ": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": "4", "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": -1, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": 101, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": "2048", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 65537, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": 4, " ": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0.5]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,-1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 16, "board": {"columnCount": 2, "rowCount": 2, "grid": [0,0,0,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,11,0,0,0,1,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,11,0,0,0,1,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 2048, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,10,0,0,0,1,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status",  "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,10,0,0,0,1,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "tile": 16,  "board": {"columnCount": 2, "rowCount": 2, "grid": [1,2,3,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "status", "board": {"columnCount": 4, "rowCount": 4, "grid": [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))