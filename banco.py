'''Info about client's bank'''


class Bank:
    def __init__(self, agency, c_account, s_account):
        # self._cpf = None
        self._agency = None
        self._c_account = None
        self._s_account = None


class Bank_Creation(Bank):
    def __init__(self, agency, c_account, s_account):
        super().__init__(agency, c_account, s_account)
        # self._cpf = stored_cpf
        self._agency = agency
        self._c_account = c_account
        self._s_account = s_account

    @property
    def bank_data(self):
        return self._agency, self._c_account, self._s_account
