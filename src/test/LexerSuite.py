import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    # Test Identifiers
    def test_lower_identifier(self):
        """Test lowercase identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_upper_identifier(self):
        """Test uppercase identifiers"""
        self.assertTrue(TestLexer.checkLexeme("ABC", "ABC,<EOF>", 102))

    def test_mixed_identifier(self):
        """Test mixed-case identifiers"""
        self.assertTrue(TestLexer.checkLexeme("aBcDeF", "aBcDeF,<EOF>", 103))

    def test_identifier_with_underscore(self):
        """Test identifiers with underscore"""
        self.assertTrue(TestLexer.checkLexeme("_my_var", "_my_var,<EOF>", 104))

    def test_identifier_with_numbers(self):
        """Test identifiers with numbers"""
        self.assertTrue(TestLexer.checkLexeme("var123", "var123,<EOF>", 105))

    def test_invalid_identifier(self):
        """Test invalid identifier starting with number"""
        self.assertTrue(TestLexer.checkLexeme("123abc", "123,abc,<EOF>", 106))

    # Test Keywords
    def test_keyword_var(self):
        """Test 'var' keyword"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;", "var,abc,int,;,<EOF>", 107))

    def test_keyword_func(self):
        """Test 'func' keyword"""
        self.assertTrue(TestLexer.checkLexeme("func abc ( ) {}", "func,abc,(,),{,},<EOF>", 108))

    def test_all_keywords(self):
        """Test all MiniGo keywords"""
        input_str = "var const func type if else for return break continue true false nil int float boolean string"
        expected_output = "var,const,func,type,if,else,for,return,break,continue,true,false,nil,int,float,boolean,string,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 109))

    # Test Operators
    def test_operators(self):
        """Test MiniGo operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / % == != < <= > >= && || ! := =", "+,-,*,/,%,==,!=,<,<=,>,>=,&&,||,!,:=,=,<EOF>", 110))

    # Test Separators
    def test_separators(self):
        """Test separators: (), {}, [], , ;"""
        self.assertTrue(TestLexer.checkLexeme("( ) { } [ ] , ;", "(,),{,},[,],,,;,<EOF>", 111))

    # Test Integer Literals
    def test_integer_literals(self):
        """Test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0 42 123456", "0,42,123456,<EOF>", 112))

    def test_invalid_integer_literal(self):
        """Test invalid integer literal with leading zero"""
        self.assertTrue(TestLexer.checkLexeme("0123", "0,123,<EOF>", 113))

    # Test Floating-Point Literals
    def test_floating_point_literals(self):
        """Test floating-point literals"""
        self.assertTrue(TestLexer.checkLexeme("0.5 3.14 10.0e5", "0.5,3.14,10.0e5,<EOF>", 114))

    def test_invalid_floating_point_literal(self):
        """Test invalid floating-point literals"""
        self.assertTrue(TestLexer.checkLexeme("1.", "1.,<EOF>", 115))
        self.assertTrue(TestLexer.checkLexeme(".5", ".,5,<EOF>", 116))
        self.assertTrue(TestLexer.checkLexeme("3.e10", "3.,e10,<EOF>", 117))

    # Test String Literals
    def test_valid_string(self):
        """Test valid string literals"""
        self.assertTrue(TestLexer.checkLexeme('"Hello, World!"', '"Hello, World!",<EOF>', 118))

    def test_string_with_escape_sequencesssssss(self):
        """Test valid string with escape sequences"""
        self.assertTrue(TestLexer.checkLexeme('"This is a test \\n"', '"This is a test \\n",<EOF>', 119))

    def test_unclosed_string(self):
        """Test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme('"Unclosed string', "UnclosedString(Unclosed string)", 120))

    def test_illegal_escape(self):
        """Test illegal escape sequences"""
        self.assertTrue(TestLexer.checkLexeme('"Illegal \\m escape"', "IllegalEscape(Illegal \\m)", 121))

    # Test Comments
    def test_single_line_comments(self):
        """Test single-line comments"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment\nvar x int;", "var,x,int,;,<EOF>", 122))

    def test_multi_line_comment(self):
        """Test multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Comment block */ var y float;", "var,y,float,;,<EOF>", 123))

    def test_nested_comment(self):
        """Test nested multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Outer /* Inner */ Outer End */ var z int;", "var,z,int,;,<EOF>", 124))

    # Test Complex Expressions
    def test_complex_expression(self):
        """Test complex expressions with operators"""
        self.assertTrue(TestLexer.checkLexeme("a + b * (c - d) / e", "a,+,b,*,(,c,-,d,),/,e,<EOF>", 125))

    def test_function_call(self):
        """Test function call with parameters"""
        self.assertTrue(TestLexer.checkLexeme("foo(10, 20, 30)", "foo,(,10,,,20,,,30,),<EOF>", 126))

    def test_array_access(self):
        """Test array access"""
        self.assertTrue(TestLexer.checkLexeme("arr[5] := 100;", "arr,[,5,],:=,100,;,<EOF>", 127))

    # Test Errors
    def test_invalid_character(self):
        """Test invalid character"""
        self.assertTrue(TestLexer.checkLexeme("hello @world", "hello,ErrorToken @", 128))

    def test_invalid_syntax(self):
        """Test invalid syntax"""
        self.assertTrue(TestLexer.checkLexeme("var x 5;", "var,x,5,;,<EOF>", 129))

    def test_invalid_index_access(self):
        """Test invalid index access"""
        self.assertTrue(TestLexer.checkLexeme("arr[] := 10;", "arr,[,],:=,10,;,<EOF>", 130))
    def test_identifier_with_digits(self):
        """Test identifiers with digits"""
        self.assertTrue(TestLexer.checkLexeme("var_1234", "var_1234,<EOF>", 201))

    def test_identifier_with_mixed_case_and_digits(self):
        """Test identifiers with mixed case and digits"""
        self.assertTrue(TestLexer.checkLexeme("VarName_456", "VarName_456,<EOF>", 202))

    def test_reserved_keyword_as_identifier(self):
        """Test using a reserved keyword as an identifier"""
        self.assertTrue(TestLexer.checkLexeme("funcName varFunc", "funcName,varFunc,<EOF>", 203))

    def test_multiple_identifiers(self):
        """Test multiple identifiers in a row"""
        self.assertTrue(TestLexer.checkLexeme("x y z abc_def _ghi", "x,y,z,abc_def,_ghi,<EOF>", 204))

    def test_identifier_with_special_characters(self):
        """Test invalid identifier with special characters"""
        self.assertTrue(TestLexer.checkLexeme("my$var", "my,ErrorToken $", 205))

    # --------------- KEYWORDS TEST CASES ----------------

    def test_all_miniGo_keywords(self):
        """Test all MiniGo keywords"""
        input_str = "var const func type if else for return break continue true false nil int float boolean string"
        expected_output = "var,const,func,type,if,else,for,return,break,continue,true,false,nil,int,float,boolean,string,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 206))

    # --------------- OPERATOR TEST CASES ----------------

    def test_arithmetic_operators(self):
        """Test arithmetic operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / %", "+,-,*,/,%,<EOF>", 207))

    def test_relational_operators(self):
        """Test relational operators"""
        self.assertTrue(TestLexer.checkLexeme("== != < <= > >=", "==,!=,<,<=,>,>=,<EOF>", 208))

    def test_logical_operators(self):
        """Test logical operators"""
        self.assertTrue(TestLexer.checkLexeme("&& || !", "&&,||,!,<EOF>", 209))

    def test_assignment_operators(self):
        """Test assignment operators"""
        self.assertTrue(TestLexer.checkLexeme(":= =", ":=,=,<EOF>", 210))

    # --------------- SEPARATOR TEST CASES ----------------

    def test_separators(self):
        """Test separators: parentheses, brackets, braces, comma, semicolon"""
        self.assertTrue(TestLexer.checkLexeme("( ) { } [ ] , ;", "(,),{,},[,],,,;,<EOF>", 211))

    # --------------- INTEGER LITERALS TEST CASES ----------------

    def test_valid_integer_literals(self):
        """Test valid integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0 42 123456", "0,42,123456,<EOF>", 212))

    def test_invalid_integer_literal_leading_zero(self):
        """Test invalid integer with leading zero"""
        self.assertTrue(TestLexer.checkLexeme("0123", "0,123,<EOF>", 213))

    # --------------- FLOAT LITERALS TEST CASES ----------------

    def test_valid_float_literals(self):
        """Test valid floating-point literals"""
        self.assertTrue(TestLexer.checkLexeme("0.5 3.14 10.0e5", "0.5,3.14,10.0e5,<EOF>", 214))

    def test_invalid_float_literals(self):
        """Test invalid floating-point literals"""
        self.assertTrue(TestLexer.checkLexeme("1.", "1.,<EOF>", 215))
        self.assertTrue(TestLexer.checkLexeme(".5", ".,5,<EOF>", 216))
        self.assertTrue(TestLexer.checkLexeme("3.e10", "3.,e10,<EOF>", 217))

    # --------------- STRING LITERALS TEST CASES ----------------

    def test_valid_string_literals(self):
        """Test valid string literals"""
        self.assertTrue(TestLexer.checkLexeme('"Hello, World!"', '"Hello, World!",<EOF>', 218))

    def test_string_with_escape_sequencesss(self):
        """Test valid string with escape sequences"""
        self.assertTrue(TestLexer.checkLexeme('"This is a test \\n"', '"This is a test \\n",<EOF>', 219))

    def test_unclosed_string(self):
        """Test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme('"Unclosed string', "UnclosedString(Unclosed string)", 220))

    def test_illegal_escape_in_string(self):
        """Test illegal escape sequences"""
        self.assertTrue(TestLexer.checkLexeme('"Illegal \\m escape"', "IllegalEscape(Illegal \\m)", 221))

    # --------------- COMMENT TEST CASES ----------------

    def test_single_line_comments(self):
        """Test single-line comment"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment\nvar x int;", "var,x,int,;,<EOF>", 222))

    def test_multi_line_comments(self):
        """Test multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Comment block */ var y float;", "var,y,float,;,<EOF>", 223))

    def test_nested_comment(self):
        """Test nested multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Outer /* Inner */ Outer End */ var z int;", "var,z,int,;,<EOF>", 224))

    # --------------- COMPLEX EXPRESSIONS & STATEMENTS TEST CASES ----------------

    def test_complex_expression(self):
        """Test complex expressions with multiple operators"""
        self.assertTrue(TestLexer.checkLexeme("a + b * (c - d) / e", "a,+,b,*,(,c,-,d,),/,e,<EOF>", 225))

    def test_function_call(self):
        """Test function call with parameters"""
        self.assertTrue(TestLexer.checkLexeme("foo(10, 20, 30)", "foo,(,10,,,20,,,30,),<EOF>", 226))

    def test_array_access(self):
        """Test array access"""
        self.assertTrue(TestLexer.checkLexeme("arr[5] := 100;", "arr,[,5,],:=,100,;,<EOF>", 227))

    def test_nested_struct_declaration(self):
        """Test nested struct declaration"""
        input_str = """type Person struct {
            name string;
            age int;
            address struct {
                city string;
                zip int;
            };
        };"""
        expected_output = "type,Person,struct,{,name,string,;,age,int,;,address,struct,{,city,string,;,zip,int,;,},;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 228))

    def test_invalid_character(self):
        """Test invalid character"""
        self.assertTrue(TestLexer.checkLexeme("hello @world", "hello,ErrorToken @", 229))

    def test_invalid_syntax(self):
        """Test invalid syntax"""
        self.assertTrue(TestLexer.checkLexeme("var x 5;", "var,x,5,;,<EOF>", 230))

    def test_invalid_index_access(self):
        """Test invalid index access"""
        self.assertTrue(TestLexer.checkLexeme("arr[] := 10;", "arr,[,],:=,10,;,<EOF>", 231))

    def test_identifier_starting_with_underscore(self):
        """Test identifiers that start with an underscore"""
        self.assertTrue(TestLexer.checkLexeme("_var_name", "_var_name,<EOF>", 301))

    def test_identifier_containing_numbers(self):
        """Test identifiers with numbers in different positions"""
        self.assertTrue(TestLexer.checkLexeme("name1 1name myVar123 abc_456", "name1,1,name,myVar123,abc_456,<EOF>", 302))

    def test_identifier_mixed_with_keywords(self):
        """Test identifiers that contain keywords"""
        self.assertTrue(TestLexer.checkLexeme("variableForIf elseBlock", "variableForIf,elseBlock,<EOF>", 303))

    def test_invalid_identifier_with_special_characters(self):
        """Test invalid identifiers containing special characters"""
        self.assertTrue(TestLexer.checkLexeme("hello@world", "hello,ErrorToken @", 304))

    # ------------------ KEYWORDS TEST CASES ------------------

    def test_all_keywords_separately(self):
        """Test all MiniGo keywords separately"""
        input_str = "var const func type if else for return break continue true false nil int float boolean string"
        expected_output = "var,const,func,type,if,else,for,return,break,continue,true,false,nil,int,float,boolean,string,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 305))

    def test_keywords_mixed_with_identifiers(self):
        """Test keywords appearing next to identifiers"""
        self.assertTrue(TestLexer.checkLexeme("varTest funcCall returnValue", "varTest,funcCall,returnValue,<EOF>", 306))

    # ------------------ OPERATOR TEST CASES ------------------

    def test_unexpected_operator_combinations(self):
        """Test unexpected combinations of operators"""
        self.assertTrue(TestLexer.checkLexeme("=== !=== >>> <<<", "==,=,!=,==,>,>,>,<,<,<,<EOF>", 307))

    def test_separated_operators(self):
        """Test operators separated by spaces"""
        self.assertTrue(TestLexer.checkLexeme("= := + - * / % == != < <= > >=", "=,:=,+,-,*,/,%,==,!=,<,<=,>,>=,<EOF>", 308))

    def test_unexpected_operators(self):
        """Test invalid or unexpected operator tokens"""
        self.assertTrue(TestLexer.checkLexeme("a ? b : c", "a,ErrorToken ?,b,ErrorToken :,c,<EOF>", 309))

    # ------------------ SEPARATOR TEST CASES ------------------

    def test_separators_with_spaces(self):
        """Test separators spaced out"""
        self.assertTrue(TestLexer.checkLexeme("( ) { } [ ] , ;", "(,),{,},[,],,,;,<EOF>", 310))

    def test_separators_without_spaces(self):
        """Test separators appearing without spaces"""
        self.assertTrue(TestLexer.checkLexeme("(){},;", "(,),{,},,,;,<EOF>", 311))

    # ------------------ NUMBER LITERAL TEST CASES ------------------

    def test_various_number_literals(self):
        """Test integer and floating-point literals"""
        self.assertTrue(TestLexer.checkLexeme("42 0 123456 0.5 3.14 2e10 5.0E-3", "42,0,123456,0.5,3.14,2e10,5.0E-3,<EOF>", 312))

    def test_invalid_number_literals(self):
        """Test incorrectly formatted numbers"""
        self.assertTrue(TestLexer.checkLexeme(".5", ".,5,<EOF>", 313))
        self.assertTrue(TestLexer.checkLexeme("1.", "1.,<EOF>", 314))
        self.assertTrue(TestLexer.checkLexeme("2.e3", "2.,e3,<EOF>", 315))
        self.assertTrue(TestLexer.checkLexeme("0b101", "0,b101,<EOF>", 316))  # No binary literals in MiniGo

    # ------------------ STRING LITERAL TEST CASES ------------------

    def test_valid_string_literalssss(self):
        """Test valid string literals"""
        self.assertTrue(TestLexer.checkLexeme('"hello world"', '"hello world",<EOF>', 317))
        self.assertTrue(TestLexer.checkLexeme('"String with escape \\n"', '"String with escape \\n",<EOF>', 318))

    def test_unclosed_string_literals(self):
        """Test unclosed string literals"""
        self.assertTrue(TestLexer.checkLexeme('"This is unclosed', "UnclosedString(This is unclosed)", 319))

    def test_illegal_escape_sequencess(self):
        """Test illegal escape sequences in string literals"""
        self.assertTrue(TestLexer.checkLexeme('"Illegal \\q escape"', "IllegalEscape(Illegal \\q)", 320))

    def test_empty_string(self):
        """Test empty string literals"""
        self.assertTrue(TestLexer.checkLexeme('""', '"",<EOF>', 321))

    # ------------------ COMMENT TEST CASES ------------------

    def test_single_line_commentsss(self):
        """Test single-line comment"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment\nvar x int;", "var,x,int,;,<EOF>", 322))

    def test_multi_line_comment(self):
        """Test multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Comment block */ var y float;", "var,y,float,;,<EOF>", 323))

    def test_nested_comment(self):
        """Test nested multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Outer /* Inner */ Outer End */ var z int;", "var,z,int,;,<EOF>", 324))

    # ------------------ COMPLEX STATEMENTS & EXPRESSIONS TEST CASES ------------------

    def test_function_call_with_expressions(self):
        """Test function calls with expressions as arguments"""
        self.assertTrue(TestLexer.checkLexeme("foo(10 + 5, 3.14 * 2)", "foo,(,10,+,5,,,3.14,*,2,),<EOF>", 325))

    def test_array_index_access(self):
        """Test array indexing"""
        self.assertTrue(TestLexer.checkLexeme("arr[10] := 5;", "arr,[,10,],:=,5,;,<EOF>", 326))

    def test_nested_expressions(self):
        """Test complex nested expressions"""
        self.assertTrue(TestLexer.checkLexeme("a + (b - c) * (d / e)", "a,+,(,b,-,c,),*,(,d,/,e,),<EOF>", 327))

    # ------------------ ERROR HANDLING TEST CASES ------------------

    def test_unexpected_characters(self):
        """Test unexpected characters in input"""
        self.assertTrue(TestLexer.checkLexeme("foo # bar", "foo,ErrorToken #,bar,<EOF>", 328))

    def test_invalid_variable_declaration(self):
        """Test incorrect variable declaration syntax"""
        self.assertTrue(TestLexer.checkLexeme("var x 5;", "var,x,5,;,<EOF>", 329))

    def test_invalid_function_declaration(self):
        """Test incorrect function declaration"""
        self.assertTrue(TestLexer.checkLexeme("func test { return 0; }", "func,test,{,return,0,;,},<EOF>", 330))

    def test_unexpected_tokens(self):
        """Test unexpected tokens in expressions"""
        self.assertTrue(TestLexer.checkLexeme("if (x ?? y) {}", "if,(,x,ErrorToken ?,?,y,),{,},<EOF>", 331))
    def test_identifier_containing_only_underscore(self):
        """Test an identifier that consists only of underscores"""
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 401))

    def test_identifier_mixed_with_numbers_and_underscore(self):
        """Test identifiers with numbers and underscores"""
        self.assertTrue(TestLexer.checkLexeme("_var123 var_456 _1_2_", "_var123,var_456,_1_2_,<EOF>", 402))

    def test_reserved_keyword_as_partial_identifier(self):
        """Test identifiers containing reserved keywords"""
        self.assertTrue(TestLexer.checkLexeme("funcTest ifCondition returnValue", "funcTest,ifCondition,returnValue,<EOF>", 403))

    # ------------------ COMPLEX KEYWORDS TEST CASES ------------------

    def test_misplaced_keywords(self):
        """Test keywords appearing in invalid places"""
        self.assertTrue(TestLexer.checkLexeme("return = 5;", "return,=,5,;,<EOF>", 404))
        self.assertTrue(TestLexer.checkLexeme("if + else", "if,+,else,<EOF>", 405))

    def test_keywords_adjacent_to_symbols(self):
        """Test keywords appearing next to symbols"""
        self.assertTrue(TestLexer.checkLexeme("for(int x = 0; x < 10; x++)", "for,(,int,x,=,0,;,x,<,10,;,x,+,+,),<EOF>", 406))

    # ------------------ COMPLEX OPERATOR TEST CASES ------------------

    def test_misused_operators(self):
        """Test unexpected uses of operators"""
        self.assertTrue(TestLexer.checkLexeme("5 * / 3", "5,*,/,3,<EOF>", 407))
        self.assertTrue(TestLexer.checkLexeme("a && || b", "a,&&,||,b,<EOF>", 408))

    def test_unexpected_operator_combinations(self):
        """Test invalid operator combinations"""
        self.assertTrue(TestLexer.checkLexeme("!== <<= >>=", "!=,=,<<,=,>>=,<EOF>", 409))

    # ------------------ EXTREME STRING TEST CASES ------------------

    def test_string_with_escaped_double_quotes(self):
        """Test strings containing escaped double quotes"""
        self.assertTrue(TestLexer.checkLexeme('"This is a \\"quoted\\" word"', '"This is a \\"quoted\\" word",<EOF>', 410))

    def test_multiline_string(self):
        """Test unclosed multiline string"""
        self.assertTrue(TestLexer.checkLexeme('"This is a \n multiline string', "UnclosedString(This is a )", 411))




    # ------------------ ADVANCED COMMENTS TEST CASES ------------------

    def test_comment_followed_by_code(self):
        """Test comment before code"""
        self.assertTrue(TestLexer.checkLexeme("// comment\nvar x int;", "var,x,int,;,<EOF>", 413))

    def test_nested_comments_with_code_inside(self):
        """Test a block comment with code inside"""
        self.assertTrue(TestLexer.checkLexeme("/* var x = 10; */ var y int;", "var,y,int,;,<EOF>", 414))

    def test_nested_multiline_comments(self):
        """Test deeply nested multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Outer /* Inner /* Deepest */ End */ */", "<EOF>", 415))

    # ------------------ NESTED STRUCTURES TEST CASES ------------------

    def test_deeply_nested_struct(self):
        """Test a deeply nested struct declaration"""
        input_str = """type Person struct {
            name string;
            address struct {
                city string;
                coordinates struct {
                    latitude float;
                    longitude float;
                };
            };
        };"""
        expected_output = "type,Person,struct,{,name,string,;,address,struct,{,city,string,;,coordinates,struct,{,latitude,float,;,longitude,float,;,},;,},;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 416))

    def test_struct_with_multiple_nested_arrays(self):
        """Test struct containing arrays and nested structs"""
        input_str = """type Data struct {
            values [10]int;
            nested struct {
                names [5]string;
                metrics [3][3]float;
            };
        };"""
        expected_output = "type,Data,struct,{,values,[,10,],int,;,nested,struct,{,names,[,5,],string,;,metrics,[,3,],[,3,],float,;,},;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 417))

    # ------------------ LONG INPUT TEST CASES ------------------

    def test_very_long_identifier(self):
        """Test an excessively long identifier"""
        long_id = "a" * 256
        self.assertTrue(TestLexer.checkLexeme(long_id, long_id + ",<EOF>", 418))

    def test_large_code_snippet(self):
        """Test large MiniGo code snippet"""
        input_str = """
        var x int;
        var y float;
        func add(a int, b int): int {
            return a + b;
        }
        """
        expected_output = "var,x,int,;,var,y,float,;,func,add,(,a,int,,,b,int,),:,int,{,return,a,+,b,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 419))

    # ------------------ ERROR HANDLING TEST CASES ------------------

    def test_invalid_characters(self):
        """Test input containing illegal characters"""
        self.assertTrue(TestLexer.checkLexeme("var x # y;", "var,x,ErrorToken #,y,;,<EOF>", 420))

    def test_mixed_valid_and_invalid_tokens(self):
        """Test a mix of valid and invalid tokens"""
        self.assertTrue(TestLexer.checkLexeme("func test() { x := 10; & y := 20; }", "func,test,(,),{,x,:=,10,;,ErrorToken &,y,:=,20,;,},<EOF>", 421))

    def test_illegal_number_literal(self):
        """Test illegal number formats"""
        self.assertTrue(TestLexer.checkLexeme("123abc", "123,abc,<EOF>", 422))
        self.assertTrue(TestLexer.checkLexeme("12.34.56", "12.34,.,56,<EOF>", 423))

    def test_unexpected_end_of_input(self):
        """Test unexpected EOF in a complex expression"""
        self.assertTrue(TestLexer.checkLexeme("func main() { if (x ", "func,main,(,),{,if,(,x,<EOF>", 424))

    # ------------------ EXTREME NESTING TEST CASES ------------------

    def test_extremely_nested_expressions(self):
        """Test an extremely nested expression"""
        self.assertTrue(TestLexer.checkLexeme("(((((((x + y) * z) / w) % v) - u) == t)", "(,(,(,(,(,(,(,x,+,y,),*,z,),/,w,),%,v,),-,u,),==,t,),<EOF>", 425))

    def test_nested_function_calls(self):
        """Test deeply nested function calls"""
        self.assertTrue(TestLexer.checkLexeme("func(a(b(c(d(e(f()))))))", "func,(,a,(,b,(,c,(,d,(,e,(,f,(,),),),),),),),<EOF>", 426))
    def test_identifier_with_special_characters(self):
        """Test invalid identifiers containing special characters"""
        self.assertTrue(TestLexer.checkLexeme("my$var another@var", "my,ErrorToken $,var,another,ErrorToken @,var,<EOF>", 501))

    def test_long_identifier(self):
        """Test excessively long identifier"""
        long_id = "a" * 300
        self.assertTrue(TestLexer.checkLexeme(long_id, long_id + ",<EOF>", 502))

    def test_identifiers_with_reserved_keywords(self):
        """Test identifiers that contain reserved keywords"""
        self.assertTrue(TestLexer.checkLexeme("ifElse varForLoop funcCall", "ifElse,varForLoop,funcCall,<EOF>", 503))

    # ------------------ KEYWORDS EDGE CASES ------------------

    def test_mixed_keywords_and_identifiers(self):
        """Test mixing keywords and identifiers"""
        self.assertTrue(TestLexer.checkLexeme("if var123 returnVal elseStruct", "if,var123,returnVal,elseStruct,<EOF>", 504))

    def test_keywords_as_identifiers(self):
        """Test reserved keywords used incorrectly"""
        self.assertTrue(TestLexer.checkLexeme("var int float string", "var,int,float,string,<EOF>", 505))

    # ------------------ OPERATOR EDGE CASES ------------------

    def test_unexpected_operator_usage(self):
        """Test unexpected usage of operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / % := == !=", "+,-,*,/,%,:=,==,!=,<EOF>", 506))

    def test_operator_spacing_issues(self):
        """Test spacing issues with operators"""
        self.assertTrue(TestLexer.checkLexeme("x+=y x-=y x*=y x/=y x%=y", "x,+,=,y,x,-,=,y,x,*,=,y,x,/,=,y,x,%,=,y,<EOF>", 507))

    def test_malformed_operators(self):
        """Test malformed operators"""
        self.assertTrue(TestLexer.checkLexeme("!== <<= >>=", "!=,=,<<,=,>>=,<EOF>", 508))

    # ------------------ STRING LITERALS EDGE CASES ------------------

    def test_unclosed_string_literal(self):
        """Test unclosed string literal"""
        self.assertTrue(TestLexer.checkLexeme('"This is an unclosed string', "UnclosedString(This is an unclosed string)", 509))

    def test_string_with_escape_sequences(self):
        """Test string containing escape sequences"""
        self.assertTrue(TestLexer.checkLexeme('"Hello \\n World!"', '"Hello \\n World!",<EOF>', 510))

    def test_illegal_escape_sequence(self):
        """Test illegal escape sequence"""
        self.assertTrue(TestLexer.checkLexeme('"Illegal \\q escape"', "IllegalEscape(Illegal \\q)", 511))

    def test_string_with_nested_quotes(self):
        """Test string containing escaped double quotes"""
        self.assertTrue(TestLexer.checkLexeme('"He said: \\"Hello!\\""', '"He said: \\"Hello!\\"",<EOF>', 512))

    # ------------------ COMMENT EDGE CASES ------------------

    def test_single_line_comment(self):
        """Test single-line comment"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment\nvar x int;", "var,x,int,;,<EOF>", 513))

    def test_multi_line_commensssst(self):
        """Test multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Multi-line comment */ var y float;", "var,y,float,;,<EOF>", 514))

    def test_nested_multi_line_comments(self):
        """Test deeply nested multi-line comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Outer /* Inner /* Deepest */ End */ */", "<EOF>", 515))

    # ------------------ COMPLEX EXPRESSIONS ------------------

    def test_complex_math_expression(self):
        """Test complex mathematical expression"""
        self.assertTrue(TestLexer.checkLexeme("a + (b - c) * (d / e) % f", "a,+,(,b,-,c,),*,(,d,/,e,),%,f,<EOF>", 516))

    def test_complex_logical_expression(self):
        """Test complex logical expression"""
        self.assertTrue(TestLexer.checkLexeme("if (a && b || !c)", "if,(,a,&&,b,||,!,c,),<EOF>", 517))

    def test_nested_function_calls(self):
        """Test deeply nested function calls"""
        self.assertTrue(TestLexer.checkLexeme("func(a(b(c(d(e(f()))))))", "func,(,a,(,b,(,c,(,d,(,e,(,f,(,),),),),),),),<EOF>", 518))

    def test_array_indexing_with_expressions(self):
        """Test array indexing with complex expressions"""
        self.assertTrue(TestLexer.checkLexeme("arr[(x + y) * 2] := 5;", "arr,[,(,x,+,y,),*,2,],:=,5,;,<EOF>", 519))

    # ------------------ INVALID SYNTAX TEST CASES ------------------

    def test_invalid_variable_declaration(self):
        """Test incorrect variable declaration syntax"""
        self.assertTrue(TestLexer.checkLexeme("var x 5;", "var,x,5,;,<EOF>", 520))

    def test_invalid_function_declaration(self):
        """Test incorrect function declaration"""
        self.assertTrue(TestLexer.checkLexeme("func test { return 0; }", "func,test,{,return,0,;,},<EOF>", 521))

    def test_unexpected_symbols(self):
        """Test unexpected symbols in input"""
        self.assertTrue(TestLexer.checkLexeme("var x @ y;", "var,x,ErrorToken @,y,;,<EOF>", 522))

    def test_unexpected_end_of_input(self):
        """Test unexpected EOF in a complex expression"""
        self.assertTrue(TestLexer.checkLexeme("if (x ", "if,(,x,<EOF>", 523))

    # ------------------ EXTREME NESTING TEST CASES ------------------

    def test_extremely_nested_expressions(self):
        """Test extremely nested mathematical expressions"""
        self.assertTrue(TestLexer.checkLexeme("(((((((x + y) * z) / w) % v) - u) == t)", "(,(,(,(,(,(,(,x,+,y,),*,z,),/,w,),%,v,),-,u,),==,t,),<EOF>", 524))

    def test_nested_struct_definitions(self):
        """Test deeply nested struct declarations"""
        input_str = """type A struct {
            field1 int;
            field2 struct {
                field3 float;
                field4 struct {
                    field5 string;
                };
            };
        };"""
        expected_output = "type,A,struct,{,field1,int,;,field2,struct,{,field3,float,;,field4,struct,{,field5,string,;,},;,},;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 525))

    def test_nested_loops_and_conditions(self):
        """Test deeply nested loops and conditionals"""
        input_str = """for i := 0; i < 10; i++ {
            if (i % 2 == 0) {
                while (j < i) {
                    j := j + 1;
                }
            }
        }"""
        expected_output = "for,i,:=,0,;,i,<,10,;,i,+,+,{,if,(,i,%,2,==,0,),{,while,(,j,<,i,),{,j,:=,j,+,1,;,},},},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected_output, 526))