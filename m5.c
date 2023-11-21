#include <stdio.h>

double computePolynomial(double x) {
  return 3 * x * x * x * x * x + 2 * x * x * x * x - 5 * x * x * x - x * x + 7 * x - 6;
}

int main() {
  double x;

  // Prompt the user to enter a value for x
  printf("Enter a value for x: ");
  scanf("%lf", &x);

  // Compute the value of the polynomial
  double result = computePolynomial(x);

  // Display the result
  printf("The value of the polynomial for x = %.2f is %.2f\n", x, result);

  return 0;
}
