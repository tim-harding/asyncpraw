"""Provide the VotableMixin class."""
from __future__ import annotations

from ....const import API_PATH


class VotableMixin:
    """Interface for :class:`.RedditBase` classes that can be voted on."""

    async def _vote(self, direction: int):
        await self._reddit.post(
            API_PATH["vote"], data={"dir": str(direction), "id": self.fullname}
        )

    async def clear_vote(self):
        """Clear the authenticated user's vote on the object.

        .. note::

            Votes must be cast by humans. That is, API clients proxying a human's action
            one-for-one are OK, but bots deciding how to vote on content or amplifying a
            human's vote are not. See the reddit rules for more details on what
            constitutes vote manipulation. [`Ref
            <https://www.reddit.com/dev/api#POST_api_vote>`_]

        Example usage:

        .. code-block:: python

            submission = await reddit.submission("5or86n", fetch=False)
            await submission.clear_vote()

            comment = await reddit.comment("dxolpyc", fetch=False)
            await comment.clear_vote()

        """
        await self._vote(direction=0)

    async def downvote(self):
        """Downvote the object.

        .. note::

            Votes must be cast by humans. That is, API clients proxying a human's action
            one-for-one are OK, but bots deciding how to vote on content or amplifying a
            human's vote are not. See the reddit rules for more details on what
            constitutes vote manipulation. [`Ref
            <https://www.reddit.com/dev/api#POST_api_vote>`_]

        Example usage:

        .. code-block:: python

            submission = await reddit.submission("5or86n", fetch=False)
            await submission.downvote()

            comment = await reddit.comment("dxolpyc", fetch=False)
            await comment.downvote()

        .. seealso::

            :meth:`.upvote`

        """
        await self._vote(direction=-1)

    async def upvote(self):
        """Upvote the object.

        .. note::

            Votes must be cast by humans. That is, API clients proxying a human's action
            one-for-one are OK, but bots deciding how to vote on content or amplifying a
            human's vote are not. See the reddit rules for more details on what
            constitutes vote manipulation. [`Ref
            <https://www.reddit.com/dev/api#POST_api_vote>`_]

        Example usage:

        .. code-block:: python

            submission = await reddit.submission("5or86n", fetch=False)
            await submission.upvote()

            comment = await reddit.comment("dxolpyc", fetch=False)
            await comment.upvote()

        .. seealso::

            :meth:`.downvote`

        """
        await self._vote(direction=1)
