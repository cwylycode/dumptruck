# A man walks into a bar - "Ouch."
import time


def render_loading_bar(percentage: float, num_of_dots: int, dot_symbol: str = '*', empty_dot_symbol: str = ' '):
    """
    Print out a loading bar to console at a specific percentage with character symbols
    Percentage value should be between 0.0 - 1.0
    Number of dots is the max count of dots in the loading bar when at 100%
    The dot symbol should just be a single character since multiple/large characters will 'extend' the loading bar when updated with an increased percent
    """

    if percentage < 0:
        percentage = 0
    if percentage > 1:
        percentage = 1

    dot_count = round(percentage * num_of_dots)
    dots = (dot_symbol+' ') * dot_count
    empty_dots = (empty_dot_symbol+' ')*(num_of_dots-dot_count)
    print(f"| {dots + empty_dots}|")


if __name__ == "__main__":
    import platform
    import os

    p = platform.system()

    def clear_screen():
        if p == "Windows":
            os.system("cls")  # Clear screen for Windows
        elif p == "Darwin":
            print("\033\143")  # Clear screen and scrollback for macOS
        else:
            os.system("clear")  # Clear screen for Linux/Others

    percent = 0
    while percent < 1:
        clear_screen()
        percent += 0.1
        if percent > 1:
            percent = 1
        render_loading_bar(percent, 10, ">", "-")
        time.sleep(1)
