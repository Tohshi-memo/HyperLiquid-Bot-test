# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T05:07:23.739651+00:00`
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

- `market_context_high->crypto_alt_4h` score `6.4574` n `117` status `ready` deltaP `16.1547` edge `0.5753` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.376` n `54` status `ready` deltaP `32.0` edge `0.318` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.376` n `54` status `ready` deltaP `32.0` edge `0.318` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.0092` n `117` status `ready` deltaP `20.8151` edge `0.5179` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.0462` n `54` status `ready` deltaP `18.4339` edge `0.3424` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0462` n `54` status `ready` deltaP `18.4339` edge `0.3424` maxDD `-1.9151`
- `market_context_high->unknown_4h` score `4.5922` n `117` status `ready` deltaP `-3.1621` edge `0.4684` maxDD `-1.8373`
- `risk_on_high->crypto_major_4h` score `4.4458` n `54` status `ready` deltaP `33.9205` edge `0.4291` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4458` n `54` status `ready` deltaP `33.9205` edge `0.4291` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6188` n `117` status `ready` deltaP `13.2671` edge `0.1532` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2381` n `117` status `ready` deltaP `6.7097` edge `0.139` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1612` n `117` status `ready` deltaP `12.8505` edge `0.0323` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.3431` n `117` status `ready` deltaP `1.0973` edge `0.0021` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3517` n `54` status `ready` deltaP `2.1513` edge `0.0128` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3517` n `54` status `ready` deltaP `2.1513` edge `0.0128` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.4009` n `117` status `ready` deltaP `7.1153` edge `0.0061` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.475` n `54` status `ready` deltaP `1.7022` edge `0.0009` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.475` n `54` status `ready` deltaP `1.7022` edge `0.0009` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.6203` n `117` status `ready` deltaP `-0.2772` edge `-0.0029` maxDD `-1.3154`
- `risk_on_high->metal_4h` score `-0.6762` n `54` status `ready` deltaP `0.4573` edge `0.0148` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
