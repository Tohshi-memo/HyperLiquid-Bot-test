# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T06:07:17.144023+00:00`
- Price records: `672`
- Market context records: `1919`
- Flow alert records: `7422`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6012`

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

- `market_context_high->crypto_alt_4h` score `7.7322` n `199` status `ready` deltaP `24.0332` edge `0.5986` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2533` n `199` status `ready` deltaP `29.3916` edge `0.5331` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.0035` n `199` status `ready` deltaP `17.958` edge `0.4163` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6775` n `199` status `ready` deltaP `16.1064` edge `0.2252` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.9676` n `192` status `ready` deltaP `13.5416` edge `0.5224` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.8867` n `192` status `ready` deltaP `13.8889` edge `0.2239` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.8669` n `210` status `ready` deltaP `9.1289` edge `0.11` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.7063` n `210` status `ready` deltaP `8.2849` edge `0.115` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.5829` n `192` status `ready` deltaP `6.0764` edge `0.1309` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.5284` n `199` status `ready` deltaP `10.5504` edge `0.0826` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.0624` n `192` status `ready` deltaP `11.8056` edge `0.021` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1212` n `210` status `ready` deltaP `4.9772` edge `0.0361` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.6199` n `210` status `ready` deltaP `5.2652` edge `0.019` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6341` n `210` status `ready` deltaP `0.2296` edge `0.0088` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6439` n `210` status `ready` deltaP `-3.0339` edge `0.0009` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.6628` n `199` status `ready` deltaP `11.9331` edge `0.1344` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.7869` n `199` status `ready` deltaP `-1.9901` edge `0.0012` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.0499` n `192` status `ready` deltaP `7.1181` edge `0.3549` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.1798` n `210` status `ready` deltaP `1.4956` edge `-0.0131` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.9199` n `192` status `ready` deltaP `13.8889` edge `0.606` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
