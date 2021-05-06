#include "stuff.h"
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;

double pow(double base, long exp)
{
	double result = 1.0;
	long count;
	if(base == 0) return 0; // Zero Div and such
	if(exp < 0) // Neg
	{
		count = 1;
		while(--count > exp) result = result / base;
	}
	if(exp > 0) // Pos
	{
		count = -1;
		while(++count < exp)result = result * base;
	}
	return result;
}

void GenerateSecretCode(char * dest, char * str)
{
	//Validate - must be exactly 9 chars long and only a-z
	int len = strlen(str);
	for(unsigned char i = 0; i < len; i++)
	{
		if(str[i] < 0x61 || str[i] > 0x7a || len != 9)
		{
			cout<<"BANG! BANG! BANG!"<<endl;
			return;
		}
	}

	char p[3][20], s[3][20];

	//Part1 - first and last chars be alphabet num
	sprintf(s[0],"%d",str[0]-96);
	sprintf(s[1],"%c",str[1]);
	sprintf(s[2],"%d",str[2]-96);
	strcat(p[0],s[0]); strcat(p[0],s[1]); strcat(p[0],s[2]);

	//Part2 - swap first and last
	sprintf(s[0],"%c",str[5]);
	sprintf(s[1],"%c",str[4]);
	sprintf(s[2],"%c",str[3]);
	strcat(p[1],s[0]); strcat(p[1],s[1]); strcat(p[1],s[2]);

	//Part3 - increase each letter up one
	for(unsigned char i = 0; i < 3; i++)
	{
		sprintf(s[i],"%c",str[6+i]+1);
		if(s[i][0] == 0x7a)
			sprintf(s[i],"%c",0x61);
		strcat(p[2],s[i]);
	}

	//Final - p1+p2+p0
	strcat(dest,p[1]);
	strcat(dest,p[2]);
	strcat(dest,p[0]);
}

string MysteryFunc(unsigned long n)
{
	string num_string = to_string(n);
	string result;

	for(int i = 0; i < num_string.size();)
	{
		int instances = 1, next = 1;
		while(num_string[i] != '\0')
		{
			if(num_string[i+next] == num_string[i])
			{
				next++;
				instances++;
				continue;
			}
			else break;
		}
		result.append(to_string(instances)+num_string[i]);
		i += next;
	}
	return result;
}

bool IsPalindrome(string str)
{
	int size = str.size();
	string lower = "";
	string reversed = "";
	lower.resize(size);
	reversed.resize(size);
	transform(str.begin(),str.end(),lower.begin(),::tolower);
	reverse_copy(lower.begin(), lower.end(), reversed.begin());
	if(lower.compare(reversed)) return false;
	else return true;
}

unsigned char IsPalindrome(char * str)
{
	int size = 0;
	for(int i = 0; str[i] != '\0'; i++){size++;}

	char lower[size+1];
	char reversed[size+1];

	for(int i = 0; i < size; i++)
	{
		if(64<str[i] && str[i]<91) lower[i] = str[i]+32;
		else lower[i] = str[i];

		reversed[size-1-i] = lower[i];
	}
	for(int i = 0; i < size; i++)
		if(lower[i] != reversed[i]) return 0;

	return 1;
}

string ScaleTip(int* arr, int size)
{
	int left = 0, right = 0;
	int l_elems = 0, r_elems = 0;
	int i = -1;
	char toggle = 0;
	while(++i < size)
	{
		if(arr[i] == -1)
		{
			if(toggle == 1) return "Invalid";
			toggle = 1;
			continue;
		}
		if(toggle)
		{
			right += arr[i];
			r_elems += 1;
		}
		else
		{
			left += arr[i];
			l_elems += 1;
		}
	}
	if(l_elems != r_elems || !toggle) return "Invalid";
	if(left > right) return "Left";
	if(left < right) return "Right";
	return "Balanced";
}

void ShiftLetters(char * s, int size, int shifts)
{
	cout<<"Original: "<<s<<endl;
	while(shifts-- > 0)
	{
		for(int i = 0; i < size; i++)
		{
			if(s[i] > 0x40 && s[i] < 0x5b)
			{
				if(s[i] == 0x5a)
					s[i] = 0x41;
				else
					s[i] += 1;
			}
			if(s[i] > 0x60 && s[i] < 0x7b)
			{
				if(s[i] == 0x7a)
					s[i] = 0x61;
				else
					s[i] += 1;
			}
		}
	}
	cout<<"Result:   "<<s<<endl;
}