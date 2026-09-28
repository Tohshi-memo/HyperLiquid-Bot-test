# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T06:22:26.993750+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7838`

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

- `news_risk_high->unknown_24h` score `591.0636` n `139` status `ready` deltaP `1.2153` edge `49.2472` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `3.4978` n `139` status `ready` deltaP `16.6155` edge `0.5759` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.9845` n `139` status `ready` deltaP `21.1506` edge `0.0939` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `1.1054` n `139` status `ready` deltaP `15.5188` edge `0.2443` maxDD `-11.1179`
- `news_risk_high->metal_24h` score `1.089` n `139` status `ready` deltaP `20.3013` edge `0.1409` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.9891` n `139` status `ready` deltaP `19.7041` edge `0.112` maxDD `-9.2079`
- `news_risk_high->crypto_major_24h` score `0.7628` n `139` status `ready` deltaP `12.0466` edge `0.4267` maxDD `-26.1424`
- `news_risk_high->crypto_alt_1h` score `0.3257` n `139` status `ready` deltaP `5.82` edge `0.0794` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.1221` n `139` status `ready` deltaP `5.0091` edge `0.0058` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.0524` n `139` status `ready` deltaP `4.56` edge `0.0401` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `-0.3272` n `139` status `ready` deltaP `5.1445` edge `0.2044` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `-0.5855` n `139` status `ready` deltaP `0.8917` edge `0.0082` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.7223` n `139` status `ready` deltaP `1.4751` edge `0.0153` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.8904` n `139` status `ready` deltaP `-1.7986` edge `0.0261` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1586` n `139` status `ready` deltaP `-8.6687` edge `-0.0027` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2198` n `139` status `ready` deltaP `10.1344` edge `-0.0026` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.6653` n `139` status `ready` deltaP `-12.2049` edge `0.0173` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9726` n `139` status `ready` deltaP `-10.968` edge `-0.0123` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.7132` n `139` status `ready` deltaP `-9.0542` edge `-0.016` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6004` n `139` status `ready` deltaP `-9.3405` edge `0.0041` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
