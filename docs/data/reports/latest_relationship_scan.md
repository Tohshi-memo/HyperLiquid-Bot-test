# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T18:37:18.567024+00:00`
- Price records: `672`
- Market context records: `1245`
- Flow alert records: `5492`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_major_24h` score `18.3769` n `128` status `ready` deltaP `42.7951` edge `1.3593` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `8.0179` n `128` status `ready` deltaP `5.221` edge `0.755` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.7178` n `128` status `ready` deltaP `22.4826` edge `0.6949` maxDD `-15.1306`
- `market_context_high->metal_24h` score `7.6584` n `128` status `ready` deltaP `1.5625` edge `0.7945` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8489` n `128` status `ready` deltaP `22.9167` edge `0.2766` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.7878` n `128` status `ready` deltaP `-7.8125` edge `0.5159` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.3848` n `128` status `ready` deltaP `17.5495` edge `0.2314` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.2122` n `128` status `ready` deltaP `22.3958` edge `0.4952` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `1.9914` n `128` status `ready` deltaP `1.5625` edge `0.4285` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5855` n `128` status `ready` deltaP `14.0434` edge `0.1068` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6433` n `128` status `ready` deltaP `9.5996` edge `0.0213` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5738` n `128` status `ready` deltaP `5.609` edge `0.0473` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.3815` n `128` status `ready` deltaP `6.3369` edge `0.036` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.2653` n `128` status `ready` deltaP `10.8673` edge `0.0107` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.2537` n `128` status `ready` deltaP `15.606` edge `0.0602` maxDD `-6.4478`
- `market_context_high->crypto_major_4h` score `-0.0141` n `128` status `ready` deltaP `6.917` edge `0.1442` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0629` n `128` status `ready` deltaP `6.0489` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2931` n `128` status `ready` deltaP `0.7953` edge `0.0414` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4315` n `128` status `ready` deltaP `2.0771` edge `0.0074` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6693` n `128` status `ready` deltaP `8.0983` edge `0.1567` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
