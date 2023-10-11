#include <stdio.h>
#include <math.h>

double entropy(int K, double *probabilities) {
    double H = 0;
    for (int i = 0; i < K; i++) {
        if (probabilities[i] > 0) {
            H -= probabilities[i] * log2(probabilities[i]);
        }
    }
    return H;
}

int main() {
    // Define the number of possible values K and their probabilities for variable X
    int K = 4;
    double probabilities_X[] = {0.2, 0.3, 0.2, 0.3};

    // Calculate H(X)
    double H_X = entropy(K, probabilities_X);

    // Define probabilities for 2X, X^2, and 2^X
    double probabilities_2X[] = {0.2, 0.3, 0.2, 0.3}; // Replace with the actual values
    double probabilities_X2[] = {0.1, 0.2, 0.1, 0.6}; // Replace with the actual values
    double probabilities_2X_X[] = {0.2, 0.3, 0.2, 0.3}; // Replace with the actual values

    // Calculate the entropies for each option
    double H_2X = entropy(K, probabilities_2X);
    double H_X2 = entropy(K, probabilities_X2);
    double H_2X_X = entropy(K, probabilities_2X_X);

    // Check the statements
    if (H_X <= log2(K)) {
        printf("A. H(X) <= log2(K) is true\n");
    }
    if (H_X <= H_2X) {
        printf("B. H(X) <= H(2X) is true\n");
    }
    if (H_X <= H_X2) {
        printf("C. H(X) <= H(X2) is true\n");
    }
    if (H_X <= H_2X_X) {
        printf("D. H(X) <= H(2^X) is true\n");
    }

    return 0;
}

