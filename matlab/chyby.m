clear all;

x20 = [10 15  20 ];
x22 = [10 15  20  22 ];
x25 = [10 15  20  22  25 ];
x27 = [10 15  20  22  25  27 ];
x35 = [10 15  20  22  25  27  30  32  35 ];
x40 = [10 15  20  22  25  27  30  32  35  37  40];
% for j in NK ZKC ZKW; do for i in brute bab dynamic fptas1 fptas3 fptas5 greedy redux; do echo "${j}${i} = importdata('${j}_summary_${i}', ';');"; done; done

NKbrute = importdata('NK_summary_brute', ';');
NKbab = importdata('NK_summary_bab', ';');
NKdynamic = importdata('NK_summary_dynamic', ';');
NKfptas1 = importdata('NK_summary_fptas1', ';');
NKfptas3 = importdata('NK_summary_fptas3', ';');
NKfptas5 = importdata('NK_summary_fptas5', ';');
NKgreedy = importdata('NK_summary_greedy', ';');
NKredux = importdata('NK_summary_redux', ';');

ZKCbrute = importdata('ZKC_summary_brute', ';');
ZKCbab = importdata('ZKC_summary_bab', ';');
ZKCdynamic = importdata('ZKC_summary_dynamic', ';');
ZKCfptas1 = importdata('ZKC_summary_fptas1', ';');
ZKCfptas3 = importdata('ZKC_summary_fptas3', ';');
ZKCfptas5 = importdata('ZKC_summary_fptas5', ';');
ZKCgreedy = importdata('ZKC_summary_greedy', ';');
ZKCredux = importdata('ZKC_summary_redux', ';');

ZKWbrute = importdata('ZKW_summary_brute', ';');
ZKWbab = importdata('ZKW_summary_bab', ';');
ZKWdynamic = importdata('ZKW_summary_dynamic', ';');
ZKWfptas1 = importdata('ZKW_summary_fptas1', ';');
ZKWfptas3 = importdata('ZKW_summary_fptas3', ';');
ZKWfptas5 = importdata('ZKW_summary_fptas5', ';');
ZKWgreedy = importdata('ZKW_summary_greedy', ';');
ZKWredux = importdata('ZKW_summary_redux', ';');


width = 2;
max = 4;
avg = 5;

% ----- ZKC -----
% semilogy(x35, ZKCfptas1(:,max), '-x', 'LineWidth', width, 'color', [0 0.4470 0.7410] ); hold on
% semilogy(x35, ZKCfptas3(:,max), '-x', 'LineWidth', width, 'color', [0.4940 0.1840 0.5560] ); hold on
% semilogy(x35, ZKCfptas5(:,max), '-x', 'LineWidth', width,'color',  [0.3010 0.7450 0.9330]); hold on
% semilogy(x35, ZKCgreedy(:, max), '-x', 'LineWidth', width ,'color', [0.9290 0.6940 0.1250]); hold on
% semilogy(x35, ZKCredux(:, max), '-x', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
% 
% semilogy(x35, ZKCfptas1(:,avg), '-o', 'LineWidth', width,'color',  [0 0.4470 0.7410]); hold on
% semilogy(x35, ZKCfptas3(:,avg), '-o', 'LineWidth', width, 'color', [0.4940 0.1840 0.5560] ); hold on
% semilogy(x35, ZKCfptas5(:,avg), '-o', 'LineWidth', width,'color',  [0.3010 0.7450 0.9330]); hold on
% semilogy(x35, ZKCgreedy(:, avg), '-o', 'LineWidth', width ,'color', [0.9290 0.6940 0.1250]); hold on
% semilogy(x35, ZKCredux(:, avg), '-o', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on

% ----- ZKW -----
% semilogy(x35, ZKWfptas1(:,max), '-x', 'LineWidth', width, 'color', [0 0.4470 0.7410] ); hold on
% semilogy(x35, ZKWfptas3(:,max), '-x', 'LineWidth', width, 'color', [0.4940 0.1840 0.5560] ); hold on
% semilogy(x35, ZKWfptas5(:,max), '-x', 'LineWidth', width,'color',  [0.3010 0.7450 0.9330]); hold on
% semilogy(x35, ZKWgreedy(:, max), '-x', 'LineWidth', width ,'color', [0.9290 0.6940 0.1250]); hold on
% semilogy(x35, ZKWredux(:, max), '-x', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
% 
% semilogy(x35, ZKWfptas1(:,avg), '-o', 'LineWidth', width,'color',  [0 0.4470 0.7410]); hold on
% semilogy(x35, ZKWfptas3(:,avg), '-o', 'LineWidth', width, 'color', [0.4940 0.1840 0.5560] ); hold on
% semilogy(x35, ZKWfptas5(:,avg), '-o', 'LineWidth', width,'color',  [0.3010 0.7450 0.9330]); hold on
% semilogy(x35, ZKWgreedy(:, avg), '-o', 'LineWidth', width ,'color', [0.9290 0.6940 0.1250]); hold on
% semilogy(x35, ZKWredux(:, avg), '-o', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on

% ----- NK ----- 
semilogy(x35, NKfptas1(:,max), '-x', 'LineWidth', width, 'color', [0 0.4470 0.7410] ); hold on
semilogy(x35, NKfptas3(:,max), '-x', 'LineWidth', width, 'color', [0.4940 0.1840 0.5560] ); hold on
semilogy(x35, NKfptas5(:,max), '-x', 'LineWidth', width,'color',  [0.3010 0.7450 0.9330]); hold on
semilogy(x35, NKgreedy(:, max), '-x', 'LineWidth', width ,'color', [0.9290 0.6940 0.1250]); hold on
semilogy(x35, NKredux(:, max), '-x', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on

semilogy(x35, NKfptas1(:,avg), '-o', 'LineWidth', width,'color',  [0 0.4470 0.7410]); hold on
semilogy(x35, NKfptas3(:,avg), '-o', 'LineWidth', width, 'color', [0.4940 0.1840 0.5560] ); hold on
semilogy(x35, NKfptas5(:,avg), '-o', 'LineWidth', width,'color',  [0.3010 0.7450 0.9330]); hold on
semilogy(x35, NKgreedy(:, avg), '-o', 'LineWidth', width ,'color', [0.9290 0.6940 0.1250]); hold on
semilogy(x35, NKredux(:, avg), '-o', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on


grid
legend('FPTAS (0.1) max', 'FPTAS (0.3) max' , 'FPTAS (0.5) max', 'Greedy max', 'Redux max', 'FPTAS (0.1) avg', 'FPTAS (0.3) avg', 'FPTAS (0.5) avg','Greedy avg', 'Redux avg')
%legend('FPTAS (0.1) max', 'FPTAS (0.3) max' , 'FPTAS (0.5) max', 'Redux max', 'FPTAS (0.1) avg', 'FPTAS (0.3) avg', 'FPTAS (0.5) avg','Redux avg')
ylabel('Chybovost (%)')
xlabel('Věcí v batohu')
hold off
