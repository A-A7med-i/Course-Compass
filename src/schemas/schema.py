from src.constants.constant import NO_KEYWORDS
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class SearchQueries(BaseModel):
    """
    Represents a list of search queries to be used with a search engine.
    """

    quires: List[str] = Field(
        ...,
        title="Suggested search queries to be passed to the search engine",
        min_items=1,
        max_items=NO_KEYWORDS,
    )


class Price(BaseModel):
    """
    Represents the pricing information for a course.
    """

    amount: float = Field(..., description="The current price of the course.")
    currency: str = Field(..., description="The currency code (e.g., USD, EUR).")
    original_amount: Optional[float] = Field(
        None, description="The original price before any discount, if applicable."
    )
    discount_percentage: Optional[float] = Field(
        None, description="The calculated discount percentage."
    )


class CourseMetadata(BaseModel):
    """
    Represents additional metadata about a course.
    """

    instructor: Optional[str] = Field(None, description="Name of the course instructor")
    rating: Optional[float] = Field(None, description="Course rating if available")
    reviews_count: Optional[int] = Field(None, description="Number of reviews")
    last_updated: Optional[str] = Field(
        None, description="When the course was last updated"
    )
    duration: Optional[str] = Field(None, description="Course duration information")


class SingleSearchResult(BaseModel):
    """
    Represents a single search result for a course.
    """

    title: str = Field(..., description="The full title of the course")
    url: str = Field(..., description="The direct URL to the course page")
    content: str = Field(
        ..., description="A brief description or extracted content from the page"
    )
    score: float = Field(
        ..., description="The confidence score of this result (0.0-1.0)"
    )
    search_query: str = Field(..., description="The query that produced this result")
    provider: Optional[str] = Field(
        None, description="The name of the course provider/platform"
    )
    price: Optional[Price] = Field(None, description="Price information for the course")
    metadata: Optional[CourseMetadata] = Field(
        None, description="Additional course metadata"
    )


class AllSearchResults(BaseModel):
    """
    Represents a collection of search results.
    """

    results: List[SingleSearchResult] = Field(
        ..., description="List of all search results"
    )


class Rating(BaseModel):
    """
    Represents the rating information for a course.
    """

    score: float = Field(..., description="Average rating score (typically 0-5)")
    count: int = Field(..., description="Number of reviews/ratings")


class Course(BaseModel):
    """
    Represents detailed information about a single course.
    """

    title: str = Field(..., description="The full title of the course")
    url: str = Field(..., description="The direct URL to the course page")
    provider: str = Field(..., description="Platform or website offering the course")
    instructor: Optional[str] = Field(None, description="Name of the course instructor")
    price: Price = Field(..., description="Price information")
    duration: Optional[str] = Field(
        None, description="Course duration (e.g., '10 hours', '6 weeks')"
    )
    level: Optional[str] = Field(
        None, description="Skill level (e.g., 'Beginner', 'Intermediate', 'Advanced')"
    )
    rating: Optional[Rating] = Field(None, description="Rating information")
    last_updated: Optional[str] = Field(
        None, description="When the course was last updated (ISO format date string)"
    )
    topics: List[str] = Field(
        default=[], description="Main topics covered in the course"
    )
    description: Optional[str] = Field(None, description="Brief course description")
    value_score: Optional[float] = Field(
        None, description="Calculated value score for recommendation ranking"
    )


class Recommendation(BaseModel):
    """
    Represents a recommended course and the reason for the recommendation.
    """

    course: Course = Field(..., description="The recommended course")
    reason: str = Field(
        ..., description="Explanation for why this course is recommended"
    )
    rank: int = Field(..., description="Ranking position in recommendations")


class ScrapingResult(BaseModel):
    """
    Represents the final result of the course scraping process.
    """

    courses: List[Course] = Field(..., description="All scraped courses")
    top_recommendations: List[Recommendation] = Field(
        ..., description="Top recommended courses"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata about the scraping process",
    )
