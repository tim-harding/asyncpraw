"""Provide the InboxToggleableMixin class."""
from ....const import API_PATH


class InboxToggleableMixin:
    """Interface for classes that can optionally receive inbox replies."""

    async def disable_inbox_replies(self):
        """Disable inbox replies for the item.

        .. note::

            This can only apply to items created by the authenticated user.

        Example usage:

        .. code-block:: python

            comment = await reddit.comment("dkk4qjd", fetch=False)
            await comment.disable_inbox_replies()

            submission = await reddit.submission("8dmv8z", fetch=False)
            await submission.disable_inbox_replies()

        .. seealso::

            :meth:`.enable_inbox_replies`

        """
        await self._reddit.post(
            API_PATH["sendreplies"], data={"id": self.fullname, "state": False}
        )

    async def enable_inbox_replies(self):
        """Enable inbox replies for the item.

        .. note::

            This can only apply to items created by the authenticated user.

        Example usage:

        .. code-block:: python

            comment = await reddit.comment("dkk4qjd", fetch=False)
            await comment.enable_inbox_replies()

            submission = await reddit.submission("8dmv8z", fetch=False)
            await submission.enable_inbox_replies()

        .. seealso::

            :meth:`.disable_inbox_replies`

        """
        await self._reddit.post(
            API_PATH["sendreplies"], data={"id": self.fullname, "state": True}
        )
