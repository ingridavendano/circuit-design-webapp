# -----------------------------------------------------------------------------
# Defined tokens and functions for digital logic expression using regex.
# -----------------------------------------------------------------------------
tokens = [
    # identifier
    'ID',
    # logic operatiors
    'NOT', 'NAND', 'AND', 'NOR', 'OR', 'NXOR', 'XOR',
    # assigments
    'EQUALS',
    # delimiters
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE',
    # binary numbers, integers, booleans
    'BIN', 'INT', 'TRUE', 'FALSE'
]

# -----------------------------------------------------------------------------

# identifier
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'


# logic operators
def t_NOT(t):
    r'([nN][oO][tT])|~|!'
    return t


def t_NAND(t):
    r'([nN][aA][nN][dD])'
    return t


def t_AND(t):
    r'([aA][nN][dD])|(\&{1,2})|\*'
    return t


def t_NOR(t):
    r'([nN][oO][rR])'
    return t


def t_OR(t):
    r'([oO][rR])|\|{1,2}|\+'
    return t


def t_NXOR(t):
    r'([nN][xX][oO][rR])'
    return t


def t_XOR(t):
    r'([xX][oO][rR])|\^'
    return t


# assignments
t_EQUALS = r'='

# delimiters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'


# binary
def t_BIN(t):
    r'(0b)[01^(2-9)]+'
    try:
        t.value = int(t.value, 2)
    except ValueError:
        print "Binary value %d is too large." % t.value
        t.value = int(0)
    return t


# integers
def t_INT(t):
    r'[0-9][0-9]*'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Integer value %d is too large." % t.value
        t.value = int(0)
    return t


# booleans
def t_TRUE(t):
    r'([tT][rR][uU][eE])'
    t.value = int(1)
    return t


def t_FALSE(t):
    r'([fF][aA][lL][sS][eE])'
    t.value = int(0)
    return t


# tokens to ignore
t_ignore = " \t"


# new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# tokens that have no type
def t_error(t):
    print "Illegal character '%s'!" % t.value[0]
    t.lexer.skip(1)


# -----------------------------------------------------------------------------
# Run PLY lex module that uses above functions to define tokens.
# -----------------------------------------------------------------------------
import ply.lex as lex
lexer = lex.lex()
