%{
#include "parser.tab.h"              // Inclusión del archivo de encabezado generado por Bison
#include <string.h>                  // Para funciones de manipulación de cadenas
#include <stdlib.h>                  // Para funciones de asignación dinámica
%}

%%
"int"                   { return INT; }                                  // Reconoce la palabra clave "int"
[a-zA-Z_][a-zA-Z0-9_]*  { yylval.str = strdup(yytext); return ID; }      // Captura identificadores
"="                     { return IGUAL; }                                // Reconoce el signo igual
";"                     { return PUNTOYCOMA; }                           // Reconoce punto y coma
[ \t\n]+                ;                                                 // Ignora espacios y saltos
.                       { return yytext[0]; }                            // Cualquier otro carácter
%%

