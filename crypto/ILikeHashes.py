import hashlib
import string

# alfabeto comune per flag CTF
ALPHABET = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    "{}_-" +
    "!@#$%^&*()[]<>.,:;?/\\|+=~'\""
)

rev = {hashlib.sha256(ch.encode("utf-8")).hexdigest(): ch for ch in ALPHABET}

decoded = []
unknown_hashes = set()

with open("./crypto/hash_values.txt", "r", encoding="utf-8") as f:
    for line in f:
        h = line.strip().lower()
        if not h:
            continue
        ch = rev.get(h)
        if ch is None:
            decoded.append("?")
            unknown_hashes.add(h)
        else:
            decoded.append(ch)

print("FLAG?:", "".join(decoded))
print("Unknown hashes:", len(unknown_hashes))
if unknown_hashes:
    print("\nLista unknown:")
    for h in sorted(unknown_hashes):
        print(h)