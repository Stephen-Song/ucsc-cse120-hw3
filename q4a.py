import pyrtl

def datapath(zero, lt, opcode):
    # TODO: implement logic to assign branch below using the specification in Q4.a)
    # For example: branch = zero & lt ~opcode
    branch = ((~opcode[1] & ~opcode[0] & lt) | (~opcode[1] & opcode[0] & ~lt) | (opcode[1] & ~opcode[0] & zero) | (opcode[1] & opcode[0] & ~zero))
    return branch

if __name__ == "__main__":
    zero = pyrtl.Input(1, "zero")
    lt = pyrtl.Input(1, "lt")
    opcode = pyrtl.Input(2, "opcode")

    branch_out = datapath(zero, lt, opcode)

    branch = pyrtl.Output(1, "branch")
    branch <<= branch_out

    sim = pyrtl.Simulation()

    # Example test case below, this should PASS
    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 0})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")
    
    # TODO: write test cases here
    #Opcode = 0
    try:
        sim.step({"zero" : 0, "lt" : 0, "opcode": 0})
        assert sim.inspect("branch") == 0
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 0})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 1, "lt" : 0, "opcode": 0})
        assert sim.inspect("branch") == 0
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 1, "lt" : 1, "opcode": 0})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")
        
    #Opcode = 1
    try:
        sim.step({"zero" : 0, "lt" : 0, "opcode": 1})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 1})
        assert sim.inspect("branch") == 0
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 1, "lt" : 0, "opcode": 1})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 1, "lt" : 1, "opcode": 1})
        assert sim.inspect("branch") == 0
        print("Test PASS")
    except:
        print("Test FAIL")

    #Opcode = 2
    try:
        sim.step({"zero" : 0, "lt" : 0, "opcode": 2})
        assert sim.inspect("branch") == 0
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 2})
        assert sim.inspect("branch") == 0
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 1, "lt" : 0, "opcode": 2})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 1, "lt" : 1, "opcode": 2})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")

    #Opcode = 3
    try:
        sim.step({"zero" : 0, "lt" : 0, "opcode": 3})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 3})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 1, "lt" : 0, "opcode": 3})
        assert sim.inspect("branch") == 0
        print("Test PASS")
    except:
        print("Test FAIL")

    try:
        sim.step({"zero" : 1, "lt" : 1, "opcode": 3})
        assert sim.inspect("branch") == 0
        print("Test PASS")
    except:
        print("Test FAIL")
