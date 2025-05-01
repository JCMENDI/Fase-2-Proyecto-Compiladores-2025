grammar MiCompilador;

programa: 'PROGRAM' ID ';' bloque '.';

bloque: declaraciones? compound_statement;

declaraciones: declaracion+;

declaracion
    : var_declaracion
    | funcion_declaracion
    ;

var_declaracion
    : 'VAR' ID ':' tipo ';' var_declaracion?
    ;

funcion_declaracion
    : 'FUNCTION' 'VOID' ID '(' lista_parametros? ')' ';' bloque
    | 'FUNCTION' tipo ID '(' lista_parametros? ')' ';' bloque
    ;

lista_parametros: parametro (',' parametro)*;

parametro: ID ':' tipo;

tipo: 'INTEGER' | 'REAL' | 'BOOLEAN' | 'STRING';

compound_statement: 'BEGIN' lista_sentencias? 'END';

lista_sentencias: sentencia (';' sentencia)* ';'?;

sentencia
    : asignacion
    | sentencia_if
    | sentencia_while
    | llamada_procedimiento
    | sentencia_io
	| compound_statement
	| sentencia_return
    ;
	
asignacion: ID ':=' expresion;

sentencia_if: 'IF' expresion 'THEN' sentencia ( 'ELSE' sentencia )?;

sentencia_while: 'WHILE' expresion 'DO' sentencia;

llamada_procedimiento: ID '(' lista_argumentos? ')';

lista_argumentos: expresion (',' expresion)*;

sentencia_return: 'RETURN' expresion ';';

sentencia_io
    : 'PRINTLN' '(' (STRING_CONST | ID | INT | FLOAT) ')'
    | 'READLN' '(' ID ')'
    ;

expresion: expresion_simple (operador_relacional expresion_simple)?;

expresion_simple
    : termino (operador_aditivo termino)*
    ;

termino
    : factor (operador_multiplicativo factor)*
    ;

factor
    : '(' expresion ')'
    | ID
	| llamada_procedimiento  
    | INT
    | FLOAT
    | booleano
    ;

booleano: 'TRUE' | 'FALSE';

operador_relacional: '=' | '<>' | '<' | '<=' | '>' | '>=';

operador_aditivo: '+' | '-' | 'OR';

operador_multiplicativo: '*' | '/' | 'AND';

STRING_CONST: '"' ( ~["\\] | '\\' . )* '"';

BOOL: 'TRUE' | 'FALSE';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;

INT: [0-9]+;

FLOAT: [0-9]+ '.' [0-9]+;

WS: [ \t\r\n]+ -> skip;