grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
    language = Python3;
}

program  : decl+ EOF ;

decl
    : vardecl
    | constdecl
    | funcdecl
    | typedecl
    ;

vardecl
    : 'var' (ID)? ':' typeID ('=' expression)? ';' ;



constdecl
    : 'const' ID (':' typeID)? '=' expression ';' ;

typedecl
    : 'type' ID '=' typeID ';'   // Type aliasing
    | 'type' ID structType ';'   // Struct definition
    ;

funcdecl
    : 'func' ID '(' paramList? ')' (':' typeID | ) blockStmt ';'
    ;

paramList
    : param (',' param)* 
    ;

param
    : ID ':' typeID
    ;

blockStmt
    : '{' stmt* '}' 
    ;

stmt
    : vardecl
    | assignStmt
    | returnStmt
    | ifStmt
    | forStmt
    | breakStmt
    | continueStmt
    | callStmt
    | blockStmt 
    ;

assignStmt
    : ID ( '[' expression ']' )? ':=' expression ';'
    ;

returnStmt
    : 'return' expression? ';'
    ;

ifStmt
    : 'if' '(' expression ')' blockStmt ( 'else' blockStmt )?
    ;

forStmt
    : 'for' (assignStmt? ';' expression? ';' assignStmt? | expression)? '{' loopStmt* '}'  
    | 'for' ID ',' ID 'in' ID '{' loopStmt* '}' 
    ;

loopStmt
    : vardecl
    | assignStmt
    | returnStmt
    | ifStmt
    | forStmt
    | breakStmt      
    | continueStmt   
    | callStmt
    ;

breakStmt
    : 'break' ';'
    ;

continueStmt
    : 'continue' ';'
    ;

callStmt
    : ID '(' argList? ')' ';'
    ;

argList
    : expression (',' expression)* 
    ;

expression
    : expression op=('*' | '/' | '%') expression
    | expression op=('+' | '-') expression
    | expression op=('==' | '!=' | '<' | '<=' | '>' | '>=') expression
    | expression '&&' expression
    | expression '||' expression
    | '!' expression
    | '(' expression ')'  
    | structInitExpr
    | ID
    | literal
    | ID '{' structInitList '}'
    | expression '?' expression ':' expression   // Ternary operator
    ;

structInitExpr
    : ID '{' structInitList '}'                
    ;

structInitList
    : structInitField (',' structInitField)* 
    ;

structInitField
    : ID ':' expression
    ;

literal
    : INTLIT
    | FLOATLIT
    | STRINGLIT
    | 'true'
    | 'false'
    | 'nil'
    ;

typeID
    : 'int'
    | 'float'
    | 'boolean'
    | 'string'
    | arrayType
    | structType
    | interfaceType
    ;

arrayType
    : '[' INTLIT ']' typeID
    ;

structType
    : 'struct' '{' fieldDecl+ '}'
    ;

fieldDecl
    : ID ':' typeID ';'
    ;

interfaceType
    : 'interface' '{' methodDecl* '}'
    ;

methodDecl
    : ID '(' paramList? ')' (':' typeID)? ';'
    ;

/* Lexer Rules */
ID  : [a-zA-Z_][a-zA-Z0-9_]* ;

INTLIT 
    : '0' | [1-9] [0-9]*  
    ;

FLOATLIT 
    : [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?  
    | [0-9]+ [eE] [+-]? [0-9]+                
    ;

ILLEGAL_FLOAT 
    : [0-9]+ '.' {self.text = self.text[:-1]; raise ErrorToken(self.text + ".");}
    | '.' [0-9]+ {self.text = self.text; raise ErrorToken(self.text);}
    ;

STRINGLIT 
    : '"' ( ~["\\\r\n] | '\\' ["\\/bfnrt] )* '"' 
    ;

UNCLOSE_STRING 
    : '"' ( ~["\\\r\n] | '\\' ["\\/bfnrt] )* (EOF | '\n') 
    {
        text = self.text[1:]  # Remove leading quote
        if text[-1] in ['\n', '\r']: 
            raise UncloseString(text[:-1])  # Remove trailing newline if present
        else:
            raise UncloseString(text) 
    }
    ;

COMMENT 
    : '/*' (COMMENT | .)*? '*/' -> skip 
    ;

WS  
    : [ \t\r\n]+ -> skip 
    ;

// ******* KEY CHANGE: remove `?` so it is not an error token *******
ERROR_CHAR: [@#^&] ;

ILLEGAL_ESCAPE: .;  
