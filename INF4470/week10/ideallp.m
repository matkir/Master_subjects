function F = ideallp(wc,N); 
 t = (N-1)/2;              
 x = [0: (N-1)];             
 m = x - t + eps;	        
 F = sin(wc*m) ./ (pi*m);   
end

