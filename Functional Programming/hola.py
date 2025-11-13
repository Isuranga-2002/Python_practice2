def translator(language):
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    # Inner function that translates a single word
    def translate_word(word):
        return translations[language].get(word, "unknown")

    # Return the inner function
    return translate_word


# 🎯 Testing the translator
translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello'))       # Output: hola
print(translate_to_spanish('thank you'))   # Output: gracias
print(translate_to_spanish('goodbye'))     # Output: adiós
print(translate_to_spanish('please'))      # Output: unknown

translate_to_french = translator('french')
print(translate_to_french('hello'))        # Output: bonjour

translate_to_italian = translator('italian')
print(translate_to_italian('goodbye'))     # Output: arrivederci

#Commented for a commit
