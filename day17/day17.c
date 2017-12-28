#include <stdio.h>

int main() {
	long long idx = 0;
	int y = 0;
	for (int x = 1; x < 50000001; ++x) {
		/* idx = ((idx + 337) % x) + 1*/
		idx += 337; 
		idx %= x;
		if (!(idx)) {
			y = x;
		}
		++idx;
	}
	printf("%d\n", y);
}
