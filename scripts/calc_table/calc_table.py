# PR Close 이벤트가 발생하였을 때, 
# 최근에 발생된 PR 정보를 가져와 데이터를 갱신합니다.
# 그리고 current_score.txt 에 데이터를 저장함으로 써, 
# 데이터 무결성과 조작되지 않았음을 검증합니다.

# 그리고 마지막으로, README.txt 에 ASCII ART 를 통해 마무리 합니다.

import pyfiglet
from jinja2 import Template
import argparse

## 점수를 생성합니다.
# 기본적으로 left pad 를 적용하여, 최소 2글자로 표현되도록 만들었습니다.
def generate_score(score: int) -> str:
    art = pyfiglet.figlet_format(str(score).rjust(2, '0'), font="3d-ascii").rstrip("\r\n ")
    return art

## 이름을 생성합니다.
def generate_name(name: str) -> str:
    art = pyfiglet.figlet_format(name, font="doom").rstrip("\r\n ")
    return art
    
def get_current_information(file: str):
    with open(file, 'r') as reader:
        score = list(map(lambda x: int(x), reader.readline().split(",")))
        assert(len(score) == 2)
        winner = "Draw"
        
        if score[0] < score[1]:
            winner = 'Piorosen'
        elif score[0] > score[1]:
            winner = 'oMFDOo'

        return {"mfdo": score[0], "piorosen": score[1], "win": winner}

def generate_score_table(template: str, score) -> str:
    with open(template) as f:
        template = Template(f.read())

    result = template.render({
        'win_name': generate_name(score['win']),
        'mfdo': generate_name("oMFDOo"),
        'mfdo_score':  generate_score(score['mfdo']),
        'piorosen': generate_name("Piorosen"),
        'piorosen_score': generate_score(score['piorosen']),
    })

    return result

def main(score_file: str, template: str, output: str):
    score = get_current_information(score_file)
    result = generate_score_table(template, score)
    with open(output, "wt+") as file:
        file.write(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Score Table for Competition')

    parser.add_argument("--score_file", type=str, default='../current_score.txt')
    parser.add_argument("--template", type=str, default='../../resources/template_score.md')
    parser.add_argument("--output", type=str, default='../../README.md')

    args = parser.parse_args()

    main(args.score_file, args.template, args.output)

## 폰트 목록과 테스트를 위한 코드
# for i in pyfiglet.FigletFont.getFonts():
#     try:
#         print(i)
#         ASCII_art_1 = pyfiglet.figlet_format('oMFDOo Piorosen',font=i)
#         print(ASCII_art_1)
#         print()
#     except:
#         print(i)

