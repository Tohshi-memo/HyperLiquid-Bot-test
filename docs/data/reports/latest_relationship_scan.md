# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T19:52:31.917525+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8742`

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

- `market_context_high->unknown_4h` score `38.1779` n `90` status `ready` deltaP `-5.4185` edge `3.2715` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7993` n `62` status `ready` deltaP `37.7498` edge `0.6686` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0826` n `62` status `ready` deltaP `22.5635` edge `0.5742` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.4552` n `62` status `ready` deltaP `10.5034` edge `0.3112` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.1861` n `62` status `ready` deltaP `29.9308` edge `0.1493` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.0877` n `90` status `ready` deltaP `8.316` edge `0.6378` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8837` n `62` status `ready` deltaP `31.9365` edge `0.0536` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4468` n `62` status `ready` deltaP `10.0251` edge `0.1726` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2945` n `90` status `ready` deltaP `15.8143` edge `0.1822` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1094` n `62` status `ready` deltaP `18.0267` edge `0.1154` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9888` n `62` status `ready` deltaP `25.0242` edge `0.0139` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4482` n `62` status `ready` deltaP `20.5577` edge `0.0902` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.203` n `62` status `ready` deltaP `3.6073` edge `0.1281` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `0.9575` n `62` status `ready` deltaP `-8.3935` edge `0.2603` maxDD `-5.6309`
- `market_context_high->metal_24h` score `0.9131` n `90` status `ready` deltaP `19.3887` edge `0.1363` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.9007` n `90` status `ready` deltaP `20.0609` edge `0.016` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7034` n `90` status `ready` deltaP `11.9461` edge `0.0032` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1253` n `90` status `ready` deltaP `9.9534` edge `0.0386` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1245` n `62` status `ready` deltaP `6.6013` edge `0.0082` maxDD `-1.0132`
- `market_context_high->commodity_1h` score `-0.0467` n `90` status `ready` deltaP `4.0818` edge `0.0065` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
