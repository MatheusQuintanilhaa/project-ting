import re


def get_object(need_content, i, line):
    if need_content:
        return {"linha": i + 1, "conteudo": line}
    else:
        return {"linha": i + 1}


def get_match_data(word, instance, need_content):
    result = []
    word_lower = word.lower()
    for file in instance._data:
        lines = [
            get_object(need_content, i, line)
            for i, line in enumerate(file["linhas_do_arquivo"])
            if re.search(word_lower, line.lower())
        ]
        if lines:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines
            })
    return result


def exists_word(word, instance):
    return get_match_data(word, instance, need_content=False)


def search_by_word(word, instance):
    return get_match_data(word, instance, need_content=True)
