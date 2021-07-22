class Config:

    def __init__(self, model_type, 
                 model_name_or_path, 
                 data_name,
                 output_dir,

                 max_seq_length=128,
                 batch_size=8, 
                 learning_rate=5e-5,
                 weight_decay=0.01,
                 adam_epsilon=1e-8,
                 max_grad_norm=1.0,
                 num_train_epochs=3,
                 max_steps=-1,
                 warmup_proportion=0.0,
                 log_steps=500,
                 save_steps=500,
                 doc_stride=128,
                 seed=42,
                 device='gpu',
                 do_lower_case=False,
                 verbose=True):
        
        self.model_type = model_type
        self.model_name_or_path = model_name_or_path
        self.data_name=data_name
        self.output_dir = output_dir

        self.max_seq_length = max_seq_length
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay
        self.adam_epsilon = adam_epsilon
        self.max_grad_norm = max_grad_norm
        self.num_train_epochs = num_train_epochs
        self.max_steps = max_steps
        self.warmup_proportion =  warmup_proportion
        self.log_steps = log_steps
        self.save_steps = save_steps
        self.doc_stride = doc_stride
        self.seed = seed
        self.device = device
        self.do_lower_case = do_lower_case
        self.verbose = verbose
