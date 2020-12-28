clear all;

graf = importdata('graf19.txt');
width = 2;

plot( 1:1:size(graf) , graf(:), 'LineWidth', width ); hold on


% ----- ZKC -----
% semilogy(x, GPbrute(:, max), '-x', 'LineWidth', width ,'color', [0.6350 0.0780 0.1840]); hold on
% plot(x, GPbab(:,   max), '-x', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, GPdynamic(:,max),'-x', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% semilogy(x, GPredux(:, max), '-x', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on

% semilogy(x, GPbrute(:, avg), '-o', 'LineWidth', width ,'color', [0.6350 0.0780 0.1840]); hold on
% plot(x, GPbab(:,   avg), '-o', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, GPdynamic(:,avg),'-o', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% semilogy(x, GPredux(:, avg), '-o', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on

grid

% title('Složitost')
% subtitle('pro metodu větví a hranic')
% legend('FPTAS (0.1) max','FPTAS (0.3) max','FPTAS (0.5) max', 'Greedy max', 'Redux max', 'B&B max', 'Brute max', 'FPTAS (0.1) avg','FPTAS (0.3) avg','FPTAS (0.5) avg', 'Greedy avg', 'Redux avg', 'B&B avg', 'Brute avg')
% legend('FPTAS (0.1) max','FPTAS (0.5) max', 'Greedy max', 'Redux max', 'B&B max', 'Brute max', 'FPTAS (0.1) avg','FPTAS (0.5) avg', 'Greedy avg', 'Redux avg', 'B&B avg', 'Brute avg')
% legend('brute max','bab max', 'Dynamic cost max', 'Redux max', 'brute avg','bab avg','Dynamic cost avg', 'Redux avg')

% legend('bab max', 'bab avg')
legend('t=30, c=97')

ylabel('Cena')
xlabel('Kroků')
hold off
