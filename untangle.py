

def untangle(s,x,y):
    x_matches = []
    y_matches = []


    for s_index, s_char in enumerate(s):
        current_x_match = []
        current_y_match = []
        in_x = False
        in_y = False
        if(s_char == x[0]):
            in_x = True
            



    return (x_matches, y_matches)



if __name__ == "__main__":
        s = "100010101"
        x = "101"
        y = "0"
        # indexing starting at 1
        x_reps = [[1,2,5], [7,8,9]]
        y_reps = [[3],[4],[6]]

        x_matches, y_matches = untangle(s, x, y)

        print()
        print(f"s: {s}")
        print(f"x: {x}")
        print(f"y: {y}")
        print(f"x matches:\nExpected: {x_reps}\nActual: {x_matches}\n")
        print(f"y matches:\nExpected: {y_reps}\nActual: {y_matches}\n")