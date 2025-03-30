# 3.3
CREATE TABLE dados_operadoras (
    "Registro_ANS" VARCHAR(6) NOT NULL,
    "CNPJ" VARCHAR(14) NOT NULL,
    "Razao_Social" VARCHAR(140) NOT NULL,
    "Nome_Fantasia" VARCHAR(140) NOT NULL,
    "Modalidade" VARCHAR(50) NOT NULL,
    "Logradouro" VARCHAR(40) NOT NULL,
    "Numero" VARCHAR(20) NOT NULL,
    "Complemento" VARCHAR(40) NOT NULL,
    "Bairro" VARCHAR(30) NOT NULL,
    "Cidade" VARCHAR(30) NOT NULL,
    "UF" VARCHAR(2) NOT NULL,
    "CEP" VARCHAR(8) NOT NULL,
    "DDD" VARCHAR(4) NOT NULL,
    "Telefone" VARCHAR(20) NOT NULL,
    "Fax" VARCHAR(20),
    "Endereco_eletronico" VARCHAR(225) NOT NULL,
    "Representante" VARCHAR(50) NOT NULL,
    "Cargo_Representante" VARCHAR(40) NOT NULL,
    "Regiao_de_Comercializacao" VARCHAR(1) NOT NULL,
    "Data_Registro_ANS" DATE NOT NULL
);

CREATE TABLE relatorios (
    "REG_ANS" VARCHAR(14) NOT NULL,
    "CD_CONTA_CONTABIL" VARCHAR(14) NOT NULL,   
    "DESCRICAO" VARCHAR(150) NOT NULL,   
    "VL_SALDO_INICIAL" NUMERIC(14,2) NOT NULL,   
    "VL_SALDO_FINAL" NUMERIC(14,2) NOT NULL,   
    "Data" DATE NOT NULL
);

# 3.4
# pelo o que pesquisei, isso deveria ser executado no console, no caso do Postgres, mas não consegui.
# Porém, consegui importar os dados via interface gráfica (usando o DBeaver)
COPY dados_operadoras (
    "Registro_ANS",
    "CNPJ",
    "Razao_Social",
    "Nome_Fantasia",
    "Modalidade",
    "Logradouro",
    "Numero",
    "Complemento",
    "Bairro",
    "Cidade",
    "UF",
    "CEP",
    "DDD",
    "Telefone",
    "Fax",
    "Endereco_eletronico",
    "Representante",
    "Cargo_Representante",
    "Regiao_de_Comercializacao",
    "Data_Registro_ANS"
)
FROM 'relatorio.csv'
DELIMITER ';'
CSV HEADER;

COPY relatorios (
    "REG_ANS",
    "CD_CONTA_CONTABIL",   
    "DESCRICAO",   
    "VL_SALDO_INICIAL",   
    "VL_SALDO_FINAL",   
    "Data"
)
FROM 'relatorio.csv'
DELIMITER ';'
CSV HEADER;