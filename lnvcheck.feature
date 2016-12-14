Feature: Check LNV configuration 

  Scenario: Check if VNI is in a bridge 
     Given  VNI is configured 
       When VNI is in a bridge?  
       Then is that bridge up?
       Then are there other ports in the bridge?
       Then do I have a route to the remote endpoints?
