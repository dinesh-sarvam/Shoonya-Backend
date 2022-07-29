import uuid

## Define constants

# Language names to code (Google Translate)
LANG_NAME_TO_CODE_GOOGLE = {
    "English": "en",
    "Assamese": "as",
    "Bhojpuri": "bho",
    "Bengali": "bn",
    "Bodo": "brx",
    "Dogri": "doi",
    "Dhivehi": "dv",
    "Konkani": "gom",
    "Gujarati": "gu",
    "Hindi": "hi",
    "Kannada": "kn",
    "Kashmiri": "ks",
    "Mizo": "lus",
    "Maithili": "mai",
    "Malayalam": "ml",
    "Manipuri": "mni-Mtei",
    "Marathi": "mr",
    "Nepali": "ne",
    "Odia": "or",
    "Punjabi": "pa",
    "Sanskrit": "sa",
    "Santali": "sat",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
}

# Language code to language name GOOGLE TRANSLATE
LANG_CODE_TO_NAME_GOOGLE = {
    "en": "English",
    "as": "Assamese",
    "bho": "Bhojpuri",
    "bn": "Bengali",
    "brx": "Bodo",
    "doi": "Dogri",
    "dv": "Dhivehi",
    "gom": "Konkani",
    "gu": "Gujarati",
    "hi": "Hindi",
    "kn": "Kannada",
    "ks": "Kashmiri",
    "lus": "Mizo",
    "mai": "Maithili",
    "ml": "Malayalam",
    "mni": "Manipuri",
    "mni-Mtei": "Manipuri",
    "mr": "Marathi",
    "ne": "Nepali",
    "or": "Odia",
    "pa": "Punjabi",
    "sa": "Sanskrit",
    "sat": "Santali",
    "sd": "Sindhi",
    "si": "Sinhala",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
}

LANG_CODE_TO_NAME_ULCA = {
    "en": "English",
    "as": "Assamese",
    "bho": "Bhojpuri",
    "bn": "Bengali",
    "brx": "Bodo",
    "doi": "Dogri",
    "dv": "Dhivehi",
    "kok": "Konkani",
    "gu": "Gujarati",
    "hi": "Hindi",
    "kn": "Kannada",
    "ks": "Kashmiri",
    "lus": "Mizo",
    "mai": "Maithili",
    "ml": "Malayalam",
    "mni": "Manipuri",
    "mni-Mtei": "Manipuri",
    "mr": "Marathi",
    "ne": "Nepali",
    "or": "Odia",
    "pa": "Punjabi",
    "sa": "Sanskrit",
    "sat": "Santali",
    "sd": "Sindhi",
    "si": "Sinhala",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
}

LANG_NAME_TO_CODE_ULCA = {
    "English": "en",
    "Assamese": "as",
    "Bhojpuri": "bho",
    "Bengali": "bn",
    "Bodo": "brx",
    "Dogri": "doi",
    "Dhivehi": "dv",
    "Konkani": "kok",
    "Gujarati": "gu",
    "Hindi": "hi",
    "Kannada": "kn",
    "Kashmiri": "ks",
    "Mizo": "lus",
    "Maithili": "mai",
    "Malayalam": "ml",
    "Manipuri": "mni",
    "Marathi": "mr",
    "Nepali": "ne",
    "Odia": "or",
    "Punjabi": "pa",
    "Sanskrit": "sa",
    "Santali": "sat",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
}

LANG_MODEL_CODES = {
    "Hindi-English": 100,
    "Bengali-English": 101,
    "Tamil-English": 102,
    "English-Hindi": 103,
    "English-Tamil": 104,
    "English-Assamese": 110,
    "English-Bengali": 112,
    "English-Gujarati": 114,
    "English-Kannada": 116,
    "English-Malayalam": 118,
    "English-Marathi": 120,
    "English-Odia": 122,
    "English-Punjabi": 124,
    "English-Telugu": 126,
    "Assamese-English": 128,
    "Gujarati-English": 130,
    "Kannada-English": 132,
    "Malayalam-English": 134,
    "Marathi-English": 136,
    "Odia-English": 138,
    "Punjabi-English": 140,
    "Telugu-English": 142,
} # 144 for all the other  indic-indic translations


def hash_upload(instance, filename):
    filename = str(uuid.uuid4())[0:8] + "-" + filename
    return "profile_photos/" + filename
