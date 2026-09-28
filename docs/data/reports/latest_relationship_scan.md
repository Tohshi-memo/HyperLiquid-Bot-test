# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T01:37:28.086211+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7656`

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

- `news_risk_high->unknown_24h` score `676.8996` n `137` status `ready` deltaP `1.2153` edge `56.4002` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.9692` n `137` status `ready` deltaP `14.6822` edge `0.4614` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.6151` n `137` status `ready` deltaP `19.0073` edge `0.0774` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.0089` n `137` status `ready` deltaP `21.0995` edge `0.1289` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.226` n `139` status `ready` deltaP `16.9602` edge `0.0667` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0228` n `139` status `ready` deltaP `3.3624` edge `0.0047` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.1106` n `139` status `ready` deltaP `3.6618` edge `0.0325` maxDD `-1.957`
- `news_risk_high->crypto_alt_1h` score `-0.1432` n `139` status `ready` deltaP `4.0236` edge `0.0523` maxDD `-4.2849`
- `news_risk_high->equity_24h` score `-0.236` n `137` status `ready` deltaP `13.2705` edge `0.1475` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.637` n `139` status `ready` deltaP `0.4426` edge `0.0069` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-1.0201` n `139` status `ready` deltaP `-1.4213` edge `0.0098` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-1.0922` n `139` status `ready` deltaP `-3.4453` edge `0.0112` maxDD `-7.2607`
- `news_risk_high->fx_4h` score `-1.0949` n `139` status `ready` deltaP `12.1161` edge `0.0002` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.1235` n `139` status `ready` deltaP `-8.0699` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->crypto_major_24h` score `-1.4091` n `137` status `ready` deltaP `9.7983` edge `0.2607` maxDD `-26.1424`
- `news_risk_high->crypto_alt_4h` score `-1.6113` n `139` status `ready` deltaP `2.2482` edge `0.1167` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8058` n `139` status `ready` deltaP `-13.272` edge `0.0064` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9345` n `139` status `ready` deltaP `-10.3692` edge `-0.0114` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.4293` n `139` status `ready` deltaP `-11.9506` edge `-0.0885` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5872` n `139` status `ready` deltaP `-9.3405` edge `0.0052` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
