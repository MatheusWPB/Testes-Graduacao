import java.util.Calendar;

public class SistemaAula {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//criação do objeto Pessoa
		Pessoa p1 = new Pessoa();
		Calendar dn = Calendar.getInstance();
		
		p1.editarIdade(15);
		p1.editarNome("Cleiton");
		p1.editarPeso(85);
		System.out.println(p1.nome);
		System.out.println(p1.idade);
		System.out.println(p1.peso);
		
		
		//p1- variável de instância(sem new)
		//ainda não possui lugar na memória
		dn.set(2003, 04, 16);
		Pessoa p2 = new Pessoa("Cleide",dn,60);
		//System.out.println(p2.idade);
		//System.out.println(p2.lerNome());
		//System.out.println(p2.lerPeso());
		p2.imprimir();
		dn.set(2001, 9, 26);
		
		Cliente c1 = new Cliente("Rafabeto","Av. Brasil,924", dn, 75 );
		c1.imprimir();
	
		

	}

}
