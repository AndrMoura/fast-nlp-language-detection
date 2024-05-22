import pycld2

from typing import List, Dict, Union


def _get_multiple_languages(text: str) -> List[str]:
    pycld2.detect(text)
    _, _, langs = pycld2.detect(text)
    all_langs = set()

    for lang in langs:
        if lang[0] != "Unknown":
            all_langs.add(str.lower(lang[0]))

    return list(all_langs)


def get_task_user_agent_languages(
    llm_input: str, llm_output
) -> Dict[str, Union[int, List[str]]]:

    user_languages = _get_multiple_languages(llm_input)
    agent_languages = _get_multiple_languages(llm_output)

    return {
        "user_languages": user_languages,
        "agent_languages": agent_languages,
        "user_lang_count": len(user_languages),
        "agent_lang_count": len(agent_languages),
    }
