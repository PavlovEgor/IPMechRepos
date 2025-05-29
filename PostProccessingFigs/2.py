

def get_calc_real_time_from_log(log_filename):
    log = open(log_filename, "r")
    calc_Time = []
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

def get_calc_real_time_from_log_mpi(log_filename, np):
    log = open(log_filename, "r")
    calc_Time = []
    real_Time = []
    flag1 = 0
    A = log.readlines()

    for i, line in enumerate(A):
        if line[:7] == "Time = ":
            if flag1 == 0:
                calc_time = float(line[7:-1])
                calc_Time.append(calc_time)

                real_line = A[i+4]
                real_time_str = ''
                for s in real_line[16:]:
                    if s == 's':
                        real_time_str = real_time_str[:-1]
                        real_Time.append(float(real_time_str))
                        break
                    else:
                        real_time_str += s

            flag1 += 1
            flag1 = flag1 % np



    return (real_Time, calc_Time[:-3])

import matplotlib.pyplot as plt

plt.plot(*get_calc_real_time_from_log("log.reactingCTDyMFoam"))
plt.plot(*get_calc_real_time_from_log_mpi("log.mpirun", 6))
plt.xlabel("real")
plt.ylabel("calc")
plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

ax.plot(*get_calc_real_time_from_log("log.reactingCTDyMFoam"), label="1 ядро")
ax.plot(*get_calc_real_time_from_log_mpi("log.mpirun", 6), label="6 ядер")

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel("Расчетное время")
ax.set_ylabel("Реальное время")
ax.set_title("Зависимость расчетного времени от реального \n для расчета с 0.5 млн. элементов")
plt.legend()
plt.show()
