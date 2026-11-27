
# Practical 9: Blocks World using STRIPS Planning

# Initial State
initial_state = {
    ("ON", "A", "B"),
    ("ON", "B", "C"),
    ("ONTABLE", "C"),
    ("CLEAR", "A"),
    ("ARMEMPTY",)
}

# Goal State
goal_state = {
    ("ON", "C", "A"),
    ("ON", "A", "B"),
    ("ONTABLE", "B"),
    ("CLEAR", "C"),
    ("ARMEMPTY",)
}

# STRIPS Action: PICKUP
def pickup(block, state):

    if ("ONTABLE", block) in state and \
       ("CLEAR", block) in state and \
       ("ARMEMPTY",) in state:

        state.remove(("ONTABLE", block))
        state.remove(("CLEAR", block))
        state.remove(("ARMEMPTY",))

        state.add(("HOLDING", block))

        print("PICKUP", block)
        return True

    return False


# STRIPS Action: PUTDOWN
def putdown(block, state):

    if ("HOLDING", block) in state:

        state.remove(("HOLDING", block))

        state.add(("ONTABLE", block))
        state.add(("CLEAR", block))
        state.add(("ARMEMPTY",))

        print("PUTDOWN", block)
        return True

    return False


# STRIPS Action: UNSTACK
def unstack(block, below, state):

    if ("ON", block, below) in state and \
       ("CLEAR", block) in state and \
       ("ARMEMPTY",) in state:

        state.remove(("ON", block, below))
        state.remove(("CLEAR", block))
        state.remove(("ARMEMPTY",))

        state.add(("HOLDING", block))
        state.add(("CLEAR", below))

        print("UNSTACK", block, "from", below)
        return True

    return False


# STRIPS Action: STACK
def stack(block, below, state):

    if ("HOLDING", block) in state and \
       ("CLEAR", below) in state:

        state.remove(("HOLDING", block))
        state.remove(("CLEAR", below))

        state.add(("ON", block, below))
        state.add(("CLEAR", block))
        state.add(("ARMEMPTY",))

        print("STACK", block, "on", below)
        return True

    return False


# Execute the planning sequence
state = initial_state.copy()

print("Initial State:")
print(state)

print("\nPlanning Actions:")

unstack("A", "B", state)
putdown("A", state)

unstack("B", "C", state)
putdown("B", state)

pickup("A", state)
stack("A", "B", state)

pickup("C", state)
stack("C", "A", state)

print("\nFinal State:")
print(state)

# Check Goal
if goal_state.issubset(state):
    print("\nGoal Achieved Successfully!")
else:
    print("\nGoal Not Achieved!")
