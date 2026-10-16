# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T11:52:29.664399+00:00`
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

- `risk_on_high->commodity_24h` score `8.0346` n `54` status `ready` deltaP `42.6829` edge `0.385` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0346` n `54` status `ready` deltaP `42.6829` edge `0.385` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.8036` n `127` status `ready` deltaP `17.5376` edge `0.5415` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.5887` n `127` status `ready` deltaP `20.9681` edge `0.4581` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.8226` n `54` status `ready` deltaP `19.9582` edge `0.3135` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.8226` n `54` status `ready` deltaP `19.9582` edge `0.3135` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.8843` n `54` status `ready` deltaP `33.1583` edge `0.3622` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.8843` n `54` status `ready` deltaP `33.1583` edge `0.3622` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3931` n `127` status `ready` deltaP `12.9202` edge `0.1364` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8761` n `127` status `ready` deltaP `5.9055` edge `0.1142` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.306` n `127` status `ready` deltaP `12.56` edge `0.0463` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2028` n `127` status `ready` deltaP `9.2767` edge `0.0082` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.359` n `54` status `ready` deltaP `3.6483` edge `0.0028` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.359` n `54` status `ready` deltaP `3.6483` edge `0.0028` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.4205` n `127` status `ready` deltaP `3.2868` edge `-0.001` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.431` n `54` status `ready` deltaP `-2.1521` edge `-0.0025` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.431` n `54` status `ready` deltaP `-2.1521` edge `-0.0025` maxDD `-0.7394`
- `market_context_high->fx_1h` score `-0.4674` n `127` status `ready` deltaP `-0.921` edge `-0.002` maxDD `-0.4757`
- `risk_on_high->crypto_major_1h` score `-0.4772` n `54` status `ready` deltaP `1.8519` edge `-0.0013` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4772` n `54` status `ready` deltaP `1.8519` edge `-0.0013` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
