# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T06:22:29.518554+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7370`

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

- `news_risk_high->unknown_24h` score `2621.1504` n `139` status `ready` deltaP `1.2153` edge `218.4211` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.746` n `139` status `ready` deltaP `32.5877` edge `1.4901` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.6244` n `139` status `ready` deltaP `32.1855` edge `0.8431` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.9817` n `139` status `ready` deltaP `27.498` edge `1.0086` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0295` n `139` status `ready` deltaP `36.602` edge `0.1613` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7004` n `139` status `ready` deltaP `30.0235` edge `0.2937` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5123` n `139` status `ready` deltaP `27.4785` edge `0.1871` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.3345` n `139` status `ready` deltaP `9.5653` edge `0.3134` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8608` n `141` status `ready` deltaP `7.7388` edge `0.1112` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6832` n `141` status `ready` deltaP `8.9045` edge `0.0637` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4913` n `141` status `ready` deltaP `9.0542` edge `0.0096` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0831` n `139` status `ready` deltaP `7.7251` edge `0.0269` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4725` n `141` status `ready` deltaP `1.3314` edge `0.0588` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.531` n `141` status `ready` deltaP `1.2284` edge `0.0105` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3256` n `139` status `ready` deltaP `8.61` edge `-0.006` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4537` n `139` status `ready` deltaP `-9.1562` edge `0.0241` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7799` n `139` status `ready` deltaP `-4.7859` edge `0.0752` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8804` n `141` status `ready` deltaP `-9.7879` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0392` n `141` status `ready` deltaP `-12.0089` edge `-0.0139` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.9519` n `139` status `ready` deltaP `-12.0844` edge `-0.0069` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
