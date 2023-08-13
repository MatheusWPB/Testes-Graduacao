
import java.util.Calendar;

public class Pessoa {
	//Definição de atributos 
	String nome;
	//string - classe -> letra maiúscula 
	int idade;
	double peso;
	private Calendar dn;
	//Definição dos construtores
	public Pessoa() {
		
	}
	public Pessoa(String n, Calendar dn, double p) {
		this.nome = n;
		this.peso = p;
		this.setDn(dn);	
		int i;
		Calendar dh = Calendar.getInstance() ;
		i = dh.get(Calendar.YEAR) - dn.get(Calendar.YEAR);
		this.idade = i;
	
	}
	//Definição dos métodos
	public int calculaIdade(Calendar dn) {
		Calendar dh= Calendar.getInstance();
		int i = dh.get(Calendar.YEAR)- dn.get(Calendar.YEAR);
		if (dh.get(Calendar.MONTH < dn.get(Calendar.MONTH)))
			return i - 1;
		else
			if ((dh.get(Calendar.MONTH == dn.get(Calendar.MONTH))))
				if (dh.get(Calendar.DAY_OF_MONTH > dn.get(Calendar.DAY_OF_MONTH)))
					return i - 1;
				else
					this.idade = i;
			else
				return i;
	}
	
	public void editarNome(String novoNome) {
		this.nome = novoNome;
	}
	// void -> não retorna nenhum valor
	public String lerNome() {
		return this.nome;
	}
	public void editarIdade(int novaIdade) {
		this.idade= novaIdade;
	}
	public int lerIdade() {
		return this.idade;
		
	}
	public void editarPeso(double novoPeso) {
		this.peso = novoPeso;
		
	}
	public double lerPeso() {
		return this.peso;
		
	}
	public void imprimir() {
		System.out.println("Nome: " + this.nome);
		System.out.println("Idade: " + this.idade);
		System.out.println("Peso: " + this.peso);
		
	}
	public Calendar getDn() {
		return dn;
	}
	public void setDn(Calendar dn) {
		this.dn = dn;
	}

}
