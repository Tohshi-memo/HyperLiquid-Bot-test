# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T19:52:28.477775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7458`

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

- `news_risk_high->unknown_24h` score `2673.366` n `139` status `ready` deltaP `1.2153` edge `222.7724` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `9.5671` n `139` status `ready` deltaP `25.296` edge `1.0238` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `6.0878` n `139` status `ready` deltaP `24.8938` edge `0.597` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `5.984` n `139` status `ready` deltaP `21.4216` edge `0.7993` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.2637` n `139` status `ready` deltaP `30.5256` edge `0.138` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.359` n `139` status `ready` deltaP `25.8017` edge `0.1855` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `2.3234` n `139` status `ready` deltaP `22.9055` edge `0.2264` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.7175` n `139` status `ready` deltaP `7.5836` edge `0.2752` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6651` n `139` status `ready` deltaP `7.0176` edge `0.0997` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.484` n `139` status `ready` deltaP `7.1049` edge `0.0591` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4563` n `139` status `ready` deltaP `8.7516` edge `0.0087` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1879` n `139` status `ready` deltaP `6.5056` edge `0.0263` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5412` n `139` status `ready` deltaP `1.1911` edge `0.0099` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5677` n `139` status `ready` deltaP `0.4469` edge `0.0525` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1812` n `139` status `ready` deltaP `-9.1178` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2397` n `139` status `ready` deltaP `9.6771` edge `-0.0021` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4809` n `139` status `ready` deltaP `-9.9184` edge `0.0257` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8663` n `139` status `ready` deltaP `-5.5481` edge `0.0692` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0458` n `139` status `ready` deltaP `-12.1656` edge `-0.0137` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8116` n `139` status `ready` deltaP `-11.1697` edge `-0.0013` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
