import IndigoGirls.dispatch as dispatch

validJson = '{"op": "swipe", "direction": "left", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]}}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))