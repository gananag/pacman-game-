#include <stdint.h>

// Function to add two numbers
uint32_t add_numbers(uint32_t num1, uint32_t num2) {
    return num1 + num2;
}

int main(void) {
    uint32_t num1 = 10;  // First number
    uint32_t num2 = 20;  // Second number
    uint32_t result;     // Result of addition

    // Call the add_numbers function
    result = add_numbers(num1, num2);

    // Print the result (assuming a serial communication interface)
    // Replace this with your microcontroller's serial communication function
    printf("Result: %d\n", result);

    while (1);  // Infinite loop to prevent program termination
    return 0;
}

