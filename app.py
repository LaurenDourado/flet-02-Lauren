# app.py
import flet as ft
from imc_logic import calcular_imc, faixa_peso_ideal

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = "#fff6f0"

    texto_cor = "#f97316"   # laranja principal
    texto_claro = "#ffe0c2" # laranja claro

    def atualizar_cores():
        titulo.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        subtitulo.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        resultado.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        peso_ideal.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        page.update()

    def toggle_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = "#1f1b2e"
            tema_btn.icon = ft.Icons.LIGHT_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = "#fff6f0"
            tema_btn.icon = ft.Icons.DARK_MODE
        atualizar_cores()

    peso = ft.TextField(
        label="Peso (kg)",
        width=300,
        prefix_icon=ft.Icons.FITNESS_CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color=texto_cor,
    )
    altura = ft.TextField(
        label="Altura (m)",
        width=300,
        prefix_icon=ft.Icons.HEIGHT,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color=texto_cor,
    )

    resultado = ft.Text(size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color=texto_cor)
    peso_ideal = ft.Text(size=16, text_align=ft.TextAlign.CENTER, color=texto_cor)

    historico = ft.ListView(expand=False, spacing=5, padding=10, auto_scroll=True)

    def calcular_imc_click(e):
        try:
            p = float(peso.value.replace(",", "."))
            a = float(altura.value.replace(",", "."))
            imc, classificacao = calcular_imc(p, a)
            resultado.value = f"📊 Seu IMC é {imc:.2f} → {classificacao}"
            min_p, max_p = faixa_peso_ideal(a)
            peso_ideal.value = f"✅ Peso ideal entre {min_p:.1f}kg e {max_p:.1f}kg"
            historico.controls.append(ft.Text(f"IMC {imc:.2f} → {classificacao}", color=texto_cor, size=14))
        except ValueError as err:
            resultado.value = f"⚠️ {str(err)}"
            peso_ideal.value = ""
        except Exception:
            resultado.value = "⚠️ Preencha peso e altura corretamente!"
            peso_ideal.value = ""
        page.update()

    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = ""
        peso_ideal.value = ""
        page.update()

    def limpar_historico(e):
        historico.controls.clear()
        page.update()

    tema_btn = ft.IconButton(ft.Icons.DARK_MODE, on_click=toggle_tema, icon_color=texto_cor)

    btn_calcular = ft.ElevatedButton(
        content=ft.Row([ft.Text("Calcular IMC", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor=texto_cor, width=180, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)), on_click=calcular_imc_click
    )

    btn_limpar = ft.ElevatedButton(
        content=ft.Row([ft.Text("Limpar", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor="#d32f2f", width=150, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)), on_click=limpar
    )

    btn_limpar_hist = ft.TextButton("🗑️ Limpar histórico", on_click=limpar_historico, style=ft.ButtonStyle(color=texto_cor))

    titulo = ft.Text("Calculadora de IMC", size=24, weight=ft.FontWeight.BOLD, color=texto_cor, text_align=ft.TextAlign.CENTER)
    subtitulo = ft.Text("Informe seus dados", size=16, color=texto_cor, text_align=ft.TextAlign.CENTER)

    page.add(
        ft.Column(
            [
                # ft.Image(src="Senai.png", width=150, height=80),  # opcional
                ft.Row([titulo, tema_btn], alignment=ft.MainAxisAlignment.CENTER),
                subtitulo,
                peso,
                altura,
                ft.Row([btn_calcular, btn_limpar], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                resultado,
                peso_ideal,
                ft.Divider(),
                ft.Text("📜 Histórico de cálculos:", size=18, weight=ft.FontWeight.BOLD, color=texto_cor),
                historico,
                btn_limpar_hist,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
