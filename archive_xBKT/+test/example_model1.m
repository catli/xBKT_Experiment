%% An example with 10 students, and 2 different types of resources 
%% Students may see 5 different questions 
%%  

num_subparts = 4;
num_resources = 2;
num_fit_initializations = 25;
observation_sequence_lengths = 5*ones(1,10);

%% Define the true model for synthetic data
truemodel = struct;

% The true model has a couple of objects.
% The As matrix stores the transition probability.
% The learning probability is the probability a student transitions from not knowing to knowing 
% In this model, there are two different resources with two different transition probability
% 

truemodel.As = cat(3,[0.75, 0.25; 0.1, 0.9]',[0.9, 0.1; 0.1, 0.9]');
truemodel.learns = truemodel.As(2,1,:);
truemodel.forgets = truemodel.As(1,2,:);

truemodel.pi_0 = [0.9;0.1];
truemodel.prior = 0.1;

truemodel.guesses = 0.05 * ones(1,num_subparts);
truemodel.slips = 0.25 * ones(1,num_subparts);


