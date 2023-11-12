def parse_command(text: str, entities : list[str]) -> (str, str, bool):
    entity = ""
    state = ""
    states = ["an", "aus", "on", "off"]
    for s in states:
        if s in text:
            state = s
            break
    for e in entities:
        if e in text:
            entity = e
            break

    found = (entity != "" and state != "")
    return entity, state, found


if __name__ == '__main__':
    entities = ["nachtlicht", "stern"]
    assert parse_command("mach das nachtlicht an", entities) == ("nachtlicht", "an", True)
    assert parse_command("stern aus", entities) == ("stern", "aus", True)
    assert parse_command("stern", entities) == ("stern", "", False)