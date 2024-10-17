def controller(reference, y_pos, time_step, Kp=0.1, Kd=0.7):
    action = 0
    if time_step != 0: # at time = 0, the error is 0 and there is no previous error so action = 0
        prev_error = reference[time_step - 1] - y_pos[time_step - 1]
        current_error = reference[time_step] - y_pos[time_step]
        action = Kp * current_error + Kd * (current_error - prev_error)
    return action
