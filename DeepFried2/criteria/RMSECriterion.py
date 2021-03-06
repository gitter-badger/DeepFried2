import DeepFried2 as df


class RMSECriterion:
    def symb_forward(self, symb_input, symb_target):
        return df.T.mean(df.T.sqrt(df.T.sum((symb_input - symb_target)**2, axis=1)))


class MSECriterion:
    def symb_forward(self, symb_input, symb_target):
        return df.T.mean(df.T.sum((symb_input - symb_target)**2, axis=1))
