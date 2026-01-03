import yaml
import json
from .hasher import hashContent
import subprocess
from .cache import catch

'''
cache data model 

[
 {
   name: "name of the task",
   input: number of inputs,
   output: number of outputs,
   inputHash: ["input hash 1", "input hash 2"],
   outputHash: ["output hash 1", "output hash 2"],
   timestamp: xxxxxxxxxxx
 }
]
'''

def task(taskName: str):

    with open("task.yaml", "r") as f:
        task = yaml.safe_load(f)

    if (task["name"] == taskName):
        print(f"Task: {taskName} found!\n")

        curHash = list()
        # calculate input hash
        for i in task["inputs"]:
            curHash.append(hashContent(i))

        # check with cache
        with open("cache.json", "r") as c:
            jsonData = c.read()

        cache = json.loads(jsonData)[0]
        # skip if matched
        if (cache[input] == len(curHash) and set(cache["inputHash"]) == set(curHash)):
            print("\n-----------------\nSkipping command because there has been no changes in any input files\n-----------------\n")
        else:
        # execute command if not matched
            result = subprocess.run(
                task["command"],
                capture_output=True,
                text=True
            )

            print(f"Output: {result.stdout}")
            print("\n#---------------------------------#\n")
            print(f"Errors: {result.stderr}")

            outputHash = list()

            for i in task["outputs"]:
                outputHash.append(hashContent(i))

            catch(taskName, len(curHash), len(outputHash) , curHash, outputHash)


        # cache the new input   
    else:
        print("Task not found")