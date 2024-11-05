import sys
import subprocess
import os

# params_iter_speed = [[1,1],[1,2],[1,5]]
params_iter_speed = [["1", "1"], ["1", "2"], ["1", "5"]]  # Use lists of strings
net_types = ["spinn"]  # ["pfnn", "spinn"]
available_time = 2 * 60
n_iter = int(1e8)
num_runs = 1
log_every = 50000

dir_path = os.path.dirname(os.path.realpath(__file__))
exec_path = os.path.join(dir_path, "pinn_inverse.py")
for params in params_iter_speed:
    for net_type in net_types:
        for run in range(num_runs):
            try:
                print(f"Running with params_scale={params}, net_type={net_type}, run={run}")
                # Flatten the params list to be passed as separate arguments
                subprocess.check_call(
                    [sys.executable, exec_path] +
                    [f"--params_iter_speed"] + params +  # Pass params as separate arguments
                    [f"--net_type={net_type}",
                     f"--n_iter={n_iter}",
                     f"--log_every={log_every}",
                     f"--available_time={available_time}"]
                )
            except subprocess.CalledProcessError as e:
                print(f"Run with params={params}, net_type={net_type}, run={run} failed")
                print(e)
                sys.exit(1)

