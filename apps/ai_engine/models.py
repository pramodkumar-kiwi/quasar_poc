"""
ai_engine App models
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class OpenAiConfig(models.Model):
    """
    This class is used to handle openai related attributes
    """
    temperature = models.FloatField(
        default=0.3,
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        help_text="""
        Temperature range will be 0 - 1.<br>
        <strong>Note:</strong> Temperature changes in GPT APIs affect output randomness:<br>
        &emsp;&emsp;&emsp;higher temperature increases creativity, lower temperature promotes coherence.
        """
    )

    class Meta:
        """
        To specify db_table OpenAiConfig and verbose name attributes
        """
        db_table = "openaiconfig"
        verbose_name = "Open Ai Config"
