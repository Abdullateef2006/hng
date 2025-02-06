from rest_framework import serializers
import requests

class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField()

    def validate_number(self, value):
        """Validate that the number is a positive integer."""
        if value < 0:
            raise serializers.ValidationError("Number must be a positive integer.")
        return value

    def get_number_properties(self, number):
        """Classify number properties."""
        is_prime = self.is_prime_number(number)
        is_perfect = self.is_perfect_number(number)
        digit_sum = sum(int(digit) for digit in str(number))
        properties = self.classify_properties(number)
        fun_fact = self.get_fun_fact(number)

        return {
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }

    def is_prime_number(self, n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect_number(self, n):
        """Check if a number is a perfect number."""
        return sum(i for i in range(1, n) if n % i == 0) == n

    def classify_properties(self, n):
        """Classify number properties."""
        properties = []
        if str(n) == str(n)[::-1]:
            properties.append("palindrome")
        if sum(int(digit) ** len(str(n)) for digit in str(n)) == n:
            properties.append("armstrong")
        if n % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
        return properties

    def get_fun_fact(self, n):
        """Fetch a fun fact about the number."""
        try:
            response = requests.get(f"http://numbersapi.com/{n}")
            if response.status_code == 200:
                return response.text
        except:
            pass
        return "No fun fact available."
