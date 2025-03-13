📊 Dashboard OTB (Open-to-Buy) - B2B & B2C
Este projeto implementa um painel interativo utilizando Streamlit, Faker e Pandas para simular e analisar o processo Open-to-Buy (OTB) em ambientes B2B e B2C.

📌 Funcionalidades
✅ Geração de dados fictícios para B2B e B2C
✅ Cálculo automático do OTB (Open-to-Buy)
✅ Visualização de métricas resumidas (Vendas Totais, Estoque Atual, Estoque Desejado, OTB Total)
✅ Gráficos interativos para análise de OTB por produto
✅ Controle personalizado do número de produtos via painel lateral
Objetivo: Gera um DataFrame com valores aleatórios para vendas, estoque atual e estoque desejado.
Diferenciação: A lógica adapta os valores de acordo com B2B (maior volume) e B2C (menor volume).
📊 3. Função para Calcular OTB
def calcular_otb(df):
    df['OTB'] = (df['Vendas'] + df['Estoque Desejado']) - df['Estoque Atual']
    return df
Calcula a métrica de Open-to-Buy e adiciona ao DataFrame.
🎛️ 4. Interface do Usuário
num_produtos_b2c = st.sidebar.slider("Número de Produtos B2C", 5, 50, 10)
num_produtos_b2b = st.sidebar.slider("Número de Produtos B2B", 5, 50, 10)
Personalização: Permite ajustar o número de produtos B2B e B2C pelo menu lateral.
📊 5. Exibição de Dados e Métricas
st.dataframe(df_otb)
Mostra uma tabela interativa com os dados gerados e calculados.
st.bar_chart(df_otb[df_otb['Tipo'] == tipo].set_index('Produto')['OTB'])
Cria um gráfico de barras dinâmico para cada tipo (B2B e B2C).
📈 Exemplo de Saída
Resumo Geral:

Vendas Totais
Estoque Atual
Estoque Desejado
OTB Total
Gráfico:

Visualização interativa do OTB por produto, dividido por B2B e B2C.
📌 Personalizações
Ajuste os valores de vendas, estoque ou fórmula de cálculo na função gerar_dados_vendas().
Modifique os gráficos usando st.line_chart, st.area_chart, etc.
Personalize os limites dos sliders de produtos na interface.
📄 Licença
Este projeto é de livre utilização e modificação.