import IndigoGirls.dispatch as dispatch

validJson = '{"op": "initializeGame"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = ''
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = 42
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

errorJson = '{"op": "unknown"}'
errorResult = dispatch.dispatch(errorJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n\n").format(errorJson, errorResult))

validJson = '{"op": "initializeGame", "rowCount": 2}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": 2, "columnCount": 2}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": "two"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "columnCount": "9"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "columnCount": 101}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": 100}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": 100, "columnCount":100}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))