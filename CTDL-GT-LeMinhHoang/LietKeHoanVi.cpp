#include <iostream>
#include <vector>

using namespace std;

void swap(int& a, int& b) {
	int temp = a;
	a = b;
	b = temp;
}

void input(int& n) {
	cout << "\nNhap n: ";
	cin >> n;
}

void output(vector<int> a, int n) {
	for (int i = 0; i < n; i++) {
		cout << a[i];
	}
	cout << endl;
}

void init(vector<int>& a, int n) {

	for (int i = 0; i < n; i++) {
		a.push_back(i + 1);
	}
}

void process(vector <int> a, int n) {
	int i = n -2;
	while (i >= 0) {
		output(a, n);
		i = n - 2; //chay tu phan tu ke cuoi
		while (i >= 0 && a[i] > a[i + 1]) {  //neu ma phan tu truoc lon hon phan tu sau
			i--;//giam i cho den khi khong lon hon nua
		}
		if (i >= 0) {
			int k = n - 1;
			while (a[k] < a[i]) {//tim phan tu vua du lon hon a[i] hien tai
				k--;
			}
			swap(a[k], a[i]);
			int x = i + 1;    // doan nay la dao nguoc de cho doan giam dan
			int c = n - 1;
			while (x < c) {
				swap(a[x], a[c]);
				x++;
				c--;
			}
		}
		
	}
}

int main() {
	int n;
	vector <int> a;
	input(n);
	init(a, n);
	process(a, n);
	return 0;
}