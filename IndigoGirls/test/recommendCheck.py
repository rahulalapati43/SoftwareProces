import IndigoGirls.dispatch as dispatch

validJson = '{"op": "recommend", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": "0", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, " ": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {" ": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": "4", "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 0, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 400, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, " ": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": "4", "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 0, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 1000, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, " ": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,"2"]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,-1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 2, "rowCount": 2, "grid": [0,0,1,17]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 2, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 3, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, "grid": [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 1, "board": {"columnCount": 4, "rowCount": 4, "grid": [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 2, "board": {"columnCount": 4, "rowCount": 4, "grid": [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 3, "board": {"columnCount": 4, "rowCount": 4, "grid": [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 2, "board": {"columnCount": 4, "rowCount": 4, "grid": [3,3,3,3,1,1,0,2,0,0,1,0,0,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 12, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "recommend", "moves": 5, "board": {"columnCount": 2, "rowCount": 2, "grid": [1,1,2,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

