# exported as schema -> ./policy/schema.py object containing file

schema = {

    "type" : "object",
        
    "properties" : {

        "sid" : {"type" : "string"},
        
        "intent" : {"type" : "string"},
        
        "command": {"type" : "string" },
        
        "target" : {"type" : "string"}
    
},
        "required" : ["sid", "intent", "command", "target"]
    
}