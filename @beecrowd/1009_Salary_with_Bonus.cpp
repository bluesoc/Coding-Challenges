#include <iostream>
#include <iomanip>
#define PORCENTAGEM 15
using namespace std;

int main() {
	string name;
	double salario, venda, final;
	cin >> name >> salario >> venda;
	final = ((venda*PORCENTAGEM)/100) + salario;
	cout << "TOTAL = R$ " << fixed << setprecision(2) << final << endl;	
	return 0;
}
