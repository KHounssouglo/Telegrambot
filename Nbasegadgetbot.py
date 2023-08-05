

token="6435974280:AAEYK2ZtblQqE2sm2WgGsp4X5pcO5fEP5AI"

from telegram.ext import updater ,messagehandler ,commandhandler ,filters

def start(uodate , context):

    update.message.reply_text("Bienvenue chez N-BASE!Je suis chargé de vous diriger vers nos produits et nos services. Merci")

    def gmail(update , context):

        update.message.reply_text("E-mail: ntassa koffi@gmail.com")

        def site(update , context):

            update.message.reply_text("https://")

            def incomprehension(update , context):

                update.message.reply_text("Désolé ,je n'ai pas compris ce que voulez. Veuillez essayer une autre commande.")

                def main():

                    updater=updater(token="6435974280:AAEYK2ZtblQqE2sm2WgGsp4X5pcO5fEP5AI" ,use_context=true)

                    dp=updater.dispatcher

                    dp.add_handler(commandhandler("start , start"))

                    dp.app_handler(commandhandler("site , site"))

                    dp.app_handler(commandhandler("incomprehension , incomprehension"))

                    dp.app_handler(messagehandler("filters.text , incomprehension"))

                    updater.start_polling()

                    updater.idle()

                    if_name_=="__main__"

                    main()



