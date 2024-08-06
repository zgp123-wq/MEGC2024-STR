import warnings
from typing import Optional
import torch
import torch.nn as nn


class MultiheadAttention(nn.Module):
    """A wrapper for ``torch.nn.MultiheadAttention``
    Implement MultiheadAttention with identity connection,
    and position embedding is also passed as input.
    Args:
        embed_dim (int): The embedding dimension for attention.
        num_heads (int): The number of attention heads.
        attn_drop (float): A Dropout layer on attn_output_weights.
            Default: 0.0.
        proj_drop (float): A Dropout layer after `MultiheadAttention`.
            Default: 0.0.
        batch_first (bool): if `True`, then the input and output tensor will be
            provided as `(bs, n, embed_dim)`. Default: False. `(n, bs, embed_dim)`
    """

    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        attn_drop: float = 0.0,
        proj_drop: float = 0.0,
        batch_first: bool = False,
        **kwargs,
    ):
        super(MultiheadAttention, self).__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.batch_first = batch_first

        self.attn = nn.MultiheadAttention(
            embed_dim=embed_dim,
            num_heads=num_heads,
            dropout=attn_drop,
            batch_first=batch_first,
            **kwargs,
        )

        self.proj_drop = nn.Dropout(proj_drop)

    def forward(
        self,
        query: torch.Tensor,
        key: Optional[torch.Tensor] = None,
        value: Optional[torch.Tensor] = None,
        identity: Optional[torch.Tensor] = None,
        query_pos: Optional[torch.Tensor] = None,
        key_pos: Optional[torch.Tensor] = None,
        attn_mask: Optional[torch.Tensor] = None,
        key_padding_mask: Optional[torch.Tensor] = None,
        **kwargs,
    ) -> torch.Tensor:
        """Forward function for `MultiheadAttention`
        **kwargs allow passing a more general data flow when combining
        with other operations in `transformerlayer`.
        Args:
            query (torch.Tensor): Query embeddings with shape
                `(num_query, bs, embed_dim)` if self.batch_first is False,
                else `(bs, num_query, embed_dim)`
            key (torch.Tensor): Key embeddings with shape
                `(num_key, bs, embed_dim)` if self.batch_first is False,
                else `(bs, num_key, embed_dim)`
            value (torch.Tensor): Value embeddings with the same shape as `key`.
                Same in `torch.nn.MultiheadAttention.forward`. Default: None.
                If None, the `key` will be used.
            identity (torch.Tensor): The tensor, with the same shape as x, will
                be used for identity addition. Default: None.
                If None, `query` will be used.
            query_pos (torch.Tensor): The position embedding for query, with the
                same shape as `query`. Default: None.
            key_pos (torch.Tensor): The position embedding for key. Default: None.
                If None, and `query_pos` has the same shape as `key`, then `query_pos`
                will be used for `key_pos`.
            attn_mask (torch.Tensor): ByteTensor mask with shape `(num_query, num_key)`.
                Same as `torch.nn.MultiheadAttention.forward`. Default: None.
            key_padding_mask (torch.Tensor): ByteTensor with shape `(bs, num_key)` which
                indicates which elements within `key` to be ignored in attention.
                Default: None.
        """
        if key is None:
            key = query
        if value is None:
            value = key
        if identity is None:
            identity = query
        if key_pos is None:
            if query_pos is not None:
                # use query_pos if key_pos is not available
                if query_pos.shape == key.shape:
                    key_pos = query_pos
                else:
                    warnings.warn(f"position encoding of key is" f"missing in {self.__class__.__name__}.")
        if query_pos is not None:
            query = query + query_pos
        if key_pos is not None:
            key = key + key_pos

        out = self.attn(
            query=query,
            key=key,
            value=value,
            attn_mask=attn_mask,
            key_padding_mask=key_padding_mask,
        )[0]

        return identity + self.proj_drop(out)
