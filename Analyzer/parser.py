import ply.yacc as yacc

from Analyzer.scanner import tokens
from Expression.Abs import Abs
from Expression.Arithmetic import Arithmetic
from Expression.ArrayAccess import ArrayAccess
from Expression.CaseExpr import CaseExpr
from Expression.Cast import Cast
from Expression.Clone import Clone
from Expression.CreateArray import CreateArray
from Expression.DefaultExpr import DefaultExpr
from Expression.IfExpr import IfExpr
from Expression.Literal import Literal
from Expression.Logic import Logic
from Expression.Relational import Relational
from Expression.SimpleAccess import SimpleAccess
from Expression.Sqrt import Sqrt
from Expression.ToString import ToString
from Instruction.Asignation import Asignation
from Instruction.Break import Break
from Instruction.Case import Case
from Instruction.Continue import Continue
from Instruction.Declaration import Declaration
from Instruction.Default import Default
from Instruction.If import If
from Instruction.Loop import Loop
from Instruction.Match import Match
from Instruction.Println import Println
from Instruction.Return import Return
from Instruction.Statement import Statement
from Instruction.While import While
from Util.Array import Array
from Util.Expression import Expression
from Util.Retorno import ArithmeticType, LogicType, RelationalType, Type

precedence = (
    ("left", "OR"),
    ("left", "AND"),
    ("left", "EQUALS", "NEQUALS"),
    ("left", "LTHAN", "GTHAN", "LORE", "GORE"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE", "MODULE"),
    ("nonassoc", "POWER"),
    ("right", "RAS"),
    ("right", "UMINUS", "NOT"),  # Unary minus operator
    ("left", "DOT"),
)


def p_init(p):
    "init : instructions"
    p[0] = p[1]


def p_instructions(p):
    "instructions : instructions instruction"
    p[1].append(p[2])
    p[0] = p[1]


def p_instructions_instr(p):
    "instructions : instruction"
    p[0] = [p[1]]


def p_instr(p):
    """instruction : declaration SEMICOLON
    | println SEMICOLON
    | asignation SEMICOLON
    | ifst
    | match
    | while
    | loop
    | break SEMICOLON
    | continue SEMICOLON
    | return SEMICOLON"""
    p[0] = p[1]


def p_simple_instr(p):
    """simple_instr : println
    | asignation
    | declaration
    | break
    | continue
    | return"""
    p[0] = p[1]


def p_primitive_type(p):
    """primitive_type : RINT
    | RFLOAT
    | RBOOL
    | RCHAR
    | AMPERSAND RSTR
    | RSTRING
    | RUSIZE"""
    if p[1] == "i64":
        p[0] = Type.Int
    elif p[1] == "f64":
        p[0] = Type.Float
    elif p[1] == "bool":
        p[0] = Type.Bool
    elif p[1] == "char":
        p[0] = Type.Char
    elif p[1] == "&":
        p[0] = Type.Str
    elif p[1] == "String":
        p[0] = Type.String
    else:
        p[0] = Type.Usize


def p_array_type(p):
    "array_type : LBRACKET primitive_type SEMICOLON INT RBRACKET"
    p[0] = {"type": p[2], "size": p[4]}


def p_array_type_arr(p):
    "array_type : LBRACKET array_type SEMICOLON INT RBRACKET"
    p[0] = {"type": p[2], "size": p[4]}


# TODO: Implementar arrays de tipo struct y vector


def p_statement(p):
    "statement : LCBRACKET instructions RCBRACKET"
    p[0] = Statement(p.lineno(1), p.lexpos(1), p[2])


def p_declaration_mut_type(p):
    """declaration : RLET RMUT ID COLON primitive_type EQUAL expression"""
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[3], True, p[7], p[5])


def p_declaration_type(p):
    """declaration : RLET ID COLON primitive_type EQUAL expression"""
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[2], False, p[6], p[4])


def p_declaration_mut(p):
    """declaration : RLET RMUT ID EQUAL expression"""
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[3], True, p[5], None)


def p_declaration(p):
    """declaration : RLET ID EQUAL expression"""
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[2], False, p[4], None)


def p_declaration_array_mut(p):
    "declaration : RLET RMUT ID COLON array_type EQUAL expression"
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[3], True, p[7], p[5])


def p_declaration_array(p):
    "declaration : RLET ID COLON array_type EQUAL expression"
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[2], False, p[6], p[4])


def p_println(p):
    "println : RPRINT NOT LPAREN expressions RPAREN"
    p[0] = Println(p.lineno(1), p.lexpos(1), p[4])


def p_asignation(p):
    """asignation : ID EQUAL expression"""
    p[0] = Asignation(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_ifst(p):
    "ifst : RIF expression statement else_st"
    p[0] = If(p.lineno(1), p.lexpos(1), p[2], p[3], p[4])


def p_else_st(p):
    """else_st : RELSE statement
    | RELSE ifst
    | empty"""
    if p[1] == "else":
        p[0] = p[2]
    else:
        p[0] = None


def p_ifst_expr(p):
    "if_expr : RIF expression LCBRACKET instructions expression RCBRACKET else_st_expr"
    p[0] = IfExpr(p.lineno(1), p.lexpos(1), p[2], p[4], p[5], p[7])


def p_ifst_expr_2(p):
    "if_expr : RIF expression LCBRACKET expression RCBRACKET else_st_expr"
    p[0] = IfExpr(p.lineno(1), p.lexpos(1), p[2], None, p[4], p[6])


def p_else_st_expr(p):
    """else_st_expr : RELSE LCBRACKET instructions expression RCBRACKET
    | RELSE LCBRACKET expression RCBRACKET
    | RELSE if_expr
    | empty"""
    if p[1] == "else":
        if p[2] == "{":
            if isinstance(p[3], Expression):
                p[0] = DefaultExpr(p.lineno(1), p.lexpos(1), None, p[3])
            else:
                p[0] = DefaultExpr(p.lineno(1), p.lexpos(1), p[3], p[4])
        else:
            p[0] = p[2]
    else:
        p[0] = None


def p_match(p):
    "match : RMATCH expression LCBRACKET cases default RCBRACKET"
    p[0] = Match(p.lineno(1), p.lexpos(1), p[2], p[4], p[5])


def p_cases(p):
    "cases : cases case"
    p[1].append(p[2])
    p[0] = p[1]


def p_cases_case(p):
    "cases : case"
    p[0] = [p[1]]


def p_case(p):
    """case : expressions_match ARROW statement
    | expressions_match ARROW simple_instr COMMA"""
    p[0] = Case(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_default(p):
    """default : UNDERSCORE ARROW statement
    | UNDERSCORE ARROW simple_instr COMMA
    | empty"""
    if p[1] == "_":
        p[0] = Default(p.lineno(1), p.lexpos(1), p[3])
    else:
        p[0] = None


def p_match_expr(p):
    "match_expr : RMATCH expression LCBRACKET cases_expr default_expr RCBRACKET"
    p[0] = Match(p.lineno(1), p.lexpos(1), p[2], p[4], p[5])


def p_cases_expr(p):
    "cases_expr : cases_expr case_expr"
    p[1].append(p[2])
    p[0] = p[1]


def p_cases_case_expr(p):
    "cases_expr : case_expr"
    p[0] = [p[1]]


def p_case_expr(p):
    """case_expr : expressions_match ARROW expression COMMA
    | expressions_match ARROW LCBRACKET expression RCBRACKET
    | expressions_match ARROW LCBRACKET statement expression RCBRACKET"""
    if p[3] == "{":
        if isinstance(p[4], Statement):
            p[0] = CaseExpr(p.lineno(1), p.lexpos(1), p[1], p[4], p[5])
        else:
            p[0] = CaseExpr(p.lineno(1), p.lexpos(1), p[1], None, p[4])
    else:
        p[0] = CaseExpr(p.lineno(1), p.lexpos(1), p[1], None, p[3])


def p_default_expr(p):
    """default_expr : UNDERSCORE ARROW expression COMMA
    | UNDERSCORE ARROW LCBRACKET expression RCBRACKET
    | UNDERSCORE ARROW LCBRACKET statement expression RCBRACKET
    | empty"""
    if p[1] == "_":
        if p[3] == "{":
            if isinstance(p[4], Statement):
                p[0] = DefaultExpr(p.lineno(1), p.lexpos(1), None, p[4])
            else:
                p[0] = DefaultExpr(p.lineno(1), p.lexpos(1), p[4], p[5])
        else:
            p[0] = DefaultExpr(p.lineno(1), p.lexpos(1), None, p[3])
    else:
        p[0] = None


def p_while(p):
    "while : RWHILE expression statement"
    p[0] = While(p.lineno(1), p.lexpos(1), p[2], p[3])


def p_loop(p):
    "loop : RLOOP statement"
    p[0] = Loop(p.lineno(1), p.lexpos(1), p[2])


def p_break(p):
    "break : RBREAK"
    p[0] = Break(p.lineno(1), p.lexpos(1), None)


def p_break_2(p):
    "break : RBREAK expression"
    p[0] = Break(p.lineno(1), p.lexpos(1), p[2])


def p_continue(p):
    "continue : RCONTINUE"
    p[0] = Continue(p.lineno(1), p.lexpos(1))


def p_return(p):
    "return : RRETURN"
    p[0] = Return(p.lineno(1), p.lexpos(1), None)


def p_return_2(p):
    "return : RRETURN expression"
    p[0] = Return(p.lineno(1), p.lexpos(1), p[2])


def p_expressions(p):
    "expressions :  expressions COMMA expression"
    p[1].append(p[3])
    p[0] = p[1]


def p_expressions_expression(p):
    "expressions : expression"
    p[0] = [p[1]]


def p_expressions_match(p):
    "expressions_match :  expressions_match PIPE expression"
    p[1].append(p[3])
    p[0] = p[1]


def p_expressions_expression_match(p):
    "expressions_match : expression"
    p[0] = [p[1]]


def p_expression(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | expression MODULE expression"""
    col = p.lexpos(1)
    if p[2] == "+":
        p[0] = Arithmetic(p.lineno(1), col, p[1], p[3], ArithmeticType.Addition)
    elif p[2] == "-":
        p[0] = Arithmetic(p.lineno(1), col, p[1], p[3], ArithmeticType.Substraction)
    elif p[2] == "*":
        p[0] = Arithmetic(p.lineno(1), col, p[1], p[3], ArithmeticType.Multiplication)
    elif p[2] == "/":
        p[0] = Arithmetic(p.lineno(1), col, p[1], p[3], ArithmeticType.Division)
    else:
        p[0] = Arithmetic(p.lineno(1), col, p[1], p[3], ArithmeticType.Module)


def p_expr_power(p):
    """expression : RINT DCOLON POWER LPAREN expression COMMA expression RPAREN
    | RFLOAT DCOLON POWERF LPAREN expression COMMA expression RPAREN"""
    col = p.lexpos(1)
    if p[1] == "i64":
        p[0] = Arithmetic(p.lineno(1), col, p[5], p[7], ArithmeticType.Power, Type.Int)
    else:
        p[0] = Arithmetic(
            p.lineno(1), col, p[5], p[7], ArithmeticType.Power, Type.Float
        )


def p_expr_uminus(p):
    "expression : MINUS expression %prec UMINUS"
    left = Literal(p.lineno(1), p.lexpos(1), 1)
    p[0] = Arithmetic(p.lineno(1), p.lexpos(1), left, p[2], ArithmeticType.Negation)


def p_expr_par(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]


def p_expr_sqrt_abs(p):
    """expression : expression DOT SQRT LPAREN RPAREN
    | expression DOT ABS LPAREN RPAREN"""
    if p[3] == "sqrt":
        p[0] = Sqrt(p.lineno(1), p.lexpos(1), p[1])
    else:
        p[0] = Abs(p.lineno(1), p.lexpos(1), p[1])


def p_expr_clone(p):
    "expression : expression DOT CLONE LPAREN RPAREN"
    p[0] = Clone(p.lineno(1), p.lexpos(1), p[1])


def p_expr_logic(p):
    """expression : expression AND expression
    | expression OR expression
    | NOT expression %prec NOT"""
    if p[2] == "||":
        p[0] = Logic(p.lineno(1), p.lexpos(1), p[1], p[3], LogicType.Or)
    elif p[2] == "&&":
        p[0] = Logic(p.lineno(1), p.lexpos(1), p[1], p[3], LogicType.And)
    else:
        left = Literal(p.lineno(1), p.lexpos(1), False)
        p[0] = Logic(p.lineno(1), p.lexpos(1), left, p[2], LogicType.Not)


def p_expr_relational(p):
    """expression : expression EQUALS expression
    | expression NEQUALS expression
    | expression LTHAN expression
    | expression LORE expression
    | expression GTHAN expression
    | expression GORE expression"""
    col = p.lexpos(1)
    if p[2] == "==":
        p[0] = Relational(p.lineno(1), col, p[1], p[3], RelationalType.Equals)
    elif p[2] == "!=":
        p[0] = Relational(p.lineno(1), col, p[1], p[3], RelationalType.NotEquals)
    elif p[2] == "<":
        p[0] = Relational(p.lineno(1), col, p[1], p[3], RelationalType.Less)
    elif p[2] == "<=":
        p[0] = Relational(p.lineno(1), col, p[1], p[3], RelationalType.LessOrEqual)
    elif p[2] == ">":
        p[0] = Relational(p.lineno(1), col, p[1], p[3], RelationalType.Greater)
    else:
        p[0] = Relational(p.lineno(1), col, p[1], p[3], RelationalType.GreaterOrEqual)


def p_expr_cast(p):
    "expression : expression RAS primitive_type"
    p[0] = Cast(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_expr_tostr(p):
    """expression : expression DOT RTOSTRING LPAREN RPAREN
    | expression DOT RTOOWNED LPAREN RPAREN"""
    p[0] = ToString(p.lineno(1), p.lexpos(1), p[1])


def p_literal(p):
    """expression : INT
    | FLOAT
    | STRING
    | CHAR"""
    p[0] = Literal(p.lineno(1), p.lexpos(1), p[1])


def p_true(p):
    "expression : RTRUE"
    p[0] = Literal(p.lineno(1), p.lexpos(1), True)


def p_false(p):
    "expression : RFALSE"
    p[0] = Literal(p.lineno(1), p.lexpos(1), False)


def p_access(p):
    "expression : ID"
    p[0] = SimpleAccess(p.lineno(1), p.lexpos(1), p[1])


def p_access_array(p):
    "expression : expression LBRACKET expression RBRACKET"
    p[0] = ArrayAccess(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_create_array(p):
    """expression : LBRACKET expression SEMICOLON INT RBRACKET
    | LBRACKET expressions RBRACKET"""
    if isinstance(p[2], Expression):
        p[0] = CreateArray(p.lineno(1), p.lexpos(1), None, p[2], p[4])
    else:
        p[0] = CreateArray(p.lineno(1), p.lexpos(1), p[2], None, 0)


def p_expr_selection(p):
    """expression : if_expr
    | match_expr
    | loop"""
    p[0] = p[1]


def p_empty(p):
    "empty :"
    pass


def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()
