# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T02:52:26.601199+00:00`
- Price records: `672`
- Market context records: `3646`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `37.3859` n `32` status `ready` deltaP `42.5347` edge `2.8362` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `37.3859` n `32` status `ready` deltaP `42.5347` edge `2.8362` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `33.8226` n `32` status `ready` deltaP `44.6181` edge `2.5211` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `33.8226` n `32` status `ready` deltaP `44.6181` edge `2.5211` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `29.6045` n `32` status `ready` deltaP `41.6667` edge `2.2044` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `29.6045` n `32` status `ready` deltaP `41.6667` edge `2.2044` maxDD `-0.8779`
- `risk_on_high->index_24h` score `19.2498` n `32` status `ready` deltaP `44.6181` edge `1.3067` maxDD `0.0`
- `risk_on_and_context->index_24h` score `19.2498` n `32` status `ready` deltaP `44.6181` edge `1.3067` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.705` n `32` status `ready` deltaP `21.0366` edge `0.9474` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.705` n `32` status `ready` deltaP `21.0366` edge `0.9474` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `11.2387` n `32` status `ready` deltaP `30.2083` edge `0.7613` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `11.2387` n `32` status `ready` deltaP `30.2083` edge `0.7613` maxDD `-0.7574`
- `market_context_high->equity_24h` score `9.5347` n `157` status `ready` deltaP `21.6882` edge `1.2164` maxDD `-35.3144`
- `market_context_high->index_24h` score `8.8538` n `157` status `ready` deltaP `29.9684` edge `0.7096` maxDD `-11.3924`
- `market_context_high->metal_24h` score `3.5242` n `157` status `ready` deltaP `24.5156` edge `0.6836` maxDD `-21.6171`
- `market_context_high->crypto_major_24h` score `3.3809` n `157` status `ready` deltaP `8.717` edge `0.9303` maxDD `-49.5335`
- `risk_on_high->crypto_alt_4h` score `3.1432` n `32` status `ready` deltaP `1.4482` edge `0.4367` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.1432` n `32` status `ready` deltaP `1.4482` edge `0.4367` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.5202` n `32` status `ready` deltaP `9.8323` edge `0.371` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5202` n `32` status `ready` deltaP `9.8323` edge `0.371` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
