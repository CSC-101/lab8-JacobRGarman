def groups_of_3(lst: list[int]) -> list[list[int]]:
    """Group the input list into sublists of three elements each.
    Args:
        lst (list[int]): A list of integers.
    Returns:
        list[list[int]]: A list of sublists, each containing up to three integers.
    """
    return [lst[i:i + 3] for i in range(0, len(lst), 3)]
