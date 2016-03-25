%% parameters

num_subparts = 40;
num_resources = 4;
num_fit_initializations = 25;


student_data = csvread('xBKT_student_matrix.csv',0,1);
question_data = csvread('xBKT_student_matrix.csv',0,0);
question_data = question_data(:,1);
student_start_idx = csvread('xBKT_student_idx.csv',0,0);
resources = csvread('xBKT_resources.csv',0,0);
lengths = csvread('xBKT_lengths.csv',0,0);


size(student_data)
size(student_start_idx)
size(resources)
size(lengths)
%% create a stateseqs 1x (observations) with student_data 
%% if the colsum >=8, then set to 1 else 0 
sum_answer = sum( student_data,1);
student_states = sum_answer >= 8 ;

espark_data = struct ;
espark_data.stateseqs = int8(student_states) ;
espark_data.data = int8(student_data) ;
espark_data.starts = int32(student_start_idx') ;
espark_data.lengths = int32(lengths') ;
espark_data.resources = int16(resources+1);



%% generate a random fitmodel
%% random_model: draws it from dirichlet
%% random_model_uni: draws it from uniform - gives you 0 as forgets 
		%% we don't expect forgetting in a short session 
		%% with forget, the fit is exponentially more complicated 
fitmodel = generate.random_model_uni(num_resources,num_subparts);

best_likelihood = -inf;
for i=1:num_fit_initializations
    util.print_dot(i,num_fit_initializations);
    fitmodel = generate.random_model_uni(num_resources,num_subparts);
    % fitmodel = truemodel; % NOTE: include this line to initialize at the truth
    [fitmodel, log_likelihoods] = fit.EM_fit(fitmodel,espark_data);
    if (log_likelihoods(end) > best_likelihood)
        best_likelihood = log_likelihoods(end);
        best_model = fitmodel;
    end
end
 
% predicted states - allows you to find the predicted state for each question - predict likelihod of correct 
fit.predict_onestep