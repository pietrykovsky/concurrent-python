import os
from time import sleep


def sleeping(seconds: int):
    """
    Help function to visualise process status.
    """
    for second in range(1, seconds + 1):
        print(f"[{os.getpid()}] Process is sleeping... ({second})")
        sleep(1)


def child_process():
    """
    Create a child process and then replace it with exec()
    """
    pid = os.fork()

    # The child process
    if pid == 0:
        print(f"I am the child process with PID {os.getpid()}")
        os.execvp(
            "ls", ["ls", "-l"]
        )  # Replacing the child process code with "ls -l" command

    # The parent process
    else:
        print(f"I am the parent process with PID {os.getpid()}")
        os.wait()  # Waiting for the child process to finish
        print(f"Child process with PID {pid} has finished.")
        print(f"Parent process {os.getpid()} has finished.")


def zombie_process():
    """
    Create a zombie process by terminating the child process and not checking the status with wait()
    """
    pid = os.fork()
    if pid == 0:
        os._exit(0)  # Terminating the child process
    else:
        print(f"Creating a zombie process with PID {pid}")


def process_tree(children: int):
    """
    Create n number of children processes.

    :param children: Number of children processes
    """
    # Creating a process tree
    if children > 0:
        pid = os.fork()
        if pid == 0:
            print(f"I am a child process with PID {os.getpid()}.")
            sleeping(seconds=3)
            os._exit(0)  # Terminating the child process
        else:
            print(f"I am the parent process with PID {os.getpid()}.")
            process_tree(children=children - 1)
            os.wait()
            print(f"Child process with PID {pid} has finished.")


if __name__ == "__main__":
    child_process()
    process_tree(children=3)  # create a process tree with 3 children
    zombie_process()
