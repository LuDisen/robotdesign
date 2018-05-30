motor_db = {
    'TSM3104E040': {
        "cm": [0, 0, -50e-3],
        "m": 0.7,
        "J_rotor": 6.7e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 2800, 3750, 6000],
                [1.11, 1.11, 0.8, 0.4]
            ],
            's1': [
                [0, 3000, 4500, 6000],
                [0.318, 0.318, 0.2, 0.18]
            ]
        }
    },

    'TSM3102E040': {
        "cm": [0, 0, -45e-3],
        "m": 0.6,
        "J_rotor": 3.8e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 1800, 3500, 6000],
                [0.56, 0.56, 0.3, 0.11]
            ],
            's1': [
                [0, 3000, 4700, 6000],
                [0.159, 0.159, 0.1, 0.095]
            ]
        }
    },

    'TSM3101E040': {
        "cm": [0, 0, -25e-3],
        "m": 0.5,
        "J_rotor": 2.8e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 3000, 4500, 6000],
                [0.33, 0.33, 0.225, 0.17]
            ],
            's1': [
                [0, 3000, 4000, 6000],
                [0.095, 0.095, 0.075, 0.05]
            ]
        }
    },

    'TS4866': {
        "cm": [0, 0, -45e-3],
        "m": 0.12,
        "J_rotor": 0.26e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 5000, 6000],
                [0.1431, 0.1431, 0.126]
            ],
            's1': [
                [0, 3000, 6000],
                [0.0477, 0.0477, 0.025]
            ]
        }
    },

    'TS4864': {
        "cm": [0, 0, -35e-3],
        "m": 0.09,
        "J_rotor": 0.17e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 5500, 6000],
                [0.096, 0.096, 0.09]],
            's1': [
                [0, 3000, 4500, 6000],
                [0.032, 0.032, 0.02, 0.0125]
            ]
        }
    },

    'TS4862': {
        "cm": [0, 0, -25e-3],
        "m": 0.06,
        "J_rotor": 0.096e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 6000],
                [0.0477, 0.0477]],
            's1': [
                [0, 3000, 4500, 6000],
                [0.0159, 0.0159, 0.01, 0.008]
            ]
        }
    },

    'TS4871': {
        "cm": [0, 0, -28e-3],
        "m": 0.111,
        "J_rotor": 0.31e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 5650, 6000],
                [0.096, 0.096, 0.09]
            ],
            's1': [
                [0, 3000, 3600, 5000, 6000],
                [0.032, 0.032, 0.025, 0.01875, 0.0175]
            ]
        }
    },

    'TS4872': {
        "cm": [0, 0, -38e-3],
        "m": 0.15,
        "J_rotor": 0.47e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 5250, 6000],
                [0.155, 0.155, 0.1475]
            ],
            's1': [
                [0, 3000, 6000],
                [0.051, 0.051, 0.025]
            ]
        }
    },

    'TS4873': {
        "cm": [0, 0, -38e-3],
        "m": 0.17,
        "J_rotor": 0.57e-6,
        "iT": [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 5250, 6000],
                [0.192, 0.192, 0.153]
            ],
            's1': [
                [0, 3000, 5000, 6000],
                [0.064, 0.064, 0.0375, 0.027]
            ]
        }
    },

    'TSM3304E200': {
        "cm": [0, 0, 69e-3],
        "m": 3.2,
        "J_rotor": 1.66e-4,
        "iT": [2840e-6, 2840e-6, 1050e-6, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 3040, 5520, 8000, 8001],
                [5.98, 5.98, 4.22, 1.79, 0]
            ],
            's1': [
                [0, 3000, 6000],
                [2.39, 2.39, 1.2]
            ]
        }
    },

    'TSM3204E200': {
        "cm": [0, 0, 63e-3],
        "m": 1.7,
        "J_rotor": 0.5e-4,
        "iT": [1800e-6, 1800e-6, 700e-6, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 4320, 6160, 8000, 8001],
                [3.256, 3.2, 2.6, 2, 0]
            ],
            's1': [
                [0, 3000, 6000],
                [1.27, 1.1, 0.65]
            ]
        }
    },

    'TSM3104E200': {
        "cm": [0, 0, 56e-3],
        "m": 0.7,
        "J_rotor": 6.7e-6,
        "iT": [1000e-6, 1000e-6, 150e-6, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 3200, 5600, 8000, 8001],
                [0.92, 0.92, 0.54, 0.38, 0]
            ],
            's1':  [
                [0, 3000, 6000],
                [0.318, 0.26076, 0.18]
            ]
        }
    },

    'TSM3102E200': {
        "cm": [0, 0, 41e-3],
        "m": 0.6,
        "J_rotor": 3.8e-6,
        "iT": [320e-6, 320e-6, 123e-6, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 5200, 6600, 8000, 8001],
                [0.46, 0.46, 0.4, 0.36, 0]
            ],
            's1':  [
                [0, 3000, 6000],
                [0.159, 0.13, 0.08]
            ]
        }
    },

    'TS4632': {
        "cm":             [0, 0, 40e-3],
        "m":              0.19,
        "J_rotor":        0.4e-6,
        "iT":             [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 4700, 5000],
                [0.185, 0.185, 0.16]
            ],
            's1':  [
                [0, 4000, 5000],
                [0.062, 0.062, 0.05]
            ]
        }
    },

    'TS4631': {
        "cm":             [0, 0, 32e-3],
        "m":              0.15,
        "J_rotor":        0.4e-6,
        "iT":             [0, 0, 0, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 2150, 5000],
                [0.094, 0.094, 0.0575]
            ],
            's1':  [
                [0, 4000, 5000],
                [0.031, 0.031, 0.025]
            ]
        }
    },

    'PT_SCARA_A1': {
        "cm":             [0, 0, 63e-3],
        "m":              1.7,
        "J_rotor":        0.5e-4,
        "iT":             [1800e-6, 1800e-6, 700e-6, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 4320, 6160, 8000, 8001],
                [3.256, 3.2, 2.6, 2, 0]
            ],
            's1':  [
                [0, 3000, 6000],
                [1.27, 1.1, 0.65]
            ]
        }
    },

    'PT_SCARA_A2': {
        "cm":             [0, 0, 63e-3],
        "m":              1.7,
        "J_rotor":        0.5e-4,
        "iT":             [1800e-6, 1800e-6, 700e-6, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 4320, 6160, 8000, 8001],
                [3.256, 3.2, 2.6, 2, 0]
            ],
            's1':  [
                [0, 3000, 6000],
                [1.27, 1.1, 0.65]
            ]
        }
    },

    'PT_SCARA_A3': {
        "cm":             [0, 0, 56e-3],
        "m":              0.7,
        "J_rotor":        6.7e-6,
        "iT":             [1000e-6, 1000e-6, 150e-6, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 3200, 5600, 8000, 8001],
                [0.92, 0.92, 0.54, 0.38, 0]
            ],
            's1':  [
                [0, 3000, 6000],
                [0.318, 0.26076, 0.18]
            ]
        }
    },

    'PT_SCARA_A4': {
        "cm":             [0, 0, 41e-3],
        "m":              0.6,
        "J_rotor":        3.8e-6,
        "iT":             [320e-6, 320e-6, 123e-6, 0, 0, 0],
        "characteristic": {
            'max': [
                [0, 5200, 6600, 8000, 8001],
                [0.46, 0.46, 0.4, 0.36, 0]
            ],
            's1':  [
                [0, 3000, 6000],
                [0.159, 0.13, 0.08]
            ]
        }
    },

}


def load_motor_db(installation):
    data = {**installation, **motor_db[installation['type']]}
    return data
