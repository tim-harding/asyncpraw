"""Provide the RisingListingMixin class."""
from __future__ import annotations

from typing import TYPE_CHECKING, AsyncIterator
from urllib.parse import urljoin

from ...base import AsyncPRAWBase
from ..generator import ListingGenerator

if TYPE_CHECKING:  # pragma: no cover
    import asyncpraw.models


class RisingListingMixin(AsyncPRAWBase):
    """Mixes in the rising methods."""

    def random_rising(
        self, **generator_kwargs: str | int | dict[str, str]
    ) -> AsyncIterator[asyncpraw.models.Submission]:
        """Return a :class:`.ListingGenerator` for random rising submissions.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        For example, to get random rising submissions for r/test:

        .. code-block:: python

            subreddit = await reddit.subreddit("test")
            async for submission in subreddit.random_rising():
                print(submission.title)

        """
        return ListingGenerator(
            self._reddit, urljoin(self._path, "randomrising"), **generator_kwargs
        )

    def rising(
        self, **generator_kwargs: str | int | dict[str, str]
    ) -> AsyncIterator[asyncpraw.models.Submission]:
        """Return a :class:`.ListingGenerator` for rising submissions.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        For example, to get rising submissions for r/test:

        .. code-block:: python

            subreddit = await reddit.subreddit("test")
            async for submission in subreddit.rising():
                print(submission.title)

        """
        return ListingGenerator(
            self._reddit, urljoin(self._path, "rising"), **generator_kwargs
        )
