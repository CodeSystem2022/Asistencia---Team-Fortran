
package pasoporReferencia;

import Clase.Persona;



public class PasoPorReferenia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que se realizo en el nombre es: " + persona1.nombre);
        persona1 = cambiarElValor(persona1);
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("El numero valor del objeto es: " + persona2.nombre);
    }
  public static void cambiarValor(Persona persona){
      persona.nombre = "Maria";
      
  }
  public static Persona cambiarElValor(Persona persona){
      
      if(persona == null){
          System.out.println("Valor de persona es invalido : Null");
          return null;
      }
      else{
          persona.nombre = "Monica";
          return persona;
      }
      
  }
}
