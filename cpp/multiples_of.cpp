// The famous 'Multiples of 3 and 5' problem from Project Euler. It can be expanded to include numbers other than 3 and 5 if you want - along with a setable max number. Such lovely printing, too.

#include <iostream>
#include <vector>

std::vector<int> GetMultiples(int number, int max)
{
	std::vector<int> num_list;
	if (max < number)
		return num_list;
	for (int i = number; i <= max; i++)
	{
		if (i % number == 0)
			num_list.push_back(i);
	}
	return num_list;
}

void PrintVectorInt(std::vector<int> vec)
{
	for (int i = 0; i < vec.size(); i++)
		std::cout << vec[i] << ' ';
}

int SumVectorInt(std::vector<int> vec)
{
	int total = 0;
	for (int i = 0; i < vec.size(); i++)
		total += vec[i];
	return total;
}

void MultiplesOf()
{
	int nums[] = {3, 5};
	int max_iters = 999;
	int sum = 0;
	std::cout << "Multiples of numbers up to: " << max_iters << "\n\n";
	for (int i = 0; i < sizeof(nums) / sizeof(nums[0]); i++)
	{
		std::cout << "Multiples of " << nums[i] << ": " << std::endl;
		std::vector<int> multiples = GetMultiples(nums[i], max_iters);
		sum += SumVectorInt(multiples);
		PrintVectorInt(multiples);
		std::cout << "\n\n";
	}
	std::cout << "Total sum of multiples = " << sum << std::endl;
}