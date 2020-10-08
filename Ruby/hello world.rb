def say_hi(name)
    "Hello World, Hello " + name + " !!!"
end

puts say_hi("Edmar")
puts say_hi("Solfieri")

puts('test \n test')
puts("test \n test")

def hello(name)
    "Hello #{name.capitalize} !"
end

puts(hello("nora"))

x = [1,2,3,4,5,"Solfi", [1,2,3]]
puts(x[6], x[5])

x[7] = nil
puts(x.inspect)

equipamentos_veiculo = {
    'triangulo': 'obrigatorio',
    'chave_de_rodas': 'obrigatorio',
    'radio_bluetooth': 'opcional',
    'rodas_de_liga': 'nao_disponivel'
 }
 
p equipamentos_veiculo[:triangulo]
p equipamentos_veiculo[:chave_de_rodas]
p equipamentos_veiculo[:teto_solar]

class Pacient
    def initialize(name, blood_type)
      @name = name
      @blood_type = blood_type
    end
  
    def imprime_tag
      "Nome do paciente: #{@name} – Tipo Sanguíneo: #{@blood_type}"
    end
  end
  
  
  joao = Pacient.new("João da Silva", "O+")
  puts joao.imprime_tag
  
  num = 9
6.times do
  puts "#{num.class}: #{num}"
  num *= num
end

print <<-STRING1, <<-STRING2
       Concat
       STRING1
       enação
       STRING2