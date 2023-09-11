def transform_spaces(txt: str, msg: bytes) -> str:
    bit = 7
    idx = 0
    line_cnt = len(msg) * 8

    res = []
    lines = txt.split("\n")
    for i in range(line_cnt):
        line = lines[i] if i < len(lines) else ""
        if msg[idx] & (1 << bit):
            line += " "
        res.append(line)
        bit -= 1
        if bit == -1:
            bit = 7
            idx += 1
    return "\n".join(res)


def get_spaces(txt: str) -> bytes:
    lines = txt.split("\n")

    byte = 0
    bit = 7
    res = []
    for line in lines:
        if len(line) > 0 and line[-1] == " ":
            byte += 1 << bit
        bit -= 1
        if bit == -1:
            res.append(byte)
            byte = 0
            bit = 7
    return bytes(res)


rus = "КАМОНВЕРХСТорухаес" # 0
eng = "KAMOHBEPXCTopyxaec" # 1


def transform_letters(txt: str, msg: bytes) -> str:
    bit = 7
    idx = 0

    res = []
    for l in txt:
        if idx < len(msg) and (l in eng or l in rus):
            val = msg[idx] & (1 << bit)
            if val == 0 and l in eng:
                l = rus[eng.find(l)]
            elif val == 1 and l in rus:
                l = eng[rus.find(l)]
            bit -= 1
            if bit == -1:
                bit = 7
                idx += 1
        res.append(l)
    return "".join(res)


def get_letters(txt: str) -> bytes:
    byte = 0
    bit = 7
    res = []
    for l in txt:
        if l in eng or l in rus:
            if l in eng:
                byte += 1 << bit 
            bit -= 1
            if bit == -1:
                res.append(byte)
                byte = 0
                bit = 7
    return bytes(res)