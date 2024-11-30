# Documentación del Analizador Sintáctico

Este repositorio contiene el desarrollo de un compilador modular para el lenguaje de programación C. Fue creado como parte del curso de **Teoría de Lenguajes de Programación** en la **Universidad Centroamericana "José Simeón Cañas"**. El objetivo principal es implementar un sistema que permita analizar y validar código fuente mediante procesos de análisis léxico, sintáctico y semántico, asegurando así la calidad del código generado y optimizando el desarrollo.

## Componentes del Compilador

El compilador cuenta con tres componentes principales:

1. **Analizador Léxico**  
   Implementado en el archivo `c_lexer.py`, se encarga de identificar los tokens del código fuente, como identificadores, operadores, delimitadores y constantes. También detecta errores léxicos y maneja elementos como comentarios y cadenas de texto.

2. **Parser (Analizador Sintáctico)**  
   Implementado en el archivo `c_parser.py`, utiliza las reglas gramaticales del lenguaje C para construir un árbol sintáctico, validando la estructura lógica del código y gestionando errores de sintaxis.

3. **Analizador Semántico**  
   Contenido en `c_semantic.py`, realiza verificaciones como la correcta declaración y uso de variables, la compatibilidad de tipos y genera advertencias para optimización del código.

## Propósito

El propósito de este compilador es múltiple:
- Traducir el código fuente a una estructura ejecutable, asegurando que cumpla con las reglas del lenguaje C.
- Validar el código en tres niveles: léxico, sintáctico y semántico.
- Identificar errores y generar advertencias que faciliten la depuración.
- Ofrecer a los desarrolladores una herramienta para producir código más robusto y eficiente.

## Flujo de Trabajo

El flujo de trabajo del compilador incluye tres pasos principales:

1. **Análisis Léxico**:  
   El código fuente se descompone en tokens significativos, detectando errores básicos y preparando los datos para las siguientes fases.

2. **Análisis Sintáctico**:  
   El parser construye un árbol sintáctico que representa la estructura jerárquica del programa, validando las reglas gramaticales y reportando errores de sintaxis.

3. **Análisis Semántico**:  
   Se asegura la coherencia lógica del programa, verificando aspectos como la declaración de variables y la compatibilidad de tipos.

## Ejemplo de Ejecución

Un ejemplo sencillo del funcionamiento del compilador sería el siguiente:

### Entrada
```c
int x = 10;
y = x + 3;
```
## Resultados

- **Tokens**: `int`, `x`, `=`, `10`, `;`, `y`, `=`, `x`, `+`, `3`, `;`.
- **Árbol Sintáctico**: Una representación jerárquica que organiza los elementos del código según las reglas del lenguaje.
- **Error Semántico**: `"Variable 'y' usada pero nunca declarada"`.

El compilador detecta que la variable `y` no ha sido declarada antes de su uso, lo que representa un error crítico.

## Conclusión

La estructura modular y escalable del compilador permite adaptarlo a nuevas necesidades y lenguajes de programación. Además, integra validaciones detalladas que garantizan código válido y estructurado. Al detectar y resolver errores comunes, optimiza el desarrollo y mejora la calidad del código generado, convirtiéndolo en una herramienta eficaz tanto para aprendizaje como para desarrollo profesional.

## Créditos

El proyecto fue desarrollado por los siguientes integrantes:

- **Andrés Emilio Puente Cruz  00287919**  
- **Oscar Alexander Juarez Gonzalez  00126320**  
- **Víctor Rafael Valenzuela Cortez  00022120**  
- **Carlos Misael Perez Perez  00202118**  
- **Xavier Alessandro Quiñonez del Cid  00048219**  
- **Mario Ernesto Mayen Castro  00220618**  

**Catedrático**: Ing. Jaime Roberto Climaco  
**Materia**: Teoría de Lenguaje de Programación - Sección 1  
