from dhooks import Webhook

hook = Webhook("https://discord.com/api/webhooks/980121784298930247/4qaZGlBlXIRKEaBB6QDU2jC3yF23DFgaEwa6n11nGjPtaezScZZszeBqvyHV_6Kqtjbz")

data = input("Enter Someting: ")

hook.send (data)
