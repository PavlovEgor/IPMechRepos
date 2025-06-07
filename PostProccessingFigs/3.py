
def get_calc_real_time_from_log(log_filename):
    log = open(log_filename, "r")
    calc_Time_chem = []
    calc_Time_hidr = []
    real_Time = []
    flag = 0

    for line in log.readlines():
        if line[:7] == "Time = ":
            calc_time = float(line[7:-1])
            calc_Time.append(calc_time)

        if line[:16] == "ExecutionTime = ":
            if (flag == 0):
                real_time_str = ''
                for s in line[16:]:
                    if s == 's':
                        real_time_str = real_time_str[:-1]
                        real_Time.append(float(real_time_str))
                        break
                    else:
                        real_time_str += s

            flag += 1
            flag = flag % 5

    return (real_Time, calc_Time)