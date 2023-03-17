#include "cgcustommath.h"
#include <iostream>

int main(int argc, char* argv[]) {

	if (argc == 3) {
		try {
			auto a = std::stoi(argv[1]);
			auto b = std::stoi(argv[2]);

			auto res = matrix(a, b);
			std::cout << "Result: " << std::endl;
			std::cout << res << std::endl;
			return 0;
		}
		catch (std::exception ex)
		{
			std::cout << "The given arguments should be integer." << std::endl;
		}
	}

	std::cout << "usage: mat <a> <b>" << std::endl;
	return -1;
}
