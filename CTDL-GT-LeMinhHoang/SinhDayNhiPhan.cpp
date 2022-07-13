#include <iostream>
#include <vector>

using namespace std;

void output(vector <int> a, int n) {
	for (int i = 0; i < n; i++) {
		cout << a[i];
	}
	cout << endl;
}

void init(vector<int> &a, int& n) {
	
	do {
		cout << "Input n:\n";
		cin >> n;
		if (n <= 0) cout << "Invalid number!! Try again.";
	} while (n <= 0);
	for (int i = 0; i < n; i++) {
		a.push_back(0);
	}// khoi tao vector n so 0
}

bool check(vector <int> a, int n) { // ham nay de check dieu kien dung
	for (int i = 0; i < n; i++) {
		if (a[i] == 0) return false;
	}
	return true;
}

void binarySequence(vector <int> a, int n) {
	while (check(a, n) != true) { // chua thoa dieu kien dung thi tiep tuc lam
		output(a, n);
		if (a[n - 1] == 1) {  //neu phan tu cuoi day = 1
			int i = n - 1;
			while (a[i] == 1) { //set cac phan tu cuoi day = 0 cho den khi gap so 0 dau tien
				a[i] = 0;
				i--;
			}
			a[i] = 1;//sau khi gap so 0 dau tien thi cho no = 1
		}
		else {
			a[n - 1] = 1;
		}
	}
	output(a, n);//in ra day dieu dien dung
}
int main() {
	int n;
	vector<int>a; 
	init(a, n);
	binarySequence(a, n);
	return 0;
}