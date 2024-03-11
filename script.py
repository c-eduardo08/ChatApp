# Chat app - 
 # your name
 # your message

 # enter
 # chat, pop ups, enter in chat, send,   
# modal pop - screen center / format 
#sockts, wbsockts
import flet as ft

def main(pagina):
    texto = ft.Text("ChatD")
    
    chat = ft.Column()


    async def env_msg_tunel(mensagem):
     try:
        print(mensagem)
        # add mssg chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        #
        pagina.update()
     except Exception as e:
      print(f"Error w socket or {e}")

    pagina.pubsub.subscribe(env_msg_tunel)


    def enviar_mensagem(evento):
        print("enviar mensagem no chaat---")
        #               pagina.pubsub.send_all("--- testes ")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # add mssg
        
        # clean
        campo_mensagem.value = ""

        #updte 
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar mensagem", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])


    def entrar_chat(evento):
        print("entrar no chat...!")
        # close pop up / fechar pop up
        popup.open = False  
        # change the main page and the buttons
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        #add new f
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        #

        # 
            #pagina.add(campo_mensagem)
        #
            #pagina.add(botao_enviar)
        pagina.add(linha_enviar)



        # updte
        pagina.update()



    titulo_popup = ft.Text("Bem vindo ao ChatD")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(open=False,modal=True, 
                           title=titulo_popup, 
                           content=nome_usuario, 
                           actions=[botao_entrar] ) # content username, to fully the pop up

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER)
