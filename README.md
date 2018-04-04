# Transliterace

Transliterace z cyrilice do latinky.

- Aplikace běží v prohlížeči (index.html).
- Je potřeba podpora javascriptu.
- Na serveru musí být python 3 (translit.cgi).

Skript lze spustit i z příkazové řádky, např.:

    QUERY_STRING=ru python3 translit.cgi <<< "плющенко"
