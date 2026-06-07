# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T03:22:21.816985+00:00`
- Price records: `672`
- Market context records: `3139`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7126`

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

- `market_context_high->commodity_24h` score `14.4526` n `106` status `ready` deltaP `48.1066` edge `0.9265` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9819` n `106` status `ready` deltaP `21.4786` edge `0.9041` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7355` n `106` status `ready` deltaP `10.0727` edge `2.3068` maxDD `-71.142`
- `market_context_high->index_24h` score `6.4224` n `106` status `ready` deltaP `30.5293` edge `0.8753` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.2607` n `106` status `ready` deltaP `10.8556` edge `1.3155` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8632` n `142` status `ready` deltaP `18.6448` edge `0.1601` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1498` n `146` status `ready` deltaP `4.1322` edge `0.0272` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3954` n `146` status `ready` deltaP `6.0557` edge `0.1219` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4645` n `106` status `ready` deltaP `5.3328` edge `-0.0015` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.4922` n `146` status `ready` deltaP `3.8512` edge `0.0175` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8036` n `146` status `ready` deltaP `3.6379` edge `0.0213` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9546` n `146` status `ready` deltaP `3.3754` edge `0.0814` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1275` n `146` status `ready` deltaP `-10.6185` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.2016` n `142` status `ready` deltaP `11.5725` edge `0.0597` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.5364` n `142` status `ready` deltaP `-14.9562` edge `-0.0088` maxDD `-1.411`
- `market_context_high->unknown_4h` score `-1.9121` n `142` status `ready` deltaP `5.112` edge `0.0288` maxDD `-14.7778`
- `market_context_high->crypto_alt_4h` score `-2.0261` n `142` status `ready` deltaP `19.1429` edge `0.4171` maxDD `-58.6918`
- `market_context_high->metal_1h` score `-2.0504` n `146` status `ready` deltaP `-4.1547` edge `-0.0038` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.948` n `142` status `ready` deltaP `12.8864` edge `0.0667` maxDD `-36.7784`
- `market_context_high->unknown_1h` score `-3.0998` n `146` status `ready` deltaP `2.0589` edge `-0.0694` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
