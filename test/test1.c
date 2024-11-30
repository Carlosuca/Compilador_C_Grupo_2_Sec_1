// Función para sumar dos números
int sumar(int a, int b) {
    return a + b;
}

// Función para restar dos números
int restar(int a, int b) {
    return a - b;
}

// Función para multiplicar dos números
int multiplicar(int a, int b) {
    return a * b;
}

// Función para dividir dos números
float dividir(int a, int b) {
    if (b == 0) {
        return 0;  // Devuelve 0 como valor de error
    } else {
        printf('d');
        return a / b;
    }
}

int main() {
    int num1, num2, num3;
    char operacion;
    char operaciones = 'x';
    
    operaciones = 'D';


    scanf('d', num1);

    printf('R');
    scanf('d', num2);

    printf('R');
    scanf('c', operacion);

    for (int i = 0; i == 4; i+1) {
        if (operacion == 'x') {
            if (operacion == '+') {
                printf('R', sumar(num1, num2));
            } else if (num1) {
                printf('R', dividir(num1, num2));
            } 
            
            if (num2) {
                printf('R', dividir(num1, num2));
            } 
        }
    }

    return 0;
}
