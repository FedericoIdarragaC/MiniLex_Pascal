program proyecto ;
uses crt;
  var opcion,x,c :integer;
  var n1,n2,suma,resta,multi,divi,porcent:double;
  begin
  clrscr;
  write('digite la cantidad de calculos a realizar: ');
  read(c);
      for x:=1 to c do
         begin
         writeln;
            writeln('seleccione una operacion:');
            writeln('   Suma:.......... 1');
            writeln('   Resta:......... 2');
            writeln('   Multiplicacion:.3');
            writeln('   Divicion:.......4');
            writeln('   Porcentaje:.....5');
            write('               OPERACION: ');
            read(opcion);

            case opcion of
            1 : begin ;
                  write('sumar:  ');
                  read(n1);
                  write('mas:  ');
                  read(n2);
                  suma:=(n1+n2) ;
                  writeln('El resultado de la suma es: ',suma:9:2);
                        end;

            2 : begin ;
                  write('restar:  ');
                  read(n1);
                  write('menos: ');
                  read(n2);
                  resta:=(n1-n2) ;
                  writeln('El resultado de la resta es: ',resta:9:2);
                          end;
            3 : begin ;
                   write('multiplicar:  ');
                  read(n1);
                  write('por: ');
                  read(n2);
                  multi:=(n1*n2) ;
                  writeln('El resultado de la multiplicacion es: ',multi:9:2);
                 end;

            4: begin ;
                   write('Dividir:  ');
                  read(n1);
                  write('entre: ');
                  read(n2);
                  multi:=(n1/n2) ;
                  writeln('El resultado de la divicion es: ',multi:9:2);
                 end ;

            5: begin ;
                   write('numero a buscar el porcentaje:  ');
                  read(n1);
                  write('digite el poscentaje: ');
                  read(n2);
                  porcent:=(n1*n2)/100 ;
                  writeln('El porciento de su numero es: ',porcent:9:2,'%');
                 end;

            else
                 writeln('no existe la opcion ..... ') ;
                writeln;
             end;

                end;
   writeln;
   readln;
   readln;
   clrscr;

end.