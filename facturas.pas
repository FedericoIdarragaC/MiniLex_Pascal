program Factura;
uses CRT;
type
  prodPrecs = record
    Producto: string;
	Precio: integer;
   end;


var
  num1,num2,num3,num4:integer;
 monto1,monto2,monto3,monto4:integer;
 subtotal,iva,total: real;

procedure dibujaCeldas(xi: integer; y: integer; xf: integer);
var
  i: integer;
 Begin
   (* Linea horizonatal arriba *)
   gotoxy(xi+1,y);
   for i:= xi to xf-2 do
     write(char(45));
   (* Linea horizonatal arriba *)
   gotoxy(xi,y+2);
   for i:= xi+1 to xf do
     write(char(45));

   (* Linea vertical izquierda *)
    for i:= y to y+2 do
     begin
       gotoxy(xi,i);
	   write(char(124));
     end;
    for i:= y to y+2 do
     begin
   (* Linea vertical derecha *)
       gotoxy(xf,i);
	   write(char(124));
     end;
    for i:= y to y+2 do
     begin
       gotoxy(60,i);
	   write(char(124));
     end;
 End;


BEGIN
  ClrScr;
     Begin
     ClrScr;
     textcolor(white);
  writeln('BIENVENIDO A LA TIENDA DE ABARROTES');

   Textcolor(29);
  writeln('F A C T U R A');

  Writeln(' ');
  writeln (' ');
  writeln('producto----------------------------precio');
  writeln('manzana.............................10');
  writeln('sandia..............................20');
  writeln('limon...............................8');
  writeln('papaya...............................25');
  writeln(' ');
  writeln(' ');
  writeln(' ');
  writeln( 'Inserte la cantidad de productos que desee comprar');
   (* Linea horizonatal arriba *)
   (* Linea vertical derecha *)
Textcolor(white);
  write('cantidad de manzanas:');readln(num1);
  write('cantidad de sandias:');readln(num2);
 write('cantidad de limones :');readln(num3);
 write('cantidad de papayas :');readln(num4);
 subtotal:=(num1)*(5)+(num2)*(10)+(num3)*(15)+(num4)*(20);
 writeln('.....................................');
 writeln('......................................');
 write('tu subtotal es--->:');write(subtotal:00:00);
 writeln('');
 total:=((subtotal)*(16)/(100))+(subtotal);
 writeln('............................................');
 writeln('cantidad producto precio');
 writeln('  ');                           write(num1);writeln(' manzana      10 ');
 writeln('  ');                           write(num2);writeln(' sandia       20  ');
 writeln('  ');                           write(num3);writeln('limon         8  ');
 writeln('  ');                           write(num4);writeln('papaya       25  ');
 writeln('............................................');
 writeln('el total incluyendo IVA es--->:',total:00:00);writeln('GRACIAS POR SU COMPRA');
 readkey;
 End;
 End.