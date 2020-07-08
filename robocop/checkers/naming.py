from robot.parsing.model.statements import Documentation, Comment
from robocop.checkers import BaseChecker


MSGS = {
    "W0301": (
        "invalid-char-in-name",
        "Invalid character %s in %s name"
    )
}


def register(linter):
    linter.register_checker(InvalidCharactersInNameChecker(linter))


class InvalidCharactersInNameChecker(BaseChecker):
    def __init__(self, *args):
        self.invalid_chars = ('.', '?')
        self.node_names_map = {
            'KEYWORD_NAME': 'keyword',
            'TESTCASE_NAME': 'test case'
        }
        super().__init__(*args)
    
    def check_if_char_in_name(self, node, name_of_node):
        # if self.is_disabled(node, "invalid-char-in-name"):
        #     return
        for index, char in enumerate(node.name):
            if char in self.invalid_chars:
                print(node.col_offset)
                print(node.end_col_offset)
                self.report(MSGS, "invalid-char-in-name", node, char, self.node_names_map[name_of_node],
                            col=node.col_offset + index + 1)

    def visit_TestCaseName(self, node):
        self.check_if_char_in_name(node, 'TESTCASE_NAME')
        
    def visit_KeywordName(self, node):
        self.check_if_char_in_name(node, 'KEYWORD_NAME')