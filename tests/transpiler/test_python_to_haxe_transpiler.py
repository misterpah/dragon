from dragon.transpiler.python_to_haxe_transpiler import PythonToHaxeTranspiler
from dragon.transpiler import python_to_haxe_transpiler
import os
import unittest

class TestTemplateCreator(unittest.TestCase):
    def test_add_package_statement_adds_empty_statement_for_root_file(self):
        # Linux style path
        code = python_to_haxe_transpiler._add_package_statement("/tmp", "/tmp/main.hx", "", "/")
        self.assertIn("package ;", code)

    def test_add_package_statement_adds_single_package(self):
        # Windows style path
        code = python_to_haxe_transpiler._add_package_statement("C:\\project",
            "C:\\project\\models\\player.py", "", "\\")
        self.assertIn("package models;", code)

    def test_add_package_statement_adds_multiple_nested_packages(self):
        root = os.path.join("projects", "haxe", "samurai", "code")
        filename = os.path.join(root, "common", "models", "entities", "player.py")
        code = python_to_haxe_transpiler._add_package_statement(root, filename, "")
        self.assertIn("package common.models.entities", code)