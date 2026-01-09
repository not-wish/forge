import datetime
import json

def catch(taskName: str, input: int, output: int, inputHash: list[str], outputHash: list[str]):

    data = {
        "name": taskName,
        "input": input,
        "output": output,
        "inputHash": inputHash,
        "outputHash": outputHash,
        "timestamp": str(datetime.datetime.now)
    }

    with open("cache.json", "w") as f:
        json.dump(data, f)
        # f.write(content)

        