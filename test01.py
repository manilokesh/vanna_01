import runpod


def is_even(job):   

    resultjson = { "result":False, "error":""}

    job_input = job["input"]
    the_number = job_input["number"]

    if not isinstance(the_number, int): 
        resultjson["error"] = f'{the_number} is not an Integer'
    else:
        if the_number % 2 == 0:
            resultjson["result"] = True
    
    return resultjson 

runpod.serverless.start({"handler": is_even})