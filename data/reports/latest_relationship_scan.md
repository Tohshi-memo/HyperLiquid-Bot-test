# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T11:07:30.879773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9006`

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

- `risk_on_high->commodity_24h` score `7.9327` n `54` status `ready` deltaP `41.2892` edge `0.3858` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9327` n `54` status `ready` deltaP `41.2892` edge `0.3858` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5989` n `123` status `ready` deltaP `18.2927` edge `0.6557` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.5552` n `54` status `ready` deltaP `21.6351` edge `0.4467` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.5552` n `54` status `ready` deltaP `21.6351` edge `0.4467` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `5.9551` n `123` status `ready` deltaP `19.6138` edge `0.5214` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.529` n `54` status `ready` deltaP `33.6156` edge `0.4418` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.529` n `54` status `ready` deltaP `33.6156` edge `0.4418` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8206` n `123` status `ready` deltaP `13.6288` edge `0.1673` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.086` n `123` status `ready` deltaP `5.3491` edge `0.1354` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0859` n `123` status `ready` deltaP `10.874` edge `0.0392` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.332` n `123` status `ready` deltaP `-0.3699` edge `-0.0017` maxDD `-0.4047`
- `risk_on_high->crypto_alt_1h` score `-0.3372` n `54` status `ready` deltaP `4.9568` edge `0.026` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3372` n `54` status `ready` deltaP `4.9568` edge `0.026` maxDD `-5.8485`
- `risk_on_high->crypto_major_1h` score `-0.3375` n `54` status `ready` deltaP `1.1034` edge `0.0216` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3375` n `54` status `ready` deltaP `1.1034` edge `0.0216` maxDD `-3.7781`
- `market_context_high->commodity_24h` score `-0.4335` n `116` status `ready` deltaP `12.8409` edge `0.1473` maxDD `-12.0788`
- `market_context_high->index_1h` score `-0.4913` n `123` status `ready` deltaP `1.6334` edge `0.0009` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5047` n `123` status `ready` deltaP `6.0124` edge `0.0048` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5115` n `54` status `ready` deltaP `0.9537` edge `0.0012` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
