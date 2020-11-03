def filter_by_key(elements, key, threshold):

    """
    Функция для фильтрации сообщений по определённому критерию.
    :param elements: итерируемая последовательность (словарь), в которой осуществляется фильтрация.
    :param key: ключ, по которому осуществляется фильтрация.
    :param threshold: порог, по которому осуществляется фильтрация.
    :return: возвращает отфильтрованную полсдеовательность.
    """

    filtered_elements = []
    for element in elements:
        if element[key] > threshold:
            filtered_elements.append(element)
    return filtered_elements