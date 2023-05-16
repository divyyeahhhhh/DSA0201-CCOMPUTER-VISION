a=imread("C:/Users/divya/Downloads/Girl with a Cat.png");
Lap=[0 1 0; 1 -4 1; 0 1 0];

% Convolve the image read
% in 'a' with Laplacian mask.
a1=conv2(a,Lap,"C:/Users/divya/Downloads/Girl with a Cat.png");

% After convolution the intensity
% Values go beyond the range.
% Normalise the range of intensity.
a2=uint8(a1);

% Display the sharpened image.
imtool(abs(a-a2),[])

% Define strong laplacian filter
lap=[-1 -1 -1; -1 8 -1; -1 -1 -1];

% Apply filter on original image
a3=conv2(a,lap,"C:/Users/divya/Downloads/Girl with a Cat.png");

% Normalise the resultant image.
a4=uint8(a3);

% Display the sharpened image.
imtool(abs(a+a4),[])

