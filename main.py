from script.categorizer.CodeforcesCategorizer import CodeforcesCategorizer
from script.categorizer.SolvedacCategorizer import SolvedacCategorizer
from script.difficultyconverter.SolvedacDifficultyConverter import SolvedacDifficultyConverter


def main():
    # SolvedacDifficultyConverter().convert()
    # SolvedacCategorizer().categorize()
    CodeforcesCategorizer().categorize()

if __name__ == '__main__':
    main()
