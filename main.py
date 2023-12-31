from script.categorizer.CodeforcesCategorizer import CodeforcesCategorizer
from script.categorizer.SolvedacCategorizer import SolvedacCategorizer
from script.categorizer.ProgrammersCategorizer import ProgrammersCategorizer
from script.difficultyconverter.SolvedacDifficultyConverter import SolvedacDifficultyConverter

def main():
    # SolvedacDifficultyConverter().convert()
    # SolvedacCategorizer().categorize()
    # CodeforcesCategorizer().categorize()

    ProgrammersCategorizer().categorize()

if __name__ == '__main__':
    main()
