#include <stdio.h>
#include <math.h>

void pythagorean_theorum(char solve = 'c')
{
	struct Side
	{
		char letter;
		double value;
	};

	struct Side s1,s2,sx;
	sx.letter = 'c'; s1.letter = 'a'; s2.letter = 'b';
	
	switch(solve)
	{
		case 'a':
		sx.letter = 'a'; s1.letter = 'c'; s2.letter = 'b';
		break;
		case 'b':
		sx.letter = 'b'; s1.letter = 'c'; s2.letter = 'a';
		break;
		default:
		break;
	}

	printf("Pythagorean Theorem\n");
	printf("Enter numbers for %c and %c to solve for %c \n",s1.letter,s2.letter,sx.letter);

	printf("Value for %c: ",s1.letter);
	scanf("%lf",&s1.value);
	printf("Value for %c: ",s2.letter);
	scanf("%lf",&s2.value);

	s1.value = pow(s1.value, 2);
	s2.value = pow(s2.value, 2);
	sx.value = (sx.letter == 'c') ? sqrt(s1.value + s2.value) : sqrt(s1.value - s2.value);
	printf("Value %c = sqroot(%lf) = %lf\n",sx.letter,pow(sx.value,2),sx.value);
}