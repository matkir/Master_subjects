function f = oblig1lib_oppg1
    f.standarize_contrast = @standarize_contrast;
    f.forward_map = @forward_map;
    f.backward_map = @backward_map;
    f.from0to255 = @from0to255;
end

function img_within_range = from0to255(img)
    img_within_range =  ((img - min(img(:))).*255)./(max(img(:)) - min(img(:)));
end

function standarized_img = standarize_contrast(img,mean,sigma)
    [N,M] = size(img);
    mean_img = sum(img(:))/(N*M);
    sigma_img = sqrt(sum((img(:)-mean_img).^2)/(N*M));
    standarized_img = mean + (img-mean_img).*(sigma/sigma_img);
end

function img_forward_mapped = forward_map(sizes_old,sizes_new,img,transform_matrix)
    N_old = sizes_old(1); M_old = sizes_old(2);
    N_new = sizes_new(1); M_new = sizes_new(2);
    
    img_forward_mapped = zeros(N_new,M_new);
    for y = 1:N_old
        for x = 1:M_old
            new_coord = transform_matrix*[x;y;1];

            %Alternatively, one could write out the explicit result after 
            %matrix multiplication which can be found in slide 5 
            %about geometric operations

            x_ = round(new_coord(1));
            y_ = round(new_coord(2));
            if ((1 <= x_ && x_ <= M_new) && (1 <= y_ && y_ <= N_new))
                img_forward_mapped(y_,x_) = img(y,x);
            end
        end
    end
end

function img_backward_mapped = backward_map(sizes_old,sizes_new,img,tranform_matrix,interpolation)
    if nargin < 5
        interpolation = 'nearest neighbour';
    end
    N_old = sizes_old(1); M_old = sizes_old(2);
    N_new = sizes_new(1); M_new = sizes_new(2);
    
    inv_transform_matrix = inv(tranform_matrix);
    img_backward_mapped = zeros(N_new,M_new);
    for y_ = 1:N_new
        for x_ = 1:M_new

            new_coord = inv_transform_matrix*[x_;y_;1];

            %Alternatively, one could calculate how to find the coordinates (y,x) as functions of (y_,x_).
            %By some rearranging of the equations we get
            %y = (a0*y_ - b0*x_ + a2*b0 - a0*b2)/(a0*b1 - b0*a1)
            %x = (x_ - a2 -a1*y)/a0

            y = new_coord(2);
            x = new_coord(1);

            if(strcmp(interpolation,'nearest neighbour'))
                value = 0;
                if ( (1 <= x && x <= M_old) && (1 <= y && y <= N_old))
                    value = img(round(y),round(x));
                end
                img_backward_mapped(y_,x_) = value;
            
            elseif(strcmp(interpolation,'bilinear'))

                x0 = floor(x); x1 = ceil(x);
                y0 = floor(y); y1 = ceil(y);

                if ( (1 <= x0 && x1 <= M_old ) && (1 <= y0 && y1 <= N_old) )

                    dx = x - x0;
                    dy = y - y0;

                    %Used the definition of the interpolation from slide 19 about geometric operations.
                    %The coordinates x and y has been interchanged here compared to the slide.

                    p = img(y0,x0) + (img(y1,x0) - img(y0,x0))*dy;
                    q = img(y0,x1) + (img(y1,x1) - img(y0,x1))*dy;

                    img_backward_mapped(y_,x_) =  p + (q-p)*dx;

                end
            end
        end
    end
end

                
             
            