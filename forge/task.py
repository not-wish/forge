import yaml
import json
from .hasher import hashContent
import subprocess
from .cache import catch
import os

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

def build(taskName: str):

    try:
        with open("task.yaml", "r") as f:
            task = yaml.safe_load(f)["task"]

        if (task["name"] == taskName):
            print(f"Task: {taskName} found!\n")

            curHash = list()
            # calculate input hash
            for i in task["inputs"]:
                curHash.append(hashContent(i))

            flag = False

            if (os.path.exists("cache.json")):
                    # check with cache
                with open("cache.json", "r") as c:
                    jsonData = c.read()

                cache = json.loads(jsonData)
                # skip if matched
                if (cache["input"] == len(curHash) and set(cache["inputHash"]) == set(curHash)):
                    print("\n-----------------\nSkipping command because there has been no changes in any input files\n-----------------\n")
                    
                    if (all(os.path.exists(o) for o in task["outputs"])):
                        flag = True
                    else:
                        print("\n-----------------\nRerunning command because some output files are missing in the directory\n-----------------\n")

            if not flag:
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
    
    except FileNotFoundError:
        print("------------------------------\ntask.yaml is not present in the current directory.\nPlease create a task.yaml file to define your tasks.\n------------------------------\n")