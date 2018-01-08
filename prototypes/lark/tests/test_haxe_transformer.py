from haxe_transformer import HaxeTransformer
from lark.lexer import Token
from lark import Tree
import unittest

class TestHaxeTransformer(unittest.TestCase):
    def test_import_stmt_transforms_simple_imports(self):
        h = HaxeTransformer()
        # TODO: sample should be "from play_state import PlayState"
        node = [Tree("import_name", [Tree("dotted_as_names", [Tree("dotted_as_name", [Tree("dotted_name", [Token("NAME", 'PlayState')])])])])]
        output = h.import_stmt(node)
        self.assertEqual("import PlayState", output)

    def test_import_stmt_transforms_dot_path_imports(self):
        h = HaxeTransformer()
        node = [Tree("dotted_name", [Token("NAME", 'openfl'), Token("NAME", 'display')]), Tree("import_as_names", [Tree("import_as_name", [Token("NAME", 'Sprite')])])]
        #output = h.import_stmt(node)
        #self.assertEqual("import openfl.display.Sprite", output)
        