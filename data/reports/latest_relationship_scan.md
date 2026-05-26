# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T01:48:12.816997+00:00`
- Price records: `672`
- Market context records: `1900`
- Flow alert records: `7369`
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

- `market_context_high->crypto_alt_4h` score `7.4095` n `199` status `ready` deltaP `23.1186` edge `0.5778` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.9021` n `199` status `ready` deltaP `27.8672` edge `0.514` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.0173` n `199` status `ready` deltaP `17.5006` edge `0.4205` maxDD `-9.8581`
- `market_context_high->metal_24h` score `2.3954` n `183` status `ready` deltaP `17.808` edge `0.3235` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3742` n `199` status `ready` deltaP `14.4296` edge `0.2111` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.6152` n `183` status `ready` deltaP `12.8756` edge `0.5808` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.4288` n `183` status `ready` deltaP `9.301` edge `0.1799` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6513` n `199` status `ready` deltaP `7.2436` edge `0.1046` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4727` n `199` status `ready` deltaP `6.805` edge `0.1054` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.4171` n `199` status `ready` deltaP `9.7882` edge `0.0784` maxDD `-3.7119`
- `market_context_high->fx_24h` score `0.3234` n `183` status `ready` deltaP `15.699` edge `0.0272` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.058` n `199` status `ready` deltaP `5.2862` edge `0.0393` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.1612` n `183` status `ready` deltaP `9.0619` edge `0.416` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `-0.4026` n `183` status `ready` deltaP `17.8848` edge `0.7058` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.4954` n `199` status `ready` deltaP `6.7305` edge `0.0252` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6371` n `199` status `ready` deltaP `-2.903` edge `0.0009` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6613` n `199` status `ready` deltaP `-0.3054` edge `0.0101` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.7624` n `199` status `ready` deltaP `11.9331` edge `0.1261` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-0.7832` n `199` status `ready` deltaP `2.8383` edge `0.011` maxDD `-3.6151`
- `market_context_high->fx_4h` score `-0.9` n `199` status `ready` deltaP `-3.8194` edge `-0.0011` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
