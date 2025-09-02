import pytest
from calculadora_financeira import calcular_diferenca_juros

@pytest.mark.parametrize("capital, juros, tempo, situacao_esperada",
                         [
                             (1000, 20.0, 2, 40),                
                             (8000, 20.0, 2, 320),                                        
                             (1000, 65.0, 2, 422.5)                                                                                                                                                             
                         ]
                    )

def test_verificar_diferenca_juros(capital, juros, tempo, situacao_esperada):

    resultado = calcular_diferenca_juros(capital, juros, tempo)

    assert resultado == situacao_esperada
