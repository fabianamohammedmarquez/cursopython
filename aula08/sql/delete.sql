-- delete

use 4linux;

SELECT * FROM pessoa;

DELETE FROM pessoa
WHERE nacionalidade_pessoa = "Espanhola";

SELECT * FROM pessoa;
