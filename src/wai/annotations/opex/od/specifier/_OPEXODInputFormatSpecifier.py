from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SourceStageSpecifier


class OPEXODInputFormatSpecifier(SourceStageSpecifier):
    """
    Specifier of the components for reading the OPEX
    object detection format.
    """
    @classmethod
    def description(cls) -> str:
        return "Reads image object-detection annotations in the OPEX format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from wai.annotations.core.component.util import LocalFilenameSource
        from ..component import FromOPEXOD, OPEXODReader
        return LocalFilenameSource, OPEXODReader, FromOPEXOD

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        return ImageObjectDetectionDomainSpecifier
