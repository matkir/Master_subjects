function f = oblig1lib_oppg2
    f.pad2D = @pad2D;
    f.convolve2D = @convolve2D;
    f.non_max_suppression = @non_max_suppression;
    f.hysteresis = @hysteresis;
end

function img_padded = pad2D(img,padlengths,padtype,cval)
    if (nargin < 3)
        padtype = 'constant';
        cval = 0;
    end
    
    pad_N = padlengths(1);
    pad_M = padlengths(2);

    half_pad_N = (pad_N-1)/2;
    half_pad_M = (pad_M-1)/2;

    [N,M] = size(img);

    %Sets values of the padded regions
    if(strcmp(padtype,'constant'))
        img_padded = ones(N+pad_N,M+pad_M);
        img_padded = cval.*img_padded;
    else
        img_padded = zeros(N+pad_N,M+pad_M);

        %--- Above img ---
        img_padded(1:half_pad_N,(half_pad_M+1):(M+half_pad_M)) = flipud(img(1:half_pad_N,:));
        %--- Under img ---
        img_padded((half_pad_N + N + 1):(pad_N+N),(half_pad_M + 1):(M + half_pad_M)) = flipud(img(((N-1)-half_pad_N)+1:N,:));

        %--- Left side to img ---
        img_padded((half_pad_N+1):(half_pad_N+N),1:half_pad_M) = fliplr(img(:,1:half_pad_M));

        %--- Right side to img ---
        img_padded((half_pad_N+1):(half_pad_N+N),(half_pad_M+M+1):(M+pad_M)) = fliplr(img(:,((M-1)-half_pad_M+1):M));

        %--- Corners ---
        %NW:
        img_padded(1:half_pad_N,1:half_pad_M) = rot90(img(1:half_pad_N,1:half_pad_M),2);

        %NE:
        img_padded(1:half_pad_N,(M+half_pad_M+1):(M+pad_M)) = rot90(img(1:half_pad_N,((M-1)-half_pad_M+1):M),2);

        %SW:
        img_padded((half_pad_N + N + 1):(N+pad_N),1:half_pad_M) = rot90(img(((N-1)-half_pad_N+1):N,1:half_pad_M),2);

        %SE:
        img_padded((half_pad_N + N + 1):(N+pad_N),(half_pad_M + M + 1):(pad_M+M)) = rot90(img(((N-1)-half_pad_N+1):N,((M-1)-half_pad_M+1):M),2);

    %Place the original image
    img_padded((half_pad_N+1):(N + half_pad_N),(half_pad_M+1):(M + half_pad_M)) = img;
    end
end

function img_convolved = convolve2D(img,h)
    img_padded = pad2D(img, size(h),'symmetric');
     
    [N,M] = size(h);
    [img_N, img_M] = size(img);
    img_convolved = zeros(img_N,img_M);

    h_rotated = rot90(h,2);

    for y = 1:img_N
        for x = 1:img_M 
            img_convolved(y,x) = sum(sum(img_padded(y:(N+y-1),x:(M+x-1)).*h_rotated));
        end
    end
end

function img_thinned = non_max_suppression(img_grad,img_direction)
    [N,M] = size(img_direction);

    img_thinned = zeros(N,M);
    for y = 2:(N-1) 
        for x = 2:(M-1) 
            degree = img_direction(y,x);
            a = 0; b = 0;

            if (degree == 0)
                a = img_grad(y-1,x);
                b = img_grad(y+1,x);
            elseif (degree == 45)
                a = img_grad(y+1,x+1);
                b = img_grad(y-1,x-1);
            elseif (degree == 135)
                a = img_grad(y-1,x+1);
                b = img_grad(y+1,x-1);
            else
                a = img_grad(y,x-1);
                b = img_grad(y,x+1);
            end

            if ( (img_grad(y,x) > a) && (img_grad(y,x) > b) )
                img_thinned(y,x) = img_grad(y,x);
            end
        end
    end
end

function  img_strong = hysteresis(img_thinned,tw,ts)
    [N,M] = size(img_thinned);

    img_strong = img_thinned(:,:);
    img_strong(img_thinned > ts) = 255;

    img_hyst = img_strong(:,:);
    marked = 1;
    while(marked > 0)
        marked = 0;
        for y = 2:N
            for x = 2:M 

                if (tw < img_strong(y,x) && img_strong(y,x) < ts)

                    %Using a 4-connected neighbourhood. Could also use 8-connected neighbourhood.
                    num_strong = sum(sum(img_strong((y-1):y,(x-1):x) == 255)); 
                    if (num_strong > 0)
                        img_hyst(y,x) = 255;
                        marked = marked+1;
                    end
                end
            end
        end

        img_strong = img_hyst(:,:);
    end
    
    %Get rid of weak edges
    img_strong(img_strong ~= 255) = 0;

end

 
