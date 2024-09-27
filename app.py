import flet as ft

def main(page: ft.Page):
    # Função para calcular o IMC
    def calcular_imc(e):
        try:
            nome_usuario = nome.value
            peso_usuario = float(peso.value)
            altura_usuario = float(altura.value)
            imc = peso_usuario / (altura_usuario ** 2)
            classificacao = ""
            cor = ft.colors.BLACK  # Cor padrão
            mensagem = ""

            # Determinando a classificação, cor e mensagem
            if imc < 18.5:
                classificacao = "Abaixo do peso"
                cor = ft.colors.YELLOW
                mensagem = "Procurar um nutricionista para uma reeducação alimentar visando ao aumento da massa corporal."
            elif 18.5 <= imc < 24.9:
                classificacao = "Peso normal"
                cor = ft.colors.BLUE
                mensagem = "Parabéns!! Continue com a sua dieta."
            elif 25 <= imc < 29.9:
                classificacao = "Sobrepeso"
                cor = ft.colors.ORANGE
                mensagem = "Cuidado!!! Você precisa perder peso, antes que seja tarde!!."
            else:
                classificacao = "Obesidade"
                cor = ft.colors.RED
                mensagem = "A obesidade é uma doença que exige tratamento sério, se cuide!!!"

            # Atualizando os campos de resultado
            result.value = f"{nome_usuario}, seu IMC: {imc:.2f} - {classificacao}"
            result.color = cor  # Alterando a cor do texto
            mensagem_result.value = mensagem  # Exibindo a mensagem personalizada
        except ValueError:
            result.value = "Por favor, insira valores válidos para peso e altura."
            result.color = ft.colors.BLACK
            mensagem_result.value = ""  # Limpa a mensagem em caso de erro

        page.update()

    # Configurações da página
    page.title = "Calculadora de IMC"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de entrada
    nome = ft.TextField(label="Nome")
    peso = ft.TextField(label="Peso (kg)", suffix_text="kg", keyboard_type=ft.KeyboardType.NUMBER)
    altura = ft.TextField(label="Altura (m)", suffix_text="m", keyboard_type=ft.KeyboardType.NUMBER)
    result = ft.Text(size=30)
    mensagem_result = ft.Text(size=20, italic=True)  # Texto para exibir as mensagens

    # Layout da página
    page.add(
        ft.Row([ft.Text("Calculadora de IMC", size=40, weight="bold")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([nome], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([peso], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([altura], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("Calcular IMC", on_click=calcular_imc)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([result], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([mensagem_result], alignment=ft.MainAxisAlignment.CENTER)  # Mensagem personalizada
    )

    page.update()

ft.app(main)