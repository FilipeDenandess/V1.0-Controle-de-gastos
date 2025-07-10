import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO = "gastos.json"
gastos = {}

#Função para carregar os dados do arquivo
def carregar_gastos():
    global gastos
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            gastos = json.load(f)
    else:
        gastos = {}

#Função para salvar os dados no arquivo
def salvar_gastos():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)

#Atualiza a lista e o total
def atualizar_lista():
    lista_gastos.delete(0, tk.END)
    total = 0
    for descricao, valor in gastos.items():
        lista_gastos.insert(tk.END, f"{descricao}: R${valor:.2f}")
        total += valor
    label_total.config(text=f"Total: R${total:.2f}")

#Adiciona novo gasto
def adicionar_gasto():
    descricao = entrada_descricao.get().strip()
    valor = entrada_valor.get().strip()
    
    if not descricao or not valor:
        messagebox.showwarning("Erro", "Preencha todos os campos.")
        return

    try:
        valor = float(valor)
        gastos[descricao] = valor
        salvar_gastos()
        atualizar_lista()
        entrada_descricao.delete(0, tk.END)
        entrada_valor.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico.")

#Remove gasto selecionado na lista
def remover_gasto():
    selecionado = lista_gastos.get(tk.ACTIVE)
    if not selecionado:
        messagebox.showinfo("Atenção", "Selecione um gasto para remover.")
        return

    descricao = selecionado.split(":")[0].strip()
    if descricao in gastos:
        del gastos[descricao]
        salvar_gastos()
        atualizar_lista()


root = tk.Tk()
root.title("Controle de Gastos")
root.geometry("400x500")

#Entrada
tk.Label(root, text="Descrição do gasto:").pack()
entrada_descricao = tk.Entry(root, width=40)
entrada_descricao.pack()

tk.Label(root, text="Valor do gasto:").pack()
entrada_valor = tk.Entry(root, width=20)
entrada_valor.pack()

#Botões
btn_adicionar = tk.Button(root, text="Adicionar Gasto", command=adicionar_gasto)
btn_adicionar.pack(pady=5)

btn_remover = tk.Button(root, text="Remover Gasto Selecionado", command=remover_gasto)
btn_remover.pack(pady=5)

#Lista gastos
lista_gastos = tk.Listbox(root, width=50)
lista_gastos.pack(pady=10)

# Total
label_total = tk.Label(root, text="Total: R$0.00", font=("Arial", 12, "bold"))
label_total.pack()


carregar_gastos()
atualizar_lista()

#Inicia o programa
root.mainloop()
