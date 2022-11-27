from typing import List, TypeVar, Union

from ..client import CommandArgs, SubCommand

TWhereable = TypeVar("TWhereable", bound="Whereable")


class Whereable:
    _where: List[List[Union[str, int]]]

    def compile_where(self) -> CommandArgs:
        """__compile_where.

        Args:

        Returns:
            CommandArgs
        """
        w = []

        if len(self._where) > 0:
            for i in self._where:
                w.extend(i)
            return w
        else:
            return []

    def where(self: TWhereable, field: str, min: int, max: int) -> TWhereable:
        """Filter the search by field

        Args:
            field (str): field name
            min (int): minimum value of field
            max (int): maximum value of field

        Returns:
            TWhereable
        """

        self._where.append([SubCommand.WHERE, field, min, max])

        return self

    def where_with_fields(
        self: TWhereable, field: str, minimum: int, maximum: int
    ) -> TWhereable:
        """Filter the search by field

        Args:
            field (str): field name
            minimum (int): minimum value of field
            maximum (int): maximum value of field

        Returns:
            TWhereable
        """

        self._where.append([SubCommand.WHERE, field, minimum, maximum])

        return self

    def where_with_expr(self: TWhereable, expr: str) -> TWhereable:
        """Filter the search by field

        Args:
            field (str): field name
            minimum (int): minimum value of field
            maximum (int): maximum value of field

        Returns:
            Within
        """

        self._where.append([SubCommand.WHERE, expr])

        return self
