# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T02:22:47.598968+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.8524` n `50` status `ready` deltaP `9.5269` edge `28.1791` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.9455` n `50` status `ready` deltaP `8.9939` edge `23.9355` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.565` n `77` status `ready` deltaP `38.3748` edge `1.3122` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0087` n `50` status `ready` deltaP `36.1667` edge `0.8179` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.3075` n `50` status `ready` deltaP `14.9722` edge `0.6801` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `7.0821` n `50` status `ready` deltaP `18.1524` edge `0.5395` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8077` n `50` status `ready` deltaP `15.5793` edge `0.4261` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.6108` n `90` status `ready` deltaP `14.4682` edge `0.3388` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.4584` n `50` status `ready` deltaP `17.6528` edge `0.5119` maxDD `-11.8957`
- `news_risk_high->equity_24h` score `3.1314` n `77` status `ready` deltaP `19.7827` edge `0.4423` maxDD `-7.1509`
- `market_context_high->crypto_major_1h` score `2.9963` n `50` status `ready` deltaP `14.7485` edge `0.1964` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9009` n `50` status `ready` deltaP `32.689` edge `0.0373` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.851` n `50` status `ready` deltaP `13.3054` edge `0.2152` maxDD `-3.6387`
- `news_risk_high->crypto_major_24h` score `2.6841` n `77` status `ready` deltaP `12.6083` edge `0.455` maxDD `-15.8971`
- `news_risk_high->equity_4h` score `2.5549` n `90` status `ready` deltaP `23.1166` edge `0.1284` maxDD `-2.9013`
- `news_risk_high->commodity_24h` score `1.5957` n `77` status `ready` deltaP `25.6922` edge `0.1457` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3595` n `77` status `ready` deltaP `13.2598` edge `0.2133` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.1943` n `77` status `ready` deltaP `16.2203` edge `0.0392` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9214` n `50` status `ready` deltaP `14.7917` edge `0.0766` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
