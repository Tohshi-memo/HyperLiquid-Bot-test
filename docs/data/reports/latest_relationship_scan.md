# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T03:07:25.184556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7628`

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

- `news_risk_high->unknown_24h` score `591.1488` n `139` status `ready` deltaP `1.2153` edge `49.2543` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.1473` n `139` status `ready` deltaP `14.3585` edge `0.4784` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.6504` n `139` status `ready` deltaP `18.8936` edge `0.0811` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9126` n `139` status `ready` deltaP `20.3013` edge `0.1262` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.4322` n `139` status `ready` deltaP `17.7224` edge `0.0788` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `0.1002` n `139` status `ready` deltaP `4.9218` edge `0.0666` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0562` n `139` status `ready` deltaP `4.2606` edge `0.0053` maxDD `-0.3214`
- `news_risk_high->equity_24h` score `-0.0015` n `139` status `ready` deltaP `13.2618` edge `0.1671` maxDD `-11.1179`
- `news_risk_high->equity_1h` score `-0.0051` n `139` status `ready` deltaP `4.2606` edge `0.0373` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.6298` n `139` status `ready` deltaP `0.4426` edge `0.0075` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.9313` n `139` status `ready` deltaP `-0.5066` edge `0.0111` maxDD `-1.493`
- `news_risk_high->crypto_major_24h` score `-0.9802` n `139` status `ready` deltaP `9.7896` edge `0.2965` maxDD `-26.1424`
- `news_risk_high->crypto_major_1h` score `-1.0003` n `139` status `ready` deltaP `-2.6968` edge `0.018` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1407` n `139` status `ready` deltaP `-8.3693` edge `-0.0024` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1511` n `139` status `ready` deltaP `11.2015` edge `-0.0009` maxDD `-3.0414`
- `news_risk_high->crypto_alt_4h` score `-1.2981` n `139` status `ready` deltaP `3.1628` edge `0.1367` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.7675` n `139` status `ready` deltaP `-13.1196` edge `0.0103` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9602` n `139` status `ready` deltaP `-10.8183` edge `-0.0117` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.2882` n `139` status `ready` deltaP `-11.0359` edge `-0.0765` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5228` n `139` status `ready` deltaP `-8.7307` edge `0.0065` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
