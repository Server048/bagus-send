from dhooks import Webhook, Embed

hook = Webhook("https://discord.com/api/webhooks/980121784298930247/4qaZGlBlXIRKEaBB6QDU2jC3yF23DFgaEwa6n11nGjPtaezScZZszeBqvyHV_6Kqtjbz")

embed = Embed(
description=`This is the **description** of the embed! :smiley:`,
color=0x5CDBF0,
timestamp=`now` # sets the timestamp to current time
)

image1 = `https://i.imgur.com/rdm3W9t.png`
image2 = `https://i.imgur.com/f1LOr4q.png`

embed.set_author(name=`Jackaldev`, con_url=image1)
embed.add_field(name=`this is the first option`, value=`vote for me! :joy:`)
embed.add_field(name=`This is the second option`, value=`No me! :smile:`)
embed.set_footer(text=`Who will you vote for!`, icon_url=image1)

embed.set_thumbnail(image1)
embed.set_image(image2)

hook.send(embed=embed)
