# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T09:07:28.817099+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8300`

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

- `market_context_high->unknown_1h` score `73.7412` n `123` status `ready` deltaP `-0.7996` edge `6.1919` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `58.3833` n `111` status `ready` deltaP `-0.7924` edge `4.9162` maxDD `-1.6513`
- `market_context_high->crypto_major_24h` score `10.9339` n `80` status `ready` deltaP `29.7569` edge `0.7264` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3263` n `65` status `ready` deltaP `32.5516` edge `0.5805` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1607` n `80` status `ready` deltaP `25.2431` edge `0.4904` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8092` n `65` status `ready` deltaP `19.7866` edge `0.4866` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.4736` n `111` status `ready` deltaP `15.0187` edge `0.2691` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3433` n `65` status `ready` deltaP `23.6111` edge `0.1212` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2114` n `65` status `ready` deltaP `11.5545` edge `0.2006` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9145` n `65` status `ready` deltaP `32.0662` edge `0.0553` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5144` n `65` status `ready` deltaP `20.272` edge `0.1354` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.3753` n `65` status `ready` deltaP `9.4173` edge `0.1707` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0339` n `65` status `ready` deltaP `25.1681` edge `0.0167` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9078` n `65` status `ready` deltaP `17.8588` edge `0.0815` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3519` n `111` status `ready` deltaP `24.4686` edge `0.0252` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.027` n `65` status `ready` deltaP `2.9226` edge `0.118` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.9172` n `123` status `ready` deltaP `10.7432` edge `0.0937` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.8509` n `123` status `ready` deltaP `14.0548` edge `0.0056` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.5534` n `65` status `ready` deltaP `24.9119` edge `0.108` maxDD `-10.9169`
- `market_context_high->crypto_alt_4h` score `0.5241` n `111` status `ready` deltaP `1.9488` edge `0.2096` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
