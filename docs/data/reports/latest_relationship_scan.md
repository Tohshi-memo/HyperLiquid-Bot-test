# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T22:52:27.335146+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7638`

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

- `news_risk_high->unknown_24h` score `720.2988` n `136` status `ready` deltaP `1.2153` edge `60.0168` maxDD `0.0`
- `news_risk_high->index_24h` score `1.4348` n `136` status `ready` deltaP `18.2088` edge `0.0677` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `1.4226` n `136` status `ready` deltaP `14.6446` edge `0.4161` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `0.8944` n `136` status `ready` deltaP `20.1185` edge `0.1259` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.0305` n `139` status `ready` deltaP `16.0456` edge `0.0565` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0384` n `139` status `ready` deltaP `3.2127` edge `0.0044` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0605` n `139` status `ready` deltaP `4.4727` edge `0.0562` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.2041` n `139` status `ready` deltaP `3.2127` edge `0.0277` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7245` n `139` status `ready` deltaP `-0.3059` edge `0.0046` maxDD `-0.7016`
- `news_risk_high->equity_24h` score `-0.8713` n `136` status `ready` deltaP `12.2447` edge `0.1014` maxDD `-11.1179`
- `news_risk_high->fx_4h` score `-1.0357` n `139` status `ready` deltaP `13.0308` edge `0.0017` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.0792` n `139` status `ready` deltaP `-7.3214` edge `-0.0015` maxDD `-1.0436`
- `news_risk_high->crypto_major_1h` score `-1.1062` n `139` status `ready` deltaP `-3.595` edge `0.0104` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.1514` n `139` status `ready` deltaP `-2.7932` edge `0.008` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-1.7827` n `139` status `ready` deltaP `1.486` edge `0.1075` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8655` n `139` status `ready` deltaP `-13.7293` edge `0.0018` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.8885` n `139` status `ready` deltaP `-9.7704` edge `-0.0095` maxDD `-3.3986`
- `news_risk_high->crypto_major_24h` score `-2.5465` n `136` status `ready` deltaP `8.9461` edge `0.1716` maxDD `-26.1424`
- `news_risk_high->crypto_major_4h` score `-3.4835` n `139` status `ready` deltaP `-12.4079` edge `-0.0924` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.655` n `139` status `ready` deltaP `-9.7978` edge `0.0026` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
