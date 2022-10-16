def load_candidates():
    """
    Открывает файл 'candidates.json'.
    Загружает данные из файла.
    """
    import os
    import json
    with open(os.path.join('..', 'data', 'candidates.json'),
              encoding='utf-8') as file:
        candidates_list = json.loads(file.read())
        return candidates_list


def get_all():
    """
    Выводит всех кандидатов.
    """
    candidate_names = {}
    candidates_list = load_candidates()
    for person in candidates_list:
        candidate_names[person["id"]] = person["name"]
    return candidate_names


def get_by_id(id):
    """
    Возвращает данные о конкретном кандидате по номеру.
    """
    candidates_list = load_candidates()
    for person in candidates_list:
        if person["id"] == id:
            return person["name"], person["position"], person["picture"], person["skills"]
        else:
            continue


def get_by_name(candidate_name):
    """
    Ищет совпадения по имени кандидата.
    Возвращает тех кандидатов, у которых совпадения есть.
    """
    candidates_by_name = {}
    candidates_list = load_candidates()
    for person in candidates_list:
        if candidate_name.lower() in person["name"].lower():
            candidates_by_name[person["id"]] = person["name"]
    return candidates_by_name


def get_by_skill(skill):
    """
    Ищет совпадения по навыкам у кандидатов.
    Возвращает тех кандидатов, у которых совпадения есть.
    """
    candidates_by_skills = {}
    candidates_list = load_candidates()
    for person in candidates_list:
        if skill.lower() in person["skills"].lower():
            candidates_by_skills[person["id"]] = person["name"]
    return candidates_by_skills
