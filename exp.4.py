
def monkey_banana_problem():
    # Initial State
    state = {
        "monkey": "A",
        "box": "B",
        "monkey_on_box": False,
        "has_banana": False
    }

    print("Initial State:", state)
    if state["monkey"] != state["box"]:
        print("Monkey moves from", state["monkey"], "to", state["box"])
        state["monkey"] = state["box"]
    print("Monkey pushes box to Banana location (C)")
    state["box"] = "C"
    state["monkey"] = "C"
    if not state["monkey_on_box"]:
        print("Monkey climbs onto the box")
        state["monkey_on_box"] = True
    if state["monkey_on_box"] and state["box"] == "C":
        print("Monkey grabs the banana!")
        state["has_banana"] = True

    print("Final State:", state)
monkey_banana_problem()
