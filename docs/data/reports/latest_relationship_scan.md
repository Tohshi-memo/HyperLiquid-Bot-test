# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T03:52:19.265052+00:00`
- Price records: `672`
- Market context records: `1909`
- Flow alert records: `7394`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->crypto_alt_4h` score `7.783` n `199` status `ready` deltaP `24.3381` edge `0.6008` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.1963` n `199` status `ready` deltaP `28.9343` edge `0.5314` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9129` n `199` status `ready` deltaP `17.5006` edge `0.4118` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.5853` n `199` status `ready` deltaP `15.3442` edge `0.2226` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.7668` n `186` status `ready` deltaP `16.4595` edge `0.2801` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.4619` n `186` status `ready` deltaP `13.1048` edge `0.5665` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.1121` n `186` status `ready` deltaP `8.1766` edge `0.161` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.7289` n `201` status `ready` deltaP `7.958` edge `0.1063` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.5346` n `199` status `ready` deltaP `10.7029` edge `0.0821` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.4973` n `201` status `ready` deltaP `7.0069` edge `0.1061` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.1585` n `186` status `ready` deltaP `14.0121` edge `0.0247` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0388` n `201` status `ready` deltaP `5.4965` edge `0.0395` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.4119` n `186` status `ready` deltaP `8.6581` edge `0.3978` maxDD `-33.1875`
- `market_context_high->metal_1h` score `-0.5366` n `201` status `ready` deltaP `6.2673` edge `0.023` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6226` n `201` status `ready` deltaP `-2.6395` edge `0.001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6735` n `201` status `ready` deltaP `-0.3679` edge `0.0095` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.694` n `199` status `ready` deltaP `11.9331` edge `0.1318` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.8225` n `199` status `ready` deltaP `-2.5999` edge `0.0007` maxDD `-1.1056`
- `market_context_high->crypto_major_24h` score `-0.9062` n `186` status `ready` deltaP `16.5099` edge `0.673` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-0.9659` n `201` status `ready` deltaP `1.8292` edge `0.0025` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
