from .cmd import run_shell_command

def get_git_diff():
    command = "git diff"
    return run_shell_command(command)
