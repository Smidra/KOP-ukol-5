clear all;

graf = importdata('../calculated_sim/chart_16_2211.dat');
width = 2;

plot( 1:1:size(graf) , graf(:), 'LineWidth', width); hold on


% ----- ZKC -----
% 'color', [0.4660 0.6740 0.1880]
% [0.6350 0.0780 0.1840] - cervena
% [0.8500 0.3250 0.0980] - orandzova
% [0.4940 0.1840 0.5560] - fialova
% [0.4660 0.6740 0.1880] - zelena

grid

% title('Složitost')
% subtitle('pro metodu větví a hranic')
% legend('bab max', 'bab avg')

legend('t=30, c=97')

ylabel('Váha')
xlabel('Kroků')
hold off
