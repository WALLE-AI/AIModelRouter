import logging

from model_runtime.errors.validate import CredentialsValidateFailedError
from model_runtime.model_providers.__base.model_provider import ModelProvider
from model_runtime.entities.model_entities import ModelType

logger = logging.getLogger(__name__)


class JinaProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        """
        Validate provider credentials
        if validate failed, raise exception

        :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
        """
        try:
            model_instance = self.get_model_instance(ModelType.TEXT_EMBEDDING)

            # Use `jina-embeddings-v3` model for validate,
            # no matter what model you pass in, text completion model or chat model
            model_instance.validate_credentials(model="jina-embeddings-v3", credentials=credentials)
        except CredentialsValidateFailedError as ex:
            raise ex
        except Exception as ex:
            logger.exception(f"{self.get_provider_schema().provider} credentials validate failed")
            raise ex