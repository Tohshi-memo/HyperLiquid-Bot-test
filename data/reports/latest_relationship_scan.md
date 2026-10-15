# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T10:07:26.858204+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9448`

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

- `risk_on_high->commodity_24h` score `7.9375` n `54` status `ready` deltaP `41.2892` edge `0.3862` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9375` n `54` status `ready` deltaP `41.2892` edge `0.3862` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.7089` n `123` status `ready` deltaP `18.9024` edge `0.6608` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.6651` n `54` status `ready` deltaP `22.2448` edge `0.4518` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.6651` n `54` status `ready` deltaP `22.2448` edge `0.4518` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.0927` n `123` status `ready` deltaP `20.2236` edge `0.5288` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.6184` n `54` status `ready` deltaP `34.2254` edge `0.4492` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6184` n `54` status `ready` deltaP `34.2254` edge `0.4492` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.841` n `123` status `ready` deltaP `13.6288` edge `0.169` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1124` n `123` status `ready` deltaP `5.3491` edge `0.1376` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1417` n `123` status `ready` deltaP `11.3313` edge `0.0408` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3203` n `54` status `ready` deltaP `1.1034` edge `0.0238` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3203` n `54` status `ready` deltaP `1.1034` edge `0.0238` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3239` n `54` status `ready` deltaP `4.9568` edge `0.0277` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3239` n `54` status `ready` deltaP `4.9568` edge `0.0277` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3483` n `123` status `ready` deltaP `-0.6702` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->commodity_24h` score `-0.4304` n `116` status `ready` deltaP `12.8409` edge `0.1477` maxDD `-12.0788`
- `market_context_high->index_1h` score `-0.4991` n `123` status `ready` deltaP `1.4832` edge `0.0009` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5047` n `123` status `ready` deltaP `6.0124` edge `0.0048` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5115` n `54` status `ready` deltaP `0.9537` edge `0.0012` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
