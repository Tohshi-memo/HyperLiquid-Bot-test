# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T06:37:32.258528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7862`

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

- `news_risk_high->unknown_24h` score `599.4516` n `139` status `ready` deltaP `1.2153` edge `49.9462` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `3.6257` n `139` status `ready` deltaP `16.7891` edge `0.5854` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.0104` n `139` status `ready` deltaP `21.3242` edge `0.0949` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `1.1853` n `139` status `ready` deltaP `15.6924` edge `0.2498` maxDD `-11.1179`
- `news_risk_high->metal_24h` score `1.1022` n `139` status `ready` deltaP `20.3013` edge `0.142` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `1.0253` n `139` status `ready` deltaP `19.8566` edge `0.114` maxDD `-9.2079`
- `news_risk_high->crypto_major_24h` score `0.9111` n `139` status `ready` deltaP `12.2202` edge `0.4379` maxDD `-26.1424`
- `news_risk_high->crypto_alt_1h` score `0.3065` n `139` status `ready` deltaP `5.6703` edge `0.0788` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.1353` n `139` status `ready` deltaP `5.1588` edge `0.0059` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.0692` n `139` status `ready` deltaP `4.7097` edge `0.0405` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `-0.2478` n `139` status `ready` deltaP `5.297` edge `0.21` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `-0.5855` n `139` status `ready` deltaP `0.8917` edge `0.0082` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.7066` n `139` status `ready` deltaP `1.6275` edge `0.0156` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9013` n `139` status `ready` deltaP `-1.9483` edge `0.0257` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1586` n `139` status `ready` deltaP `-8.6687` edge `-0.0027` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2293` n `139` status `ready` deltaP `9.982` edge `-0.0028` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.655` n `139` status `ready` deltaP `-12.0525` edge `0.0176` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9719` n `139` status `ready` deltaP `-10.968` edge `-0.0122` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.6655` n `139` status `ready` deltaP `-8.9018` edge `-0.0109` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6186` n `139` status `ready` deltaP `-9.4929` edge `0.0036` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
