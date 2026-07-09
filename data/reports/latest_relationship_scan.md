# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T08:57:15.331124+00:00`
- Price records: `672`
- Market context records: `6168`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.6195` n `32` status `ready` deltaP `42.5514` edge `0.7827` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.3347` n `32` status `ready` deltaP `64.3836` edge `0.182` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0875` n `32` status `ready` deltaP `42.5887` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3348` n `32` status `ready` deltaP `28.1343` edge `0.0209` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7174` n `195` status `ready` deltaP `0.9797` edge `0.2374` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.517` n `32` status `ready` deltaP `15.9675` edge `0.166` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.1744` n `32` status `ready` deltaP `12.6399` edge `0.113` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5842` n `32` status `ready` deltaP `7.8825` edge `0.0685` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3095` n `195` status `ready` deltaP `-1.0474` edge `0.286` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.181` n `195` status `ready` deltaP `20.7833` edge `0.1415` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.0399` n `32` status `ready` deltaP `9.8459` edge `0.0164` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1284` n `195` status `ready` deltaP `2.5982` edge `0.0637` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.3125` n `195` status `ready` deltaP `0.8266` edge `-0.001` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6526` n `195` status `ready` deltaP `3.747` edge `0.0101` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.7067` n `32` status `ready` deltaP `12.4572` edge `-0.1214` maxDD `-0.3101`
- `market_context_high->commodity_1h` score `-0.7123` n `195` status `ready` deltaP `-1.6839` edge `-0.0035` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8215` n `32` status `ready` deltaP `-3.7313` edge `-0.0307` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8982` n `195` status `ready` deltaP `1.6533` edge `-0.006` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9917` n `195` status `ready` deltaP `2.8665` edge `0.029` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.0072` n `195` status `ready` deltaP `-2.7861` edge `0.001` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
