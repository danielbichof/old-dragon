

import typer
from InquirerPy import inquirer
from .character.generator import GeradorPersonagem

app = typer.Typer()

@app.command()
def gerar():
	"""Gera um personagem interativamente pelo CLI."""
	gerador = GeradorPersonagem()
	estilos = gerador.get_estilos()
	choices = [
		{"name": f"{num}. {estilo.get_nome_estilo()} - {estilo.get_descricao()}", "value": num}
		for num, estilo in estilos.items()
	]
	escolha = inquirer.select(
		message="Escolha o estilo de rolagem:",
		choices=choices,
		default=1,
	).execute()
	estilo = estilos[escolha]
	# Geração dos valores
	if hasattr(estilo, 'gerar_valores'):
		valores = estilo.gerar_valores()
	else:
		valores = None
	# Se for estilo clássico, não precisa distribuir
	if estilo.__class__.__name__ == 'EstiloClassico':
		atributos = estilo.gerar_atributos(valores=valores)
	else:
		nomes_atributos = [
			"Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"
		]
		print(f"Valores rolados: {valores}")
		distribuicao = []
		valores_disponiveis = valores.copy()
		for nome in nomes_atributos:
			escolha_valor = inquirer.select(
				message=f"Escolha o valor para {nome}:",
				choices=[str(v) for v in valores_disponiveis],
			).execute()
			valor_escolhido = int(escolha_valor)
			distribuicao.append(valor_escolhido)
			valores_disponiveis.remove(valor_escolhido)
		atributos = estilo.gerar_atributos(distribuicao=distribuicao, valores=valores)
	print("\n" + "=" * 50)
	print("PERSONAGEM GERADO COM SUCESSO!")
	print("=" * 50)
	print(atributos)
	d = atributos.get_atributos_dict()
	print(f"Soma total dos atributos: {sum(d.values())}")
	print(f"Maior atributo: {max(d.values())}")
	print(f"Menor atributo: {min(d.values())}")
	print(f"Média dos atributos: {sum(d.values())/6:.1f}")

if __name__ == "__main__":
	app()
