# 🧪 Otimizador de Dados Clínicos – Análise Inicial
Este script em Python foi desenvolvido como uma iniciativa pessoal durante meu projeto de iniciação científica, com o objetivo de automatizar e otimizar o pré-processamento de dados clínicos coletados em planilhas Excel.

📌 Objetivo
A proposta deste código é automatizar a extração e categorização de informações importantes sobre participantes de um estudo clínico sobre o uso de paracetamol. O conjunto de dados original possui mais de 900 linhas, sendo cada paciente representado por múltiplas entradas. Antes de ser utilizado em análises mais complexas em ferramentas estatísticas ou scripts de visualização, este tratamento inicial ajuda a organizar e filtrar dados relevantes.

🧠 O que o script faz?
Para cada paciente, o script realiza as seguintes verificações e marcações:

-Redução da dor ao longo do monitoramento.

-Uso de paracetamol durante o período de análise.

-Classificação por faixa etária (jovem, adulto ou idoso).

-Estado civil (casado ou solteiro).

-Nível de escolaridade (primário, secundário ou nenhum).

-Emprego atual (empregado, dona de casa ou camponês).

-Zona de residência (urbana ou rural).

-Número de visitas de acompanhamento.

-Quantidade de partos realizados.

-Renda diária (> 1 USD ou ≤ 1 USD).

-Sexo do paciente.

-Peso do recém-nascido (> 3 kg).

-Se o organismo da mãe estava intacto após o parto.

-Se houve amamentação nas primeiras horas após o nascimento.

Os dados extraídos são copiados para uma nova planilha, já categorizados com marcações ('x') em colunas específicas, facilitando futuras análises.

🧰 Tecnologias Utilizadas
Python 3.x

Biblioteca openpyxl para leitura e escrita em arquivos .xlsx

📁 Arquivos
Coldpack_paracetamol Clinical Trial.xlsx: Planilha original com os dados brutos.

new_tabel.xlsx: Planilha de destino modelo, onde os dados são copiados e categorizados. (Apenas o esqueleto da planilha final)

new_tabel_editBy.xlsx: Arquivo gerado com os dados tratados após a execução do script.

📈 Resultados
Esse tratamento inicial reduziu consideravelmente o tempo necessário para categorizar e visualizar os dados brutos do estudo, tornando o processo de análise mais eficiente e confiável. Essa otimização servirá de base para etapas futuras da pesquisa, onde as informações serão integradas a outros scripts e softwares de análise estatística.

*para execução -> py main.py
