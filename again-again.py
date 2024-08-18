# 접두사, 접미사 포함되는지 확인하기
sentence = "powerdog"
is_prefix = "pow"
is_suffix = "dog"

result_prefix = sentence.startswith(is_prefix)
print(result_prefix)

result_suffix = sentence.endswith(is_suffix)
print(result_suffix)