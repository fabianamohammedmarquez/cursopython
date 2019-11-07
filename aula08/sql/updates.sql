use 4linux;

SELECT * FROM pessoa
WHERE id_pessoa = 1;

UPDATE pessoa
SET nome_pessoa = "Joaquim",
    nacionalidade_pessoa = "Portuguesa"
WHERE id_pessoa = 1; 


SELECT * FROM pessoa
WHERE id_pessoa = 1;
