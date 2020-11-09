program whldo;
begin 
   var counter : integer;
   var sum:integer;
   counter := 1;
   sum := 0;
   while counter <= 15 do
   
      sum := sum + counter;
      counter := counter + 1;
      
      writeln('sum =',sum);

 end. 