# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T03:22:31.460765+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9843`

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

- `market_context_high->crypto_alt_4h` score `6.5044` n `117` status `ready` deltaP `16.3071` edge `0.5782` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.4636` n `54` status `ready` deltaP `32.0` edge `0.3253` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.4636` n `54` status `ready` deltaP `32.0` edge `0.3253` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.008` n `117` status `ready` deltaP `20.8151` edge `0.5178` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.0932` n `54` status `ready` deltaP `18.5863` edge `0.3453` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0932` n `54` status `ready` deltaP `18.5863` edge `0.3453` maxDD `-1.9151`
- `market_context_high->unknown_4h` score `4.4897` n `117` status `ready` deltaP `-3.6194` edge `0.4629` maxDD `-1.8373`
- `risk_on_high->crypto_major_4h` score `4.445` n `54` status `ready` deltaP `33.9205` edge `0.429` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.445` n `54` status `ready` deltaP `33.9205` edge `0.429` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7051` n `117` status `ready` deltaP `13.7162` edge `0.1574` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2381` n `117` status `ready` deltaP `6.56` edge `0.14` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.279` n `117` status `ready` deltaP `13.9176` edge `0.035` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.3059` n `117` status `ready` deltaP `1.5477` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3516` n `54` status `ready` deltaP `2.0016` edge `0.0138` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3516` n `54` status `ready` deltaP `2.0016` edge `0.0138` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3997` n `117` status `ready` deltaP `7.1153` edge `0.0062` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4742` n `54` status `ready` deltaP `1.7022` edge `0.001` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4742` n `54` status `ready` deltaP `1.7022` edge `0.001` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5996` n `54` status `ready` deltaP `1.5244` edge `0.0175` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5996` n `54` status `ready` deltaP `1.5244` edge `0.0175` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
