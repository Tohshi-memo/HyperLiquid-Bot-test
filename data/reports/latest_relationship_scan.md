# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T17:37:38.219860+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8954`

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

- `market_context_high->crypto_major_24h` score `10.6265` n `56` status `ready` deltaP `31.2004` edge `1.442` maxDD `-18.6774`
- `market_context_high->crypto_alt_24h` score `7.5638` n `56` status `ready` deltaP `19.2212` edge `1.2665` maxDD `-29.3276`
- `risk_on_high->crypto_alt_4h` score `4.263` n `48` status `ready` deltaP `18.6484` edge `0.2757` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.263` n `48` status `ready` deltaP `18.6484` edge `0.2757` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6708` n `48` status `ready` deltaP `33.2826` edge `0.334` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6708` n `48` status `ready` deltaP `33.2826` edge `0.334` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.5611` n `100` status `ready` deltaP `13.7317` edge `0.3501` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.2568` n `100` status `ready` deltaP `17.1159` edge `0.3132` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6412` n `100` status `ready` deltaP `12.3533` edge `0.1495` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.0198` n `48` status `ready` deltaP `6.6866` edge `0.1001` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0198` n `48` status `ready` deltaP `6.6866` edge `0.1001` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.68` n `100` status `ready` deltaP `4.3473` edge `0.104` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4303` n `48` status `ready` deltaP `5.514` edge `0.0837` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4303` n `48` status `ready` deltaP `5.514` edge `0.0837` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `0.2591` n `100` status `ready` deltaP `-3.9268` edge `0.1124` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.007` n `100` status `ready` deltaP `4.3003` edge `0.0035` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1201` n `100` status `ready` deltaP `6.2515` edge `0.0044` maxDD `-0.4868`
- `market_context_high->metal_24h` score `-0.2566` n `56` status `ready` deltaP `6.4732` edge `0.0346` maxDD `-2.5192`
- `market_context_high->metal_4h` score `-0.2994` n `100` status `ready` deltaP `9.0671` edge `0.0099` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3028` n `48` status `ready` deltaP `3.4182` edge `0.0039` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
