clear all;

% for j in NK ZKC ZKW; do for i in brute bab dynamic fptas1 fptas3 fptas5 greedy redux; do echo "${j}${i} = importdata('${j}_summary_${i}', ';');"; done; done


% GPbrute  = importdata('brute-11-100_(w1000c1000)[m0.8wbalcunik1]_summary', ';');
% GPredux  = importdata('redux-11-100_(w1000c1000)[m0.8wbalcunik1]_summary', ';');

% GPbab    = importdata('bab-15-100_(w1000c1000)[m0.8wbalcunik1]_summary', ';');
% GPdynamic= importdata('dynamic-15-100_(w1000c1000)[m0.8wbalcunik1]_summary', ';');





GPbab    = importdata('bab-10-100_(w1000c1000)[m0.8wbalcunik1]_summary', ';');
GPdynamic= importdata('dynamic-10-100_(w1000c1000)[m0.8wbalcunik1]_summary', ';');


width = 2;
max = 2;
avg = 3;

x = [     100 250  500  750  1000  1250  1500];
babMAX = [190 191  191  191  193   195   193 ];
babAVG = [41  41.5 41.5 41.5 41.5  41.6  41.6];
reduxMAX = [15 15  15   15   15    15    15 ];
reduxAVG = [14  14 14   14   14    14    14];


dynMAX = [7112  13418  19899  24918  29304  32979  34506];
dynAVG = [5186  10111  16012  20463  24095  27132  29671];
brute  = [32768 32768  32768  32768  32768  32768  32768];


plot(x, babMAX,'-x', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
plot(x, babAVG,'-o', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
plot(x, reduxMAX, '-x', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
plot(x, reduxAVG, '-o', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
ylim([0 200])

% plot(x, brute, '-x', 'LineWidth', width ,'color', [0.6350 0.0780 0.1840]); hold on
% plot(x, dynMAX,'-x', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% plot(x, dynAVG,'-o', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% ylim([0 35000])

% plot(x, GPbab(:,   max), '-x', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, GPbab(:,   avg), '-o', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on

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

% legend('brute max','bab max', 'Dynamic cost max', 'Redux max', 'brute avg','bab avg','Dynamic cost avg', 'Redux avg')
legend('bab max', 'bab avg', 'redux max', 'redux avg')
% legend('brute', 'Dynamic cost max','Dynamic cost avg')

ylabel('Složitost')
xlabel('Maximální cena')
hold off
