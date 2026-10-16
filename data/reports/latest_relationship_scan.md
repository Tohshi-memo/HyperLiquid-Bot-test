# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T12:37:27.399946+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8638`

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

- `risk_on_high->commodity_24h` score `8.0123` n `54` status `ready` deltaP `42.5087` edge `0.3843` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0123` n `54` status `ready` deltaP `42.5087` edge `0.3843` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.7516` n `127` status `ready` deltaP `17.2328` edge `0.5392` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.526` n `127` status `ready` deltaP `20.6633` edge `0.4549` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.7706` n `54` status `ready` deltaP `19.6534` edge `0.3112` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.7706` n `54` status `ready` deltaP `19.6534` edge `0.3112` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.8435` n `54` status `ready` deltaP `32.8535` edge `0.359` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.8435` n `54` status `ready` deltaP `32.8535` edge `0.359` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3632` n `127` status `ready` deltaP `12.7705` edge `0.1349` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8941` n `127` status `ready` deltaP `6.0552` edge `0.1147` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3474` n `127` status `ready` deltaP `13.0173` edge `0.0467` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2052` n `127` status `ready` deltaP `9.2767` edge `0.008` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3605` n `54` status `ready` deltaP `3.6483` edge `0.0026` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3605` n `54` status `ready` deltaP `3.6483` edge `0.0026` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.4377` n `127` status `ready` deltaP `2.9865` edge `-0.0012` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.4482` n `54` status `ready` deltaP `-2.4524` edge `-0.0027` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4482` n `54` status `ready` deltaP `-2.4524` edge `-0.0027` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.4655` n `54` status `ready` deltaP `2.0016` edge `-0.0008` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4655` n `54` status `ready` deltaP `2.0016` edge `-0.0008` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.476` n `127` status `ready` deltaP `-1.0712` edge `-0.0021` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
