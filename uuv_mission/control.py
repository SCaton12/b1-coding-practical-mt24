def controller(Kp, Kd, reference, y_pos, time_step):
    action = 0
    if time_step != 0:
        current_error = reference[time_step] - y_pos[time_step]
        prev_error = reference[time_step - 1] - y_pos[time_step - 1]
        action = Kp * current_error + Kd * (current_error - prev_error)
    return action





