import java.util.Calendar;

public class Cliente extends Pessoa{
	//Cliente -> classe filho  e Pessoa -> classe pai (herança)
	//atributos
	String endereco;
	//Métodos getters/ler e setters/editar
	//Construtor cliente
	public Cliente(String n, String e, Calendar dn, double p) {
		super (n,dn,p);
		this.endereco = e;
		
	}
	

	public String getEndereço() {
		return endereco;
	}

	public void setEndereço(String nendereco) {
		this.endereco = nendereco;
	}
	public void imprimir() {
		super.imprimir();
		System.out.println("Endeeço: " + this.endereco);
	}
	//construtores 

	//métodos
	

}
