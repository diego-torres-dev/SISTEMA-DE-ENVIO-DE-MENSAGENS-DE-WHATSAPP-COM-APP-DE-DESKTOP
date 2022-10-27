# Sistema de Envio de Mensagens do WhatsApp com Aplicativo de Desktop

## Contexto

Este projeto apresenta uma aplicação de Desktop construída com
o Tkinter — uma biblioteca padrão do Python — que serve para enviar
mensagens no [WhatsApp](https://web.whatsapp.com/).

Para enviar mensagens para uma única conversa, usei este link:

```python
# Conversa para a qual vamos enviar uma mensagem
link = f"https://web.whatsapp.com/send?phone={telefone}&text={mensagem}"
```

Para evitar o processo de ter que escanear o QR Code do WhatsApp toda vez
que precisar usar este sistema, o código cria um perfil do Google Chrome e
especifica para o navegador que é criado pelo Selenium o caminho do diretório
deste perfil.

Assim, o usuário só precisa escanear o QR Code uma única vez. No entanto,
quando o navegador for fechado, o usuário não pode se desconectar de sua conta
— basta fechar o navegador.


## Bibliotecas Usadas

Neste projeto foram usadas as seguintes bibliotecas:

- os
- python-dotenv
- tkinter
- selenium
- webdriver-manager
- urllib

## Softwares Usados

Para criar a interface gráfica, usei o [Figma](https://www.figma.com/). Depois de finalizar
a arte no Figma, usei o [Proxlight Designer](https://proxlight.github.io/proxlightdesigner/)
para gerar o código que cria a janela.

## Captura da Tela do Sistema

Veja na imagem a seguir uma captura da tela do sistema:

![Captura de Tela do Sistema](./captura-de-tela-do-sistema.png)

