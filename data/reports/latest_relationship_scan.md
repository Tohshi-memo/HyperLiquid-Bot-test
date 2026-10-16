# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T10:52:27.472004+00:00`
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

- `risk_on_high->commodity_24h` score `8.1072` n `54` status `ready` deltaP `43.3798` edge `0.3864` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.1072` n `54` status `ready` deltaP `43.3798` edge `0.3864` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.8168` n `127` status `ready` deltaP `17.5376` edge `0.5426` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.6479` n `127` status `ready` deltaP `21.273` edge `0.461` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.8358` n `54` status `ready` deltaP `19.9582` edge `0.3146` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.8358` n `54` status `ready` deltaP `19.9582` edge `0.3146` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.9228` n `54` status `ready` deltaP `33.4632` edge `0.3651` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.9228` n `54` status `ready` deltaP `33.4632` edge `0.3651` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3811` n `127` status `ready` deltaP `12.9202` edge `0.1354` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8737` n `127` status `ready` deltaP `5.9055` edge `0.114` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2512` n `127` status `ready` deltaP `11.9502` edge `0.0458` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2064` n `127` status `ready` deltaP `9.2767` edge `0.0079` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3613` n `54` status `ready` deltaP `3.6483` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3613` n `54` status `ready` deltaP `3.6483` edge `0.0025` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.4377` n `127` status `ready` deltaP `2.9865` edge `-0.0012` maxDD `-1.3195`
- `market_context_high->fx_1h` score `-0.4432` n `127` status `ready` deltaP `-0.4706` edge `-0.0019` maxDD `-0.4757`
- `risk_on_high->index_1h` score `-0.4482` n `54` status `ready` deltaP `-2.4524` edge `-0.0027` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4482` n `54` status `ready` deltaP `-2.4524` edge `-0.0027` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.4788` n `54` status `ready` deltaP `1.8519` edge `-0.0015` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4788` n `54` status `ready` deltaP `1.8519` edge `-0.0015` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
