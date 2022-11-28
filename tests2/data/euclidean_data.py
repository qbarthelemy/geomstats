from tests2.data.base_data import VectorSpaceTestData


class EuclideanTestData(VectorSpaceTestData):
    def exp_vec_test_data(self):
        data = [dict(n_reps=n_reps) for n_reps in self.N_VEC_REPS]
        return self.generate_tests(data)

    def exp_random_test_data(self):
        data = [dict(n_points=n_points) for n_points in self.N_RANDOM_POINTS]
        return self.generate_tests(data)
