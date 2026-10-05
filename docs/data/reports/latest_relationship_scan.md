# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T08:37:38.536345+00:00`
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

- `market_context_high->unknown_1h` score `77.0144` n `121` status `ready` deltaP `-0.2957` edge `6.4613` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `56.0875` n `109` status `ready` deltaP `0.4069` edge `4.7098` maxDD `-1.0842`
- `market_context_high->crypto_major_24h` score `10.859` n `78` status `ready` deltaP `29.6607` edge `0.7208` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3143` n `65` status `ready` deltaP `32.5516` edge `0.5795` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1714` n `78` status `ready` deltaP `24.9867` edge `0.493` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7912` n `65` status `ready` deltaP `19.7866` edge `0.4851` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.3421` n `65` status `ready` deltaP `23.6111` edge `0.1211` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.3046` n `109` status `ready` deltaP `14.5558` edge `0.2581` maxDD `-4.047`
- `news_risk_high->equity_24h` score `3.2512` n `65` status `ready` deltaP `11.9018` edge `0.2016` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8987` n `65` status `ready` deltaP `31.9137` edge `0.055` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.4878` n `65` status `ready` deltaP `20.1196` edge `0.1342` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.3777` n `65` status `ready` deltaP `9.4173` edge `0.1709` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0207` n `65` status `ready` deltaP `25.0184` edge `0.0166` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9162` n `65` status `ready` deltaP `17.8588` edge `0.0822` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3125` n `109` status `ready` deltaP `23.9763` edge `0.0252` maxDD `-0.3868`
- `market_context_high->crypto_major_1h` score `1.0652` n `121` status `ready` deltaP `11.8585` edge `0.0986` maxDD `-3.7778`
- `news_risk_high->crypto_alt_1h` score `1.0306` n `65` status `ready` deltaP `2.9226` edge `0.1183` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.562` n `65` status `ready` deltaP `24.9119` edge `0.1091` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.522` n `121` status `ready` deltaP `13.546` edge `0.005` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.3138` n `109` status `ready` deltaP `1.2545` edge `0.1967` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
