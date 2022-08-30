import ply.yacc as yacc

from Analyzer.scanner import tokens
from Expression.Abs import Abs
from Expression.Arithmetic import Arithmetic
from Expression.ArrayAccess import ArrayAccess
from Expression.Capacity import Capacity
from Expression.Cast import Cast
from Expression.Clone import Clone
from Expression.Contains import Contains
from Expression.CreateArray import CreateArray
from Expression.CreateStruct import CreateStruct
from Expression.CreateVector import CreateVector
from Expression.Len import Len
from Expression.Literal import Literal
from Expression.Logic import Logic
from Expression.ModuleStruct import ModuleStruct
from Expression.Reference import Reference
from Expression.Relational import Relational
from Expression.Remove import Remove
from Expression.SimpleAccess import SimpleAccess
from Expression.Sqrt import Sqrt
from Expression.StructAccess import StructAccess
from Expression.ToString import ToString
from Instruction.Assignation import Assignation
from Instruction.Break import Break
from Instruction.Case import Case
from Instruction.Continue import Continue
from Instruction.Declaration import Declaration
from Instruction.Default import Default
from Instruction.For import For
from Instruction.FunctionDeclaration import FunctionDeclaration
from Instruction.FunctionCall import FunctionCall
from Instruction.If import If
from Instruction.Insert import Insert
from Instruction.Loop import Loop
from Instruction.Match import Match
from Instruction.ModDeclaration import ModDeclaration
from Instruction.ModuleCall import ModuleCall
from Instruction.NestedAssignation import NestedAssignation
from Instruction.NewStruct import NewStruct
from Instruction.Println import Println
from Instruction.Push import Push
from Instruction.Return import Return
from Instruction.Statement import Statement
from Instruction.While import While
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
    ("right", "UMINUS", "NOT", "AMPERSAND"),
    ("left", "DOT", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "DCOLON"),
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
    | for
    | struct_st
    | mod
    | push SEMICOLON
    | insert SEMICOLON
    | function_call SEMICOLON
    | break SEMICOLON
    | continue SEMICOLON
    | return SEMICOLON
    | function"""
    p[0] = p[1]


def p_simple_instr(p):
    """simple_instr : println
    | asignation
    | break
    | continue
    | return
    | push
    | insert"""
    p[0] = p[1]


def p_simple_instr_2(p):
    "simple_instr : empty"
    p[0] = None


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
    """array_type : LBRACKET primitive_type SEMICOLON INT RBRACKET
    | LBRACKET array_type SEMICOLON INT RBRACKET
    | LBRACKET ID SEMICOLON INT RBRACKET
    | LBRACKET vector_type SEMICOLON INT RBRACKET"""
    p[0] = {"type": p[2], "size": p[4]}


def p_array_type_2(p):
    "array_type : LBRACKET id_list SEMICOLON INT RBRACKET"
    t = "::".join(p[2])
    p[0] = {"type": t, "size": p[4]}


def p_vector_type(p):
    """vector_type : RVECTOR LTHAN primitive_type GTHAN
    | RVECTOR LTHAN ID GTHAN
    | RVECTOR LTHAN array_type GTHAN
    | RVECTOR LTHAN vector_type GTHAN"""
    p[0] = {"type": p[3]}


def p_vector_type_2(p):
    "vector_type : RVECTOR LTHAN id_list GTHAN"
    t = "::".join(p[3])
    p[0] = {"type": t}


def p_statement(p):
    "statement : LCBRACKET instructions simple_instr RCBRACKET"
    if p[2] is None:
        p[2] = []
    if p[3] is not None:
        p[2].append(p[3])
    p[0] = Statement(p.lineno(1), p.lexpos(1), p[2])


def p_statement_2(p):
    "statement : LCBRACKET simple_instr RCBRACKET"
    if p[2] is None:
        p[0] = Statement(p.lineno(1), p.lexpos(1), [])
    else:
        p[0] = Statement(p.lineno(1), p.lexpos(1), [p[2]])


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


def p_declaration_array_struct_mut(p):
    """declaration : RLET RMUT ID COLON array_type EQUAL expression
    | RLET RMUT ID COLON ID EQUAL expression
    | RLET RMUT ID COLON vector_type EQUAL expression"""
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[3], True, p[7], p[5])


def p_declaration_array_struct_mut_2(p):
    "declaration : RLET RMUT ID COLON id_list EQUAL expression"
    t = "::".join(p[5])
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[3], True, p[7], t)


def p_declaration_array_struct(p):
    """declaration : RLET ID COLON array_type EQUAL expression
    | RLET ID COLON ID EQUAL expression
    | RLET ID COLON vector_type EQUAL expression"""
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[2], False, p[6], p[4])


def p_declaration_array_struct_2(p):
    "declaration : RLET ID COLON id_list EQUAL expression"
    t = "::".join(p[4])
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[2], False, p[6], t)


def p_println(p):
    "println : RPRINT NOT LPAREN expressions RPAREN"
    p[0] = Println(p.lineno(1), p.lexpos(1), p[4])


def p_asignation(p):
    "asignation : ID EQUAL expression"
    p[0] = Assignation(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_nested_asignation(p):
    "asignation : nested_var EQUAL expression"
    p[0] = NestedAssignation(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_nested_var(p):
    """nested_var : nested_var DOT ID
    | nested_var LBRACKET expression RBRACKET"""
    p[1].append(p[3])
    p[0] = p[1]


def p_nested_var_id(p):
    """nested_var : ID DOT ID
    | ID LBRACKET expression RBRACKET"""
    p[0] = [p[1], p[3]]


def p_mod(p):
    """mod : RMOD ID statement
    | RPUB RMOD ID statement"""
    if p[1] == "pub":
        p[0] = ModDeclaration(p.lineno(1), p.lexpos(1), p[3], True, p[4])
    else:
        p[0] = ModDeclaration(p.lineno(1), p.lexpos(1), p[2], False, p[3])


def p_function(p):
    """function : RFN ID LPAREN RPAREN statement
    | RFN ID LPAREN args RPAREN statement"""
    if p[4] != ")":
        p[0] = FunctionDeclaration(
            p.lineno(1), p.lexpos(1), p[2], p[4], p[6], Type.Null
        )
    else:
        p[0] = FunctionDeclaration(p.lineno(1), p.lexpos(1), p[2], [], p[5], Type.Null)


def p_public_function(p):
    """function : RPUB RFN ID LPAREN RPAREN statement
    | RPUB RFN ID LPAREN args RPAREN statement"""
    if p[5] != ")":
        p[0] = FunctionDeclaration(
            p.lineno(1), p.lexpos(1), p[3], p[5], p[7], Type.Null, True
        )
    else:
        p[0] = FunctionDeclaration(
            p.lineno(1), p.lexpos(1), p[3], [], p[6], Type.Null, True
        )


def p_function_return(p):
    """function : RFN ID LPAREN RPAREN ARROW2 primitive_type statement
    | RFN ID LPAREN args RPAREN ARROW2 primitive_type statement
    | RFN ID LPAREN RPAREN ARROW2 array_type statement
    | RFN ID LPAREN args RPAREN ARROW2 array_type statement
    | RFN ID LPAREN RPAREN ARROW2 vector_type statement
    | RFN ID LPAREN args RPAREN ARROW2 vector_type statement
    | RFN ID LPAREN RPAREN ARROW2 ID statement
    | RFN ID LPAREN args RPAREN ARROW2 ID statement"""
    if p[4] != ")":
        p[0] = FunctionDeclaration(p.lineno(1), p.lexpos(1), p[2], p[4], p[8], p[7])
    else:
        p[0] = FunctionDeclaration(p.lineno(1), p.lexpos(1), p[2], [], p[7], p[6])


def p_public_function_return(p):
    """function : RPUB RFN ID LPAREN RPAREN ARROW2 primitive_type statement
    | RPUB RFN ID LPAREN args RPAREN ARROW2 primitive_type statement
    | RPUB RFN ID LPAREN RPAREN ARROW2 array_type statement
    | RPUB RFN ID LPAREN args RPAREN ARROW2 array_type statement
    | RPUB RFN ID LPAREN RPAREN ARROW2 vector_type statement
    | RPUB RFN ID LPAREN args RPAREN ARROW2 vector_type statement
    | RPUB RFN ID LPAREN RPAREN ARROW2 ID statement
    | RPUB RFN ID LPAREN args RPAREN ARROW2 ID statement"""
    if p[5] != ")":
        p[0] = FunctionDeclaration(
            p.lineno(1), p.lexpos(1), p[3], p[5], p[9], p[8], True
        )
    else:
        p[0] = FunctionDeclaration(p.lineno(1), p.lexpos(1), p[3], [], p[8], p[7], True)


def p_function_call(p):
    """function_call : ID LPAREN params RPAREN
    | ID LPAREN RPAREN"""
    if p[3] == ")":
        p[0] = FunctionCall(p.lineno(1), p.lexpos(1), p[1], [])
    else:
        p[0] = FunctionCall(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_function_call_2(p):
    """function_call : id_list LPAREN params RPAREN
    | id_list LPAREN RPAREN"""
    if p[3] == ")":
        p[0] = ModuleCall(p.lineno(1), p.lexpos(1), p[1], [])
    else:
        p[0] = ModuleCall(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_args_list(p):
    "args : args COMMA arg"
    p[1].append(p[3])
    p[0] = p[1]


def p_args_item(p):
    "args : arg"
    p[0] = [p[1]]


def p_arg(p):
    """arg : ID COLON primitive_type
    | ID COLON AMPERSAND RMUT array_type
    | ID COLON AMPERSAND RMUT vector_type
    | ID COLON AMPERSAND RMUT ID
    | ID COLON AMPERSAND RMUT LBRACKET primitive_type RBRACKET"""
    if p[3] == "&":
        if p[5] == "[":
            p[0] = {"name": p[1], "type": {"type": p[6], "size": -1}, "mut": True}
        else:
            p[0] = {"name": p[1], "type": p[5], "mut": True}
    else:
        p[0] = {"name": p[1], "type": p[3], "mut": False}


def p_arg_2(p):
    """arg : RMUT ID COLON array_type
    | RMUT ID COLON vector_type
    | RMUT ID COLON ID
    | RMUT ID COLON LBRACKET primitive_type RBRACKET
    | RMUT ID COLON AMPERSAND array_type
    | RMUT ID COLON AMPERSAND vector_type
    | RMUT ID COLON AMPERSAND ID
    | RMUT ID COLON AMPERSAND LBRACKET primitive_type RBRACKET"""
    if p[4] == "&":
        if p[5] == "[":
            p[0] = {"name": p[2], "type": {"type": p[6], "size": -1}, "mut": True}
        else:
            p[0] = {"name": p[2], "type": p[5], "mut": True}
    else:
        if p[4] == "[":
            p[0] = {"name": p[2], "type": {"type": p[5], "size": -1}, "mut": True}
        else:
            p[0] = {"name": p[2], "type": p[4], "mut": True}


def p_params_list(p):
    "params : params COMMA param"
    p[1].append(p[3])
    p[0] = p[1]


def p_params_item(p):
    "params : param"
    p[0] = [p[1]]


def p_param(p):
    """param : expression
    | AMPERSAND RMUT expression
    | AMPERSAND expression"""
    if p[1] == "&":
        if p[2] == "mut":
            p[0] = {"value": p[3], "mut": True}
        else:
            p[0] = {"value": p[2], "mut": False}
    else:
        p[0] = {"value": p[1], "mut": False}


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


def p_while(p):
    "while : RWHILE expression statement"
    p[0] = While(p.lineno(1), p.lexpos(1), p[2], p[3])


def p_loop(p):
    "loop : RLOOP statement"
    p[0] = Loop(p.lineno(1), p.lexpos(1), p[2])


def p_for_range(p):
    """for : RFOR ID RIN expression DOT DOT expression statement
    | RFOR ID RIN expression statement"""
    if p[5] == ".":
        p[0] = For(p.lineno(1), p.lexpos(1), p[2], p[4], p[7], p[8])
    else:
        p[0] = For(p.lineno(1), p.lexpos(1), p[2], p[4], None, p[5])


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
    """return : RRETURN expression
    | expression"""
    if p[1] == "return":
        p[0] = Return(p.lineno(1), p.lexpos(1), p[2])
    else:
        p[0] = Return(p.lineno(1), p.lexpos(1), p[1])


def p_push(p):
    "push : ID DOT RPUSH LPAREN expression RPAREN"
    p[0] = Push(p.lineno(1), p.lexpos(1), p[1], None, p[5])


def p_insert(p):
    "insert : ID DOT RINSERT LPAREN expression COMMA expression RPAREN"
    p[0] = Insert(p.lineno(1), p.lexpos(1), p[1], None, p[7], p[5])


def p_expressions(p):
    "expressions :  expressions COMMA expression"
    p[1].append(p[3])
    p[0] = p[1]


def p_expressions_expression(p):
    "expressions : expression"
    p[0] = [p[1]]


def p_expressions_match(p):
    "expressions_match : expressions_match PIPE expression"
    p[1].append(p[3])
    p[0] = p[1]


def p_expressions_expression_match(p):
    "expressions_match : expression"
    p[0] = [p[1]]


def p_struct_st(p):
    """struct_st : RSTRUCT ID LCBRACKET items_2 RCBRACKET
    | RSTRUCT ID LCBRACKET items_2 COMMA RCBRACKET"""
    p[0] = NewStruct(p.lineno(1), p.lexpos(1), p[2], p[4])


def p_public_struct_st(p):
    """struct_st : RPUB RSTRUCT ID LCBRACKET items_2 RCBRACKET
    | RPUB RSTRUCT ID LCBRACKET items_2 COMMA RCBRACKET"""
    p[0] = NewStruct(p.lineno(1), p.lexpos(1), p[3], p[5], True)


def p_items(p):
    "items : items COMMA item"
    p[0] = p[1]
    p[0][p[3]["id"]] = p[3]["value"]


def p_items_item(p):
    "items : item"
    p[0] = dict()
    p[0][p[1]["id"]] = p[1]["value"]


def p_item(p):
    "item : ID COLON expression"
    p[0] = {"id": p[1], "value": p[3]}


def p_items_2(p):
    "items_2 : items_2 COMMA item_2"
    p[0] = p[1]
    p[0][p[3]["id"]] = p[3]["type"]


def p_items_2_item_2(p):
    "items_2 : item_2"
    p[0] = dict()
    p[0][p[1]["id"]] = p[1]["type"]


def p_item_2(p):
    """item_2 : ID COLON primitive_type
    | ID COLON array_type
    | ID COLON ID
    | ID COLON vector_type"""
    p[0] = {"id": p[1], "type": p[3]}


def p_item_2_pub(p):
    """item_2 : RPUB ID COLON primitive_type
    | RPUB ID COLON array_type
    | RPUB ID COLON ID
    | RPUB ID COLON vector_type"""
    p[0] = {"id": p[2], "type": p[4]}


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
    | NOT expression"""
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


def p_reference(p):
    "expression : AMPERSAND expression"
    p[0] = Reference(p.lineno(1), p.lexpos(1), p[2])


def p_access(p):
    "expression : ID"
    p[0] = SimpleAccess(p.lineno(1), p.lexpos(1), p[1])


def p_expr_struct(p):
    """expression : ID LCBRACKET items RCBRACKET
    | ID LCBRACKET items COMMA RCBRACKET"""
    p[0] = CreateStruct(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_expr_struct_2(p):
    """expression : id_list LCBRACKET items RCBRACKET
    | id_list LCBRACKET items COMMA RCBRACKET"""
    p[0] = ModuleStruct(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_access_array(p):
    "expression : expression LBRACKET expression RBRACKET"
    p[0] = ArrayAccess(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_access_struct(p):
    "expression : expression DOT ID"
    p[0] = StructAccess(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_create_array(p):
    """expression : LBRACKET expression SEMICOLON INT RBRACKET
    | LBRACKET expressions RBRACKET"""
    if isinstance(p[2], Expression):
        p[0] = CreateArray(p.lineno(1), p.lexpos(1), None, p[2], p[4])
    else:
        p[0] = CreateArray(p.lineno(1), p.lexpos(1), p[2], None, 0)


def p_create_vector(p):
    """expression : RVEC NOT LBRACKET expression SEMICOLON expression RBRACKET
    | RVEC NOT LBRACKET expressions RBRACKET"""
    if isinstance(p[4], Expression):
        p[0] = CreateVector(p.lineno(1), p.lexpos(1), None, p[4], p[6], False)
    else:
        p[0] = CreateVector(p.lineno(1), p.lexpos(1), p[4], None, 0, False)


def p_create_vector_2(p):
    """expression : RVECTOR DCOLON RNEW LPAREN RPAREN
    | RVECTOR DCOLON RWITH_CAPACITY LPAREN expression RPAREN"""
    if p[3] == "new":
        p[0] = CreateVector(p.lineno(1), p.lexpos(1), None, None, None, True)
    else:
        p[0] = CreateVector(p.lineno(1), p.lexpos(1), None, None, p[5], False)


def p_exprs_vector(p):
    """expression : expression DOT RLEN LPAREN RPAREN
    | expression DOT RCAPACITY LPAREN RPAREN
    | expression DOT RREMOVE LPAREN expression RPAREN
    | expression DOT RCONTAINS LPAREN expression RPAREN"""
    if p[3] == "len":
        p[0] = Len(p.lineno(1), p.lexpos(1), p[1])
    elif p[3] == "capacity":
        p[0] = Capacity(p.lineno(1), p.lexpos(1), p[1])
    elif p[3] == "remove":
        p[0] = Remove(p.lineno(1), p.lexpos(1), p[1], p[5])
    else:
        p[0] = Contains(p.lineno(1), p.lexpos(1), p[1], p[5])


def p_expr_function(p):
    """expression : ID LPAREN params RPAREN
    | ID LPAREN RPAREN"""
    if p[3] == ")":
        p[0] = FunctionCall(p.lineno(1), p.lexpos(1), p[1], [])
    else:
        p[0] = FunctionCall(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_id_list(p):
    "id_list : id_list DCOLON ID"
    p[1].append(p[3])
    p[0] = p[1]


def p_id_list_2(p):
    "id_list : ID DCOLON ID"
    p[0] = [p[1], p[3]]


def p_expr_module_access(p):
    """expression : id_list LPAREN RPAREN
    | id_list LPAREN params RPAREN"""
    if p[3] == ")":
        p[0] = ModuleCall(p.lineno(1), p.lexpos(1), p[1], [])
    else:
        p[0] = ModuleCall(p.lineno(1), p.lexpos(1), p[1], p[3])


def p_expr_selection(p):
    """expression : ifst
    | match
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
