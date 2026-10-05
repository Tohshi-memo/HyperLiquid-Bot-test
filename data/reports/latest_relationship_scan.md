# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T10:07:31.162047+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8312`

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

- `market_context_high->unknown_1h` score `69.891` n `124` status `ready` deltaP `-0.6422` edge `5.87` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `19.6185` n `112` status `ready` deltaP `-2.1124` edge `1.7027` maxDD `-2.2991`
- `market_context_high->crypto_major_24h` score `10.8224` n `81` status `ready` deltaP `29.8032` edge `0.7168` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3731` n `65` status `ready` deltaP `32.5516` edge `0.5844` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.8166` n `81` status `ready` deltaP `25.3666` edge `0.4609` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8692` n `65` status `ready` deltaP `19.7866` edge `0.4916` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.3813` n `112` status `ready` deltaP `15.2439` edge `0.2599` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.362` n `65` status `ready` deltaP `23.7847` edge `0.1216` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1378` n `65` status `ready` deltaP `10.8601` edge `0.1991` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9436` n `65` status `ready` deltaP `32.371` edge `0.0557` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5628` n `65` status `ready` deltaP `20.5769` edge `0.1374` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4581` n `65` status `ready` deltaP `9.8664` edge `0.1746` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0471` n `65` status `ready` deltaP `25.3178` edge `0.0168` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8812` n `65` status `ready` deltaP `17.7064` edge `0.0803` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4952` n `112` status `ready` deltaP `26.1106` edge `0.0262` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.0977` n `65` status `ready` deltaP `3.3717` edge `0.1209` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.8635` n `124` status `ready` deltaP `14.2264` edge `0.0055` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.6017` n `124` status `ready` deltaP `9.0352` edge `0.0788` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5308` n `65` status `ready` deltaP `24.9119` edge `0.1051` maxDD `-10.9169`
- `market_context_high->equity_24h` score `0.4721` n `81` status `ready` deltaP `8.3719` edge `-0.0026` maxDD `-0.4427`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
