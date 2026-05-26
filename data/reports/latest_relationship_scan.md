# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T18:52:19.458648+00:00`
- Price records: `672`
- Market context records: `1965`
- Flow alert records: `7551`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7565`

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

- `market_context_high->crypto_alt_4h` score `7.2366` n `234` status `ready` deltaP `22.4124` edge `0.5681` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.6652` n `234` status `ready` deltaP `26.0462` edge `0.5064` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4109` n `234` status `ready` deltaP `13.5906` edge `0.3127` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.3464` n `234` status `ready` deltaP `14.668` edge `0.2072` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.3549` n `199` status `ready` deltaP `16.7627` edge `0.5332` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.9932` n `199` status `ready` deltaP `13.8707` edge `0.2329` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.9764` n `234` status `ready` deltaP `9.252` edge `0.1183` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.7896` n `234` status `ready` deltaP `8.2451` edge `0.1222` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.5126` n `199` status `ready` deltaP `12.5491` edge `0.4489` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3673` n `199` status `ready` deltaP `4.1922` edge `0.1255` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.3` n `234` status `ready` deltaP `8.7451` edge `0.0756` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0922` n `234` status `ready` deltaP `5.0988` edge `0.0377` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2346` n `199` status `ready` deltaP `10.1036` edge `0.018` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5909` n `234` status `ready` deltaP `0.6347` edge `0.0097` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6849` n `234` status `ready` deltaP `-3.612` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.8189` n `199` status `ready` deltaP `17.0906` edge `0.6764` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.119` n `234` status `ready` deltaP `-7.6871` edge `-0.0034` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1789` n `234` status `ready` deltaP `3.9959` edge `0.0087` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.6391` n `234` status `ready` deltaP `0.2099` edge `-0.0428` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8216` n `234` status `ready` deltaP `6.9276` edge `0.0712` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
