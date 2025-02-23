# 조사와 구두점 목록
STOP_WORDS = set([
    "강의",
    "내용",
    "요약",
    "키워드",
    "설명",  # 불용어
])

JOSA = set([
    "이",
    "가",
    "은",
    "는",
    "을",
    "를",
    "의",
    "에",
    "와",
    "과",
    "도",
    "로",
    "으로",
    "에서",
    "부터",
    "까지",
    "같이",
    "처럼",
    "다",
    "다른",
    "이런",
    "저런",
    "그런",  # 조사
])

PUNCTUATION = set([
    "!",
    "?",
    ".",
    ",",
    ":",
    ";",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "'",
    '"',
    "“",
    "”",
    "‘",
    "’",  # 구두점
])

# 복합 명사 목록
COMPOUND_NOUNS = set([
    "다각형",
    "한 변의 길이",
    "자료 모으기",
    "분수",
    "모양 조각",
    "10만",
    "소수",
    "대각선",
    "모양만들기",
    "나눗셈의 의미",
    "대분수",
    "100만",
    "시계방향",
    "나머지가 있는 두자릿수 몫",
    "큰 수",
    "빼기",
    "정사각형",
    "눈금",
    "사다리꼴",
    "각의수",
    "각의 크기",
    "뺄셈",
    "분모",
    "자연수",
    "나눗셈",
    "돌리기",
    "이등변",
    "문제",
    "각도의 차",
    "모양채우기",
    "곱셈",
    "두자릿수 몫",
    "둔각",
    "반시계방향",
    "달력",
    "꺾은선그래프",
    "바둑돌",
    "정다각형",
    "회전",
    "정삼각형",
    "각의크기",
    "마름모",
    "변",
    "변화",
    "변의길이",
    "숫자 배열",
    "연속적변화",
    "평면도형",
    "꼭지점의수",
    "연속된 숫자",
    "연결",
    "실생활 문제",
    "수선",
    "세자릿수와 두자릿수의 곱",
    "억",
    "세로 형식",
    "조",
    "무늬 만들기",
    "평행선 사이의 거리",
    "한눈에 보기",
    "방향",
    "여러 가지 사각형",
    "변의수",
    "변의 길이",
    "여러 가지 사각형의 대각선",
    "운동 횟수",
    "각도",
    "분자",
    "수 비교",
    "사각형",
    "자리값",
    "세자릿수의 곱",
    "수직선",
    "모양 만들기",
    "삼각형",
    "이름",
    "뒤집기",
    "기찻길",
    "덧셈",
    "평행사변형",
    "수직",
    "정육각형",
    "모양 채우기",
    "규칙 찾기",
    "표",
    "크기 비교",
    "계단 모양",
    "평행선",
    "세자릿수와 두자릿수의 나눗셈",
    "소수점",
    "1000만",
    "물 절약",
    "직각",
    "예각",
    "각도의 합",
    "삼각형의 각",
    "옮기기",
    "평행",
    "비교",
    "성질",
    "막대그래프",
    "사각형의 각",
    "큰수",
    "갹도",
    "물절약"
])
