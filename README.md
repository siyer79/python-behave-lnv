# python-behave-lnv

This behave-python script can be used to check if the LNV configuration is set up correctly.

<b>Scenario 1 checks the following:  Check if VNI is in a bridge</b>


1)  VNI is configured (checks the /etc/network/interfaces file for VNI's specified
2)  Are the VNI(s) specified in the interfaces file also in a bridge?
3)  Is that bridge up?
4)  Are there other ports in that bridge?
5)  Do I have a route to the remote endpoints?

