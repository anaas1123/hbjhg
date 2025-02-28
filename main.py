import flet as ft

def main(page: ft.Page):
    # App settings
    page.title = "Decimal to Binary Converter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # UI Components
    decimal_input = ft.TextField(
        label="Enter decimal number",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300,
        autofocus=True
    )
    
    result_text = ft.Text(value="", size=20)
    
    def convert_decimal(e):
        try:
            num = decimal_input.value.strip()
            if not num:
                raise ValueError("Empty input")
            
            decimal = float(num)
            
            if decimal < 0:
                raise ValueError("Negative number")
            if not decimal.is_integer():
                raise ValueError("Decimal number")
            
            binary = bin(int(decimal))[2:]
            result_text.value = f"Binary: {binary}"
            result_text.color = ft.colors.GREEN
            
        except ValueError as ve:
            result_text.value = f"Error: {str(ve).capitalize()}"
            result_text.color = ft.colors.RED
            
        except Exception:
            result_text.value = "Invalid input"
            result_text.color = ft.colors.RED
            
        finally:
            page.update()

    # Fixed icon references
    convert_btn = ft.ElevatedButton(
        "Convert to Binary",
        on_click=convert_decimal,
        icon=ft.icons.CALCULATE,  # This is actually still valid as an alias
        width=200
    )

    # Using a valid transform icon instead of non-existent CONVERT
    page.add(
        ft.Column(
            [
                ft.Icon(ft.icons.SYNC_ALT, size=40),  # Changed to sync icon
                ft.Text("Decimal to Binary", size=24, weight=ft.FontWeight.BOLD),
                decimal_input,
                convert_btn,
                result_text
            ],
            spacing=25,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
