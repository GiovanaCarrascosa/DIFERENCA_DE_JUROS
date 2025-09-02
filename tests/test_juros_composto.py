import pytest
from calculadora_financeira import calcular_juros_compostos

@pytest.mark.parametrize("capital, juros, tempo, situacao_esperada",
                         [
                             (1000.00, 20.0, 1.0, (200.0, 1200.00)),                
                             (500.00, 20.0, 2.0, (220.00, 720.00)),                                        
                             (800.00, 5.0, 2.0, (82.00, 882.00)),                                         
                             (4550.00, 100.0, 9.0, (2325050.00, 2329600.00)),                                         
                             (200.00, 0, 2.0, (0.0, 200.00)),                                         
                             (200.00, 20.0, 0, (0.0, 200.000)),                                         
                             (0, 20.0, 2.0, (0.0, 0.00))                                         
                                            
                         ]
                    )

def test_verificar_juros_compostos(capital, juros, tempo, situacao_esperada):

    resultado = calcular_juros_compostos(capital, juros, tempo)

    assert resultado == situacao_esperada

####################################################################################################################

# caso o valor da capital seja menor que 0 
def test_verificar_capital_menor_que_zero():

    #definindo a entrada
    capital = -15
    taxa_juros = 5
    tempo = 2
    
    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O capital investido não pode ser negativo."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor da taxa seja menor que 0 
def test_verificar_taxa_de_juros_menor_que_zero():

    #definindo a entrada
    capital = 15
    taxa_juros = -5
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "A taxa de juros não pode ser negativa."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor do tempo seja menor que 0 
def test_verificar_tempo_menor_que_zero():

    #definindo a entrada
    capital = 15
    taxa_juros = 5
    tempo = -2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O tempo não pode ser negativo."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

####################################################################################################################

# caso o valor da capital nao seja um int ou float
def test_verificar_se_o_valor_da_capital_for_uma_string_ao_inves_de_int_ou_float():

    #definindo a entrada
    capital = "ola"
    taxa_juros = 2
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(TypeError, match=r"O capital investido deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor da taxa nao seja um int ou float
def test_verificar_se_o_valor_da_taxa_de_juros_for_uma_string_ao_inves_de_int_ou_float():

    #definindo a entrada
    capital = 15
    taxa_juros = "ola"
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(TypeError, match = r"A taxa de juros deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor do tempo nao seja um int ou float
def test_verificar_se_o_valor_do_tempo_for_uma_string_ao_inves_de_int_ou_float():

    #definindo a entrada
    capital = 15
    taxa_juros = 2
    tempo = "ola"

    #executando a funcao e esperando erro
    with pytest.raises(TypeError, match = r"O tempo deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

####################################################################################################################

# caso o valor da capital nao tenha sido informado
def test_verificar_se_o_valor_da_capital__nao_foi_preenchida():

    #definindo a entrada
    taxa_juros = 2
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "Não é possível fazer a conta sem o valor da capital"):
        calcular_juros_compostos(None, taxa_juros, tempo)

# caso o valor da taxa nao tenha sido informado
def test_verificar_se_o_valor_da_taxa_juros_nao_foi_preenchida():

    #definindo a entrada
    capital = 20000
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "Não é possível fazer a conta sem o valor da taxa de juros"):
        calcular_juros_compostos(capital, None, tempo)

# caso o valor do tempo nao tenha sido informado
def test_verificar_se_o_valor_do_tempo_nao_foi_preenchido():

    #definindo a entrada
    capital = 2000
    taxa_juros = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "Não é possível fazer a conta sem o valor do tempo"):
        calcular_juros_compostos(capital, taxa_juros, None)
  
####################################################################################################################      
# caso NENHUM valor tenha sido informado
def test_verificar_se_a_tupla_estiver_vazia():

    #definindo a entrada
    
    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "Não é permitido uma tupla vazia."):
        calcular_juros_compostos(None, None, None)