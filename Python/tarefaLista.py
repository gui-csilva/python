response = {
	"2": 0,
	"3": 0,
	"4": 0,
	"5": 0,
	"6": 0,
	"7": 0,
	"8": 0,
	"9": 0,
	"0": 0,
}
percentual = 0.09
salario = 200

exemplo = [
	{
		"vendas":2000
	},
	{
		"vendas":3000
	},
	{
		"vendas":4000
	},
	{
		"vendas":5000
	},
	{
		"vendas":6000
	},
	{
		"vendas":7000
	},
	{
		"vendas":8000
	},
		{
		"vendas":9000
	},
	{
		"vendas":2000
	},
	{
		"vendas":3000
	},
	{
		"vendas":4000
	},
	{
		"vendas":9000
	},
]

for value in exemplo:
    comissao = value["vendas"] * percentual
    salarioFinal = salario + comissao
    salarioFinal = int(salarioFinal)
    salarioFinal = str(salarioFinal)
    if len(salarioFinal) < 3:
        response["2"] += 1
    elif len(salarioFinal) > 3:
        response["0"] += 1
    else:
        pedigiti = salarioFinal[0]
        response[pedigiti] += 1

for value in response:
    print(value, ":", response[value])
