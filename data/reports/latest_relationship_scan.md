# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T21:37:31.061923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7928`

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

- `news_risk_high->unknown_24h` score `720.1764` n `136` status `ready` deltaP `1.2153` edge `60.0066` maxDD `0.0`
- `news_risk_high->index_24h` score `1.3156` n `136` status `ready` deltaP `17.5143` edge `0.0624` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `1.0986` n `136` status `ready` deltaP `14.6446` edge `0.3891` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `0.807` n `136` status `ready` deltaP `19.2505` edge `0.1244` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `-0.0915` n `139` status `ready` deltaP `15.4358` edge `0.0504` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `-0.0941` n `139` status `ready` deltaP `4.323` edge `0.0544` maxDD `-4.2849`
- `news_risk_high->index_1h` score `-0.0971` n `139` status `ready` deltaP `2.6139` edge `0.0035` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.3084` n `139` status `ready` deltaP `2.4642` edge `0.024` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7485` n `139` status `ready` deltaP `-0.4556` edge `0.0036` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.0428` n `139` status `ready` deltaP `12.8783` edge `0.0018` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.0714` n `139` status `ready` deltaP `-7.1717` edge `-0.0015` maxDD `-1.0436`
- `news_risk_high->equity_24h` score `-1.1751` n `136` status `ready` deltaP `11.8975` edge `0.0784` maxDD `-11.1179`
- `news_risk_high->crypto_major_1h` score `-1.1756` n `139` status `ready` deltaP `-4.1938` edge `0.0055` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.2158` n `139` status `ready` deltaP `-3.403` edge `0.0067` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-1.8141` n `139` status `ready` deltaP `1.3336` edge `0.1059` maxDD `-15.9436`
- `news_risk_high->commodity_1h` score `-1.8971` n `139` status `ready` deltaP `-9.7704` edge `-0.0106` maxDD `-3.3986`
- `news_risk_high->metal_4h` score `-1.8994` n `139` status `ready` deltaP `-14.1867` edge `0.0005` maxDD `-3.6214`
- `news_risk_high->crypto_major_24h` score `-3.2584` n `136` status `ready` deltaP `8.2516` edge `0.1169` maxDD `-26.1424`
- `news_risk_high->crypto_major_4h` score `-3.5815` n `139` status `ready` deltaP `-13.0177` edge `-0.1009` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6188` n `139` status `ready` deltaP `-9.6454` edge `0.0046` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
