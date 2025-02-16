import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_valid_function_declaration(self):
        """Test valid function declaration"""
        input = """func sum(a int, b int) : int {
            return a + b;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_valid_variable_declaration(self):
        """Test valid variable declaration"""
        input = """var x : int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_valid_constant_declaration(self):
        """Test valid constant declaration"""
        input = """const PI : float = 3.14;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_valid_if_statement(self):
        """Test valid if-else statement"""
        input = """func checkNumber(x int) {
            if (x > 0) {
                return 1;
            } else {
                return 0;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_valid_for_loop(self):
        """Test valid for loop"""
        input = """func loopTest() {
            for i := 0; i < 10; i += 1 {
                var y : int;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_valid_struct_declaration(self):
        """Test valid struct declaration"""
        input = """type Person struct {
            name : string;
            age : int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_valid_interface_declaration(self):
        """Test valid interface declaration"""
        input = """type Calculator interface {
            Add(x int, y int) : int;
            Subtract(a float, b int) : float;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    # ------------------ ❌ ERROR CASES ------------------

    def test_invalid_function_missing_braces(self):
        """Test function missing closing brace"""
        input = """func foo() { return 1;"""
        expect = "Error on line 1 col 25: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_invalid_variable_declaration(self):
        """Test invalid variable declaration"""
        input = """var : int;"""
        expect = "Error on line 1 col 4: :"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_invalid_for_loop_missing_condition(self):
        """Test invalid for loop missing condition"""
        input = """func loop() {
            for ; i += 1 {
                var x : int;
            }
        };"""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_invalid_struct_missing_field_type(self):
        """Test struct missing field type"""
        input = """type Employee struct {
            name;
            age : int;
        };"""
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_invalid_function_call_missing_parentheses(self):
        """Test function call missing parentheses"""
        input = """func main() {
            print;
        };"""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_invalid_nested_statements(self):
        """Test invalid nested statements"""
        input = """func main() {
            if (x > 0) {
                for i := 0; i < 10; i += 1 
                    return i;
                };
            }
        };"""
        expect = "Error on line 5 col 18: }"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_invalid_expression_missing_operator(self):
        """Test invalid expression missing operator"""
        input = """func main() {
            var x : int = 5 5;
        };"""
        expect = "Error on line 2 col 30: 5"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_invalid_array_declaration(self):
        """Test invalid array declaration"""
        input = """var arr : [5] int;"""
        expect = "Error on line 1 col 9: ["
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_invalid_return_statement(self):
        """Test invalid return statement"""
        input = """func foo() {
            return;
            return 1, 2;
        };"""
        expect = "Error on line 3 col 22: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_invalid_break_statement(self):
        """Test break statement outside of loop"""
        input = """func foo() {
            break;
        };"""
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_invalid_continue_statement(self):
        """Test continue statement outside of loop"""
        input = """func foo() {
            continue;
        };"""
        expect = "Error on line 2 col 12: continue"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_invalid_assignment_operator(self):
        """Test invalid assignment operator"""
        input = """func foo() {
            x = 10;
        };"""
        expect = "Error on line 2 col 14: ="
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_invalid_function_parameter_syntax(self):
        """Test invalid function parameter syntax"""
        input = """func add(a int b int) : int {
            return a + b;
        };"""
        expect = "Error on line 1 col 15: b"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_invalid_function_missing_semicolon(self):
        """Test missing semicolon after function declaration"""
        input = """func foo() {}"""
        expect = "Error on line 1 col 13: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_valid_nested_if_else(self):
        """Test valid nested if-else statement"""
        input = """func check(x int) {
            if (x > 0) {
                if (x < 10) {
                    return 1;
                } else {
                    return 2;
                }
            } else {
                return 0;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_valid_nested_for_loops(self):
        """Test valid nested for loops"""
        input = """func loop() {
            for i := 0; i < 5; i += 1 {
                for j := 0; j < 5; j += 1 {
                    var x : int;
                }
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_valid_function_call_with_arguments(self):
        """Test valid function call with multiple arguments"""
        input = """func main() {
            print(10, "Hello", 3.14);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_valid_while_loop_equivalent(self):
        """Test valid while-like loop using for"""
        input = """func loop() {
            for x < 100 {
                x := x + 1;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_valid_function_returning_struct(self):
        """Test function returning a struct"""
        input = """type Person struct {
            name : string;
            age : int;
        };

        func getPerson() : Person {
            return Person{name: "John", age: 25};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    # ------------------ ❌ ERROR CASES ------------------

    def test_invalid_function_missing_return_type(self):
        """Test function missing return type"""
        input = """func foo() {
            return 10;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_invalid_function_with_wrong_param_syntax(self):
        """Test function with wrong parameter syntax"""
        input = """func add(x int, y : int) {
            return x + y;
        };"""
        expect = "Error on line 1 col 17: :"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_invalid_function_call_wrong_argument_separator(self):
        """Test function call with wrong argument separator"""
        input = """func main() {
            print(10; "Hello"; 3.14);
        };"""
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_invalid_array_declaration_missing_size(self):
        """Test array declaration missing size"""
        input = """var arr : [] int;"""
        expect = "Error on line 1 col 9: ["
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_invalid_struct_declaration_missing_braces(self):
        """Test struct missing braces"""
        input = """type Car struct 
            model : string;
            year : int;
        ;"""
        expect = "Error on line 2 col 12: model"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_invalid_while_like_loop_missing_condition(self):
        """Test for-loop missing condition"""
        input = """func loop() {
            for {
                var x : int;
            }
        };"""
        expect = "Error on line 2 col 14: {"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_invalid_function_call_missing_closing_parenthesis(self):
        """Test function call missing closing parenthesis"""
        input = """func main() {
            print(10, 20;
        };"""
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_invalid_expression_with_multiple_operators(self):
        """Test expression with incorrect operator usage"""
        input = """func main() {
            var x : int = 5 + * 3;
        };"""
        expect = "Error on line 2 col 28: *"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_invalid_return_type_in_function(self):
        """Test function with invalid return type"""
        input = """func foo() : unknownType {
            return 10;
        };"""
        expect = "Error on line 1 col 11: unknownType"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_invalid_for_loop_missing_update_expression(self):
        """Test for loop missing update expression"""
        input = """func loop() {
            for i := 0; i < 10; {
                var x : int;
            }
        };"""
        expect = "Error on line 2 col 25: {"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_invalid_assignment_in_expression(self):
        """Test invalid assignment inside an expression"""
        input = """func main() {
            var x : int = (y := 10);
        };"""
        expect = "Error on line 2 col 29: :="
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_invalid_if_statement_missing_condition(self):
        """Test if statement missing condition"""
        input = """func main() {
            if {
                var x : int;
            }
        };"""
        expect = "Error on line 2 col 16: {"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_invalid_empty_function_body(self):
        """Test function with empty body"""
        input = """func empty();"""
        expect = "Error on line 1 col 12: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_invalid_mismatched_parentheses(self):
        """Test mismatched parentheses in expression"""
        input = """func main() {
            var x : int = (5 + 3;
        };"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_invalid_struct_missing_field_separator(self):
        """Test struct missing field separator"""
        input = """type Employee struct {
            name string
            age : int;
        };"""
        expect = "Error on line 2 col 17: string"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_invalid_return_inside_loop(self):
        """Test return inside loop"""
        input = """func loop() {
            for i := 0; i < 10; i += 1 {
                return;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))
    def test_valid_function_with_no_return(self):
        """Test function without a return statement"""
        input = """func doSomething() {
            var x : int = 10;
            var y : float = 5.5;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_valid_function_with_logical_expressions(self):
        """Test function using logical expressions"""
        input = """func check(x int, y int) : boolean {
            return (x > 0) && (y < 10) || !(x == y);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_valid_struct_initialization(self):
        """Test struct initialization inside a function"""
        input = """type Student struct {
            name : string;
            age : int;
        };

        func createStudent() : Student {
            return Student{name: "Alice", age: 20};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_valid_array_declaration_and_assignment(self):
        """Test array declaration and assignment"""
        input = """func main() {
            var numbers : [5] int;
            numbers[0] := 10;
            numbers[1] := 20;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_valid_nested_for_loops_with_conditions(self):
        """Test nested for loops with conditions"""
        input = """func process() {
            for i := 0; i < 5; i += 1 {
                for j := i; j < 10; j += 2 {
                    if (j % 2 == 0) {
                        continue;
                    }
                }
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_valid_function_call_with_return_value(self):
        """Test function call with return value"""
        input = """func add(x int, y int) : int {
            return x + y;
        };

        func main() {
            var result : int = add(3, 5);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    # ------------------ ❌ ERROR CASES ------------------

    def test_invalid_function_missing_colon_in_param(self):
        """Test function missing colon in parameter"""
        input = """func test(a int b int) {
            return a + b;
        };"""
        expect = "Error on line 1 col 15: b"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_invalid_function_call_with_missing_argument(self):
        """Test function call with missing argument"""
        input = """func main() {
            var result : int = add(3, );
        };"""
        expect = "Error on line 2 col 33: )"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_invalid_array_declaration_with_wrong_brackets(self):
        """Test array declaration with incorrect brackets"""
        input = """var numbers : {5} int;"""
        expect = "Error on line 1 col 14: {"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_invalid_missing_semicolon_after_statement(self):
        """Test missing semicolon after statement"""
        input = """func main() {
            var x : int = 10
            var y : float = 3.5;
        };"""
        expect = "Error on line 2 col 26: var"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_invalid_function_returning_array(self):
        """Test function returning an array (not supported)"""
        input = """func getArray() : [5] int {
            return [1, 2, 3, 4, 5];
        };"""
        expect = "Error on line 1 col 17: ["
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_invalid_if_statement_missing_condition(self):
        """Test if statement missing condition"""
        input = """func main() {
            if {
                var x : int = 10;
            }
        };"""
        expect = "Error on line 2 col 16: {"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_invalid_for_loop_with_malformed_condition(self):
        """Test for loop with incorrect condition"""
        input = """func loop() {
            for i := 0; i +; i += 1 {
                var x : int;
            }
        };"""
        expect = "Error on line 2 col 22: +"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_invalid_struct_with_duplicate_field_names(self):
        """Test struct with duplicate field names"""
        input = """type Employee struct {
            name : string;
            name : int;
        };"""
        expect = "Error on line 3 col 12: name"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_invalid_function_call_without_parentheses(self):
        """Test function call without parentheses"""
        input = """func main() {
            print;
        };"""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_invalid_logical_expression_with_mismatched_parentheses(self):
        """Test mismatched parentheses in logical expression"""
        input = """func check() : boolean {
            return (x > 10) && (y < 5;
        };"""
        expect = "Error on line 2 col 38: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_invalid_nested_function_declaration(self):
        """Test function declaration inside another function"""
        input = """func outer() {
            func inner() {
                return 10;
            };
        };"""
        expect = "Error on line 2 col 12: func"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_invalid_variable_initialization_with_wrong_type(self):
        """Test variable initialization with wrong type"""
        input = """func main() {
            var x : int = "Hello";
        };"""
        expect = "Error on line 2 col 26: Hello"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_invalid_use_of_break_outside_loop(self):
        """Test break outside of loop"""
        input = """func main() {
            break;
        };"""
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_invalid_continue_outside_loop(self):
        """Test continue outside of loop"""
        input = """func main() {
            continue;
        };"""
        expect = "Error on line 2 col 12: continue"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_invalid_function_with_multiple_return_statements(self):
        """Test function with multiple return values (not supported)"""
        input = """func foo() : int {
            return 1, 2;
        };"""
        expect = "Error on line 2 col 22: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 268))
    def test_valid_empty_function(self):
        """Test valid empty function"""
        input = """func doNothing() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_valid_recursive_function(self):
        """Test valid recursive function"""
        input = """func factorial(n int) : int {
            if (n == 0) {
                return 1;
            } else {
                return n * factorial(n - 1);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_valid_multiple_variable_declarations(self):
        """Test multiple variable declarations"""
        input = """func main() {
            var a : int = 10;
            var b : float = 3.14;
            var c : string = "hello";
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_valid_returning_struct_instance(self):
        """Test function returning a struct instance"""
        input = """type Car struct {
            brand : string;
            year : int;
        };

        func getCar() : Car {
            return Car{brand: "Toyota", year: 2020};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_valid_logical_expressions_with_parentheses(self):
        """Test logical expressions with nested parentheses"""
        input = """func checkCondition(x int, y int) : boolean {
            return ((x > 10) && (y < 20)) || (x == y);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_valid_array_access_and_modification(self):
        """Test array access and modification"""
        input = """func modifyArray() {
            var numbers : [3] int;
            numbers[0] := 100;
            numbers[1] := numbers[0] + 20;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_valid_nested_if_statements(self):
        """Test deeply nested if-else statements"""
        input = """func check(x int) {
            if (x > 0) {
                if (x < 10) {
                    if (x % 2 == 0) {
                        return 1;
                    } else {
                        return 2;
                    }
                } else {
                    return 3;
                }
            } else {
                return 4;
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_valid_interface_with_methods(self):
        """Test interface with multiple method signatures"""
        input = """type Shape interface {
            Area() : float;
            Perimeter() : float;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_valid_function_call_with_expressions(self):
        """Test function call with expressions as arguments"""
        input = """func main() {
            var result : int = add(5 + 3, 10 * 2);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    # ------------------ ❌ ERROR CASES ------------------

    def test_invalid_function_missing_return_type(self):
        """Test function missing return type"""
        input = """func foo() {
            return 42;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_invalid_function_with_multiple_return_values(self):
        """Test function returning multiple values (unsupported)"""
        input = """func foo() : int {
            return 10, 20;
        };"""
        expect = "Error on line 2 col 22: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_invalid_nested_function_definition(self):
        """Test nested function definition (not allowed)"""
        input = """func outer() {
            func inner() {
                return 10;
            };
        };"""
        expect = "Error on line 2 col 12: func"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_invalid_function_call_with_missing_argument(self):
        """Test function call missing an argument"""
        input = """func main() {
            var result : int = add(3, );
        };"""
        expect = "Error on line 2 col 33: )"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_invalid_expression_with_extra_operator(self):
        """Test expression with an extra operator"""
        input = """func main() {
            var x : int = 10 + * 5;
        };"""
        expect = "Error on line 2 col 28: *"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_invalid_variable_declaration_missing_type(self):
        """Test variable declaration missing type"""
        input = """var x;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_invalid_array_declaration_wrong_format(self):
        """Test array declaration with incorrect syntax"""
        input = """var arr : {5} int;"""
        expect = "Error on line 1 col 14: {"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_invalid_function_call_without_parentheses(self):
        """Test function call without parentheses"""
        input = """func main() {
            print;
        };"""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_invalid_struct_with_duplicate_field_names(self):
        """Test struct with duplicate field names"""
        input = """type Employee struct {
            name : string;
            name : int;
        };"""
        expect = "Error on line 3 col 12: name"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_invalid_if_statement_missing_condition(self):
        """Test if statement missing condition"""
        input = """func main() {
            if {
                var x : int = 10;
            }
        };"""
        expect = "Error on line 2 col 16: {"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_invalid_for_loop_with_missing_update(self):
        """Test for loop missing update expression"""
        input = """func loop() {
            for i := 0; i < 10; {
                var x : int;
            }
        };"""
        expect = "Error on line 2 col 25: {"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_invalid_mismatched_parentheses(self):
        """Test mismatched parentheses in expression"""
        input = """func main() {
            var x : int = (5 + 3;
        };"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_invalid_return_outside_function(self):
        """Test return statement outside function"""
        input = """return 10;"""
        expect = "Error on line 1 col 0: return"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_valid_empty_struct(self):
        """Test struct declaration with no fields"""
        input = """type Empty struct {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_valid_array_initialization(self):
        """Test array declaration with inline initialization"""
        input = """func main() {
            var arr : [3] int = [1, 2, 3];
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_valid_ternary_like_expression(self):
        """Test ternary-like conditional expressions"""
        input = """func check(x int) : int {
            return (x > 0) ? 1 : 0;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_valid_multiline_string_literal(self):
        """Test handling of multiline string literals"""
        input = """func main() {
            var text : string = "Hello 
                                World!";
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_valid_function_pointer_assignment(self):
        """Test function pointer assignment"""
        input = """func add(x int, y int) : int {
            return x + y;
        };

        func main() {
            var funcPtr : func(int, int) : int = add;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_valid_expression_with_multiple_operations(self):
        """Test arithmetic expression with multiple operators"""
        input = """func compute() : int {
            return (10 + 5) * 3 - 8 / 2;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_valid_interface_with_generic_methods(self):
        """Test interface with generic method signatures"""
        input = """type Transformer interface {
            Transform<T>(input T) : T;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_valid_lambda_function_assignment(self):
        """Test lambda function assigned to a variable"""
        input = """func main() {
            var square : func(int) : int = func(x int) : int { return x * x; };
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    # ------------------ ❌ ERROR CASES ------------------

    def test_invalid_missing_variable_type(self):
        """Test variable missing type annotation"""
        input = """var x = 10;"""
        expect = "Error on line 1 col 5: ="
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_invalid_function_missing_return_expression(self):
        """Test function returning a value without an expression"""
        input = """func foo() : int {
            return;
        };"""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test_invalid_array_declaration_with_wrong_syntax(self):
        """Test array declaration with incorrect syntax"""
        input = """var numbers : [int] 5;"""
        expect = "Error on line 1 col 16: int"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

    def test_invalid_function_call_missing_closing_parenthesis(self):
        """Test function call missing closing parenthesis"""
        input = """func main() {
            print(10, 20;
        };"""
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

    def test_invalid_expression_with_unclosed_parentheses(self):
        """Test expression with unclosed parentheses"""
        input = """func main() {
            var x : int = (5 + (3 * 2;
        };"""
        expect = "Error on line 2 col 36: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 303))

    def test_invalid_function_with_mismatched_parameters(self):
        """Test function definition with incorrectly formatted parameters"""
        input = """func add(x int, y) : int {
            return x + y;
        };"""
        expect = "Error on line 1 col 17: )"
        self.assertTrue(TestParser.checkParser(input, expect, 304))

    def test_invalid_struct_with_duplicate_fields(self):
        """Test struct declaration with duplicate field names"""
        input = """type User struct {
            name : string;
            age : int;
            name : int;
        };"""
        expect = "Error on line 4 col 12: name"
        self.assertTrue(TestParser.checkParser(input, expect, 305))

    def test_invalid_nested_for_loops_missing_condition(self):
        """Test nested for loops missing conditions"""
        input = """func loop() {
            for i := 0; i++ {
                for j := 0; j++ {
                    var x : int;
                }
            }
        };"""
        expect = "Error on line 2 col 22: {"
        self.assertTrue(TestParser.checkParser(input, expect, 306))

    def test_invalid_unexpected_break(self):
        """Test break statement outside of a loop"""
        input = """func main() {
            break;
        };"""
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.checkParser(input, expect, 307))

    def test_invalid_unexpected_continue(self):
        """Test continue statement outside of a loop"""
        input = """func main() {
            continue;
        };"""
        expect = "Error on line 2 col 12: continue"
        self.assertTrue(TestParser.checkParser(input, expect, 308))

    def test_invalid_while_loop_syntax(self):
        """Test while loop using incorrect syntax"""
        input = """func loop() {
            while (x < 10) {
                x += 1;
            }
        };"""
        expect = "Error on line 2 col 12: while"
        self.assertTrue(TestParser.checkParser(input, expect, 309))

    def test_invalid_function_call_with_extra_comma(self):
        """Test function call with extra comma"""
        input = """func main() {
            print(10,, 20);
        };"""
        expect = "Error on line 2 col 22: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 310))

    def test_invalid_assignment_operator_misuse(self):
        """Test variable assignment using unsupported operator"""
        input = """func main() {
            x == 10;
        };"""
        expect = "Error on line 2 col 14: =="
        self.assertTrue(TestParser.checkParser(input, expect, 311))

    def test_invalid_function_definition_with_wrong_colon(self):
        """Test function definition using incorrect colon placement"""
        input = """func foo() int : {
            return 10;
        };"""
        expect = "Error on line 1 col 12: int"
        self.assertTrue(TestParser.checkParser(input, expect, 312))