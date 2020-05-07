from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown (MRJob):
    SORT_VALUES = True
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_movieIDs,
                    reducer=self.reducer_count_ratings),
            MRStep(mapper=self.mapper_format_movie,
                   reducer=self.reducer_sort_movies)

        ]

    def mapper_get_movieIDs(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1   
        
    def reducer_count_ratings(self, movieID, counts):
         yield movieID, sum(counts)

    def mapper_format_movie(self, movieID, totalCount):
        yield ('%020d' % int(totalCount), int(movieID))

    def reducer_sort_movies(self, totalCount, movieID):
        for id in movieID:
            yield int(totalCount), str(id)
                        
if __name__ == '__main__':
    RatingsBreakdown.run()
