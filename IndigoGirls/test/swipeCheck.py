import IndigoGirls.dispatch as dispatch

validJson = '{"op": "swipe", "direction": "LEFT", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "left", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "left", "board": {"columnCount": 4, "rowCount": 4, "grid": [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "RiGhT", "board": {"columnCount": 2, "rowCount": 2, "grid": [1, 1, 2, 2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,1,0,1,0,2,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [3,3,3,3,1,1,0,2,0,0,1,0,0,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "uP", "board": {"columnCount": 2, "rowCount": 2, "grid": [1, 1, 2, 2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "Up", "board": {"columnCount": 4, "rowCount": 4, "grid": [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "up", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "UP", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "up", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,1,0,1,0,2,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "up", "board": {"columnCount": 4, "rowCount": 4, "grid": [3,3,3,3,1,1,0,2,0,0,1,0,0,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "up", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "Down", "board": {"columnCount": 2, "rowCount": 2, "grid": [1, 1, 2, 2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "dOwn", "board": {"columnCount": 4, "rowCount": 4, "grid": [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "doWn", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "doWN", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "down", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,1,0,1,0,2,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "DOWN", "board": {"columnCount": 4, "rowCount": 4, "grid": [3,3,3,3,1,1,0,2,0,0,1,0,0,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "down", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "down", "board": {"columnCount": 4, "rowCount": 5, "grid": [0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "left", "board": {"columnCount": 5, "rowCount": 4, "grid": [1,1,2,2,3,2,2,3,3,1,3,3,4,4,2,4,4,5,5,3]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "up", "board": {"columnCount": 5, "rowCount": 6, "grid": [1,0,0,0,4,1,0,0,0,4,2,0,0,0,5,2,0,0,0,5,3,0,0,0,6,3,0,0,0,6]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "out", "board": {"columnCount": 4, "rowCount": 4, "grid": [3,3,3,3,1,1,0,2,0,0,1,0,0,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "board": {"columnCount": 4, "rowCount": 4, "grid": [3,3,3,3,1,1,0,2,0,0,1,0,0,0,0,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [1,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"rowCount": 4, "grid": [1,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": "4", "rowCount": 4, "grid": [1,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 1, "rowCount": 4, "grid": [1,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "grid": [1,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": "4", "grid": [1,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 101, "grid": [1,2]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 4}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 2, "rowCount": 2, "grid": [-1,2,3,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "right", "board": {"columnCount": 2, "rowCount": 2, "grid": [0,0,0,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "swipe", "direction": "up", "board": {"columnCount": 2, "rowCount": 2, "grid": [3,4,2,1]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))
