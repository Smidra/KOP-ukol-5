clear all;

% for j in NK ZKC ZKW; do for i in brute bab dynamic fptas1 fptas3 fptas5 greedy redux; do echo "${j}${i} = importdata('${j}_summary_${i}', ';');"; done; done

width = 2;
max = 2;
avg = 3;

% babMAXstrong = [118   709   1862    4492   11101];
% babAVGstrong = [58   360   835    2128   5640];
% babMAXcorr =   [148   1002   3048    7268   17628];
% babAVGcorr =   [66   411   1089    2752   7256];
% babMAXuni =    [47   153   281    660    638];
% babAVGuni =    [17   33   51    79     96];
% 
% plot(x, babMAXstrong,'-x', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, babAVGstrong,'-o', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, babMAXcorr, '-x', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% plot(x, babAVGcorr, '-o', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% plot(x, babMAXuni,'-x', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
% plot(x, babAVGuni,'-o', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
% legend('strong bab max', 'strong bab avg', 'corr bab max', 'corr bab avg', 'uni bab max', 'uni bab avg')
% ylim([0 6000])



% dynMAXstrong = [2038  18609   36579    60115       84024];
% dynAVGstrong = [1891  16249   31100    49706       72230];
% dynMAXcorr =   [2046  20390   39171    64680       89854];
% dynAVGcorr =   [1899  16338   31383    51208       74144];
% dynMAXuni =    [2046  20069   39573    65772       102133];
% dynAVGuni =    [1902  16791   32308    52770       77564];
% 
% plot(x, dynMAXstrong,'-x', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, dynAVGstrong,'-o', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, dynMAXcorr,  '-x', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% plot(x, dynAVGcorr,  '-o', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% plot(x, dynMAXuni,   '-x', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
% plot(x, dynAVGuni,   '-o', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
% legend('strong bab max', 'strong bab avg', 'corr bab max', 'corr bab avg', 'uni bab max', 'uni bab avg')
% ylim([0 60000])



% reduxMAXstrong = [ 19.173474   14.184867    5.961666    9.67971     9.314884 ];
% reduxAVGstrong = [ 10.421805   5.979555     0.767454    4.200750    5.042353 ];
% reduxMAXcorr =   [ 22.675159   14.416651    15.60071    13.75925    10.791576 ];
% reduxAVGcorr =   [ 6.446171    5.165493     4.526299    4.061455    3.760508 ];
% reduxMAXuni =    [ 9.475580    6.375321     5.961666    6.026059    4.693065 ];
% reduxAVGuni =    [ 1.130760    0.710166     0.767454    0.547468    0.564037 ];
% 
% plot(x, reduxMAXstrong,'-x', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, reduxAVGstrong,'-o', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
% plot(x, reduxMAXcorr,  '-x', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% plot(x, reduxAVGcorr,  '-o', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
% plot(x, reduxMAXuni,   '-x', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
% plot(x, reduxAVGuni,   '-o', 'LineWidth', width ,'color', [0.4660 0.6740 0.1880]); hold on
% legend('strong bab max', 'strong bab avg', 'corr bab max', 'corr bab avg', 'uni bab max', 'uni bab avg')
% ylim([0 25])




x =           [0.1  0.3     0.5      0.7      0.8    0.9  1    ];
reduxMAXlight = [5.051857    5.469506   4.548967   8.046585  8.575942   5.486845  7.238359 ];
reduxAVGlight = [0.636204    0.667748   0.632932  0.673839   0.659175   0.761267  0.756550   ];
reduxMAXheavy = [4.516995     5.281690   4.322406  3.926490  4.274962   4.035953  3.707336  ];
reduxAVGheavy = [0.657686     0.640738   0.553798  0.504983  0.548842   0.524980  0.479724  ];


plot(x, reduxMAXlight,  '-x', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
plot(x, reduxAVGlight,  '-o', 'LineWidth', width ,'color', [0.8500 0.3250 0.0980]); hold on
plot(x, reduxMAXheavy,  '-x', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on
plot(x, reduxAVGheavy,  '-o', 'LineWidth', width ,'color', [0.4940 0.1840 0.5560]); hold on

legend('light redux max', 'light redux avg', 'heavy redux max', 'heavy redux avg')
ylim([0 10])

grid
ylabel('Chybovost')
xlabel('Granularita')
hold off
