# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T02:22:16.496383+00:00`
- Price records: `672`
- Market context records: `1903`
- Flow alert records: `7376`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.5035` n `199` status `ready` deltaP `23.4235` edge `0.5836` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.9635` n `199` status `ready` deltaP `28.0197` edge `0.5181` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.8885` n `199` status `ready` deltaP `17.1958` edge `0.4118` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.4018` n `199` status `ready` deltaP `14.4296` edge `0.2134` maxDD `-5.0894`
- `market_context_high->metal_24h` score `2.1995` n `184` status `ready` deltaP `17.3536` edge `0.3102` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.5541` n `184` status `ready` deltaP `12.9529` edge `0.5752` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.3362` n `184` status `ready` deltaP `9.0429` edge `0.1739` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6525` n `199` status `ready` deltaP `7.2436` edge `0.1047` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4727` n `199` status `ready` deltaP `6.805` edge `0.1054` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.4255` n `199` status `ready` deltaP `9.7882` edge `0.0791` maxDD `-3.7119`
- `market_context_high->fx_24h` score `0.2813` n `184` status `ready` deltaP `15.2476` edge `0.0267` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0652` n `199` status `ready` deltaP `5.2862` edge `0.0387` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.2762` n `184` status `ready` deltaP `8.7485` edge `0.4085` maxDD `-33.1875`
- `market_context_high->metal_1h` score `-0.5024` n `199` status `ready` deltaP `6.7305` edge `0.0243` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-0.5885` n `184` status `ready` deltaP `17.4215` edge `0.6934` maxDD `-62.3533`
- `market_context_high->fx_1h` score `-0.6285` n `199` status `ready` deltaP `-2.7533` edge `0.001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6793` n `199` status `ready` deltaP `-0.4551` edge `0.0096` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.76` n `199` status `ready` deltaP `11.9331` edge `0.1263` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-0.8396` n `199` status `ready` deltaP `2.5389` edge `0.0083` maxDD `-3.6151`
- `market_context_high->fx_4h` score `-0.8802` n `199` status `ready` deltaP `-3.5145` edge `-0.0006` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
