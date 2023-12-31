import sys
import shutil


def get_terminal_width():
    """
    Get current terminal size to get the right display size

    Returns:
        columns(int): number of columns
    """
    terminal_size = shutil.get_terminal_size()
    return terminal_size.columns


def ft_tqdm(iterable):
    """
    Reproduce tqdm(): make a loop shows a smart progress meter

    Args:
        iterable(range): range object to loop in

    """
    columns = get_terminal_width()
    total = len(iterable)
    len_total = len(str(total))
    loading_display = 36 + (len_total * 2 - 1)

    for i, item in enumerate(iterable, 1):
        yield item
        if total is None:
            continue
        percent = int(100 * (i / total))
        bar_length = int((columns - loading_display) * percent / 100)
        bar = "=" * bar_length + ">" + " " \
            * ((columns - loading_display) - bar_length)
        sys.stdout.write(f"\r{percent}%|{bar}| {i}/{total}")
        sys.stdout.flush()
