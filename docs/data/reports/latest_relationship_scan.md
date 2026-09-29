# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T20:07:43.405523+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7156`

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

- `news_risk_high->unknown_24h` score `2591.9961` n `139` status `ready` deltaP `1.7361` edge `215.9881` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.2221` n `139` status `ready` deltaP `29.9835` edge `1.4638` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.277` n `139` status `ready` deltaP `31.491` edge `0.8178` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.2511` n `139` status `ready` deltaP `24.7202` edge `0.8829` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.9849` n `139` status `ready` deltaP `37.47` edge `0.1518` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.451` n `139` status `ready` deltaP `30.3707` edge `0.2706` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `3.0851` n `142` status `ready` deltaP `30.5716` edge `0.2134` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.1374` n `142` status `ready` deltaP `11.682` edge `0.3662` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0571` n `142` status `ready` deltaP `8.3179` edge `0.1237` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7186` n `142` status `ready` deltaP `8.301` edge `0.0705` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5078` n `142` status `ready` deltaP `9.0495` edge `0.011` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.212` n `142` status `ready` deltaP `10.6643` edge `0.0319` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.259` n `142` status `ready` deltaP `3.188` edge `0.0738` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5145` n `142` status `ready` deltaP `1.0141` edge `0.0133` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2311` n `142` status `ready` deltaP `-6.63` edge `0.0358` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.2827` n `142` status `ready` deltaP `-2.2437` edge `0.122` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.2921` n `142` status `ready` deltaP `9.2838` edge `-0.0062` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8325` n `142` status `ready` deltaP `-9.1444` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8456` n `142` status `ready` deltaP `-9.0052` edge `-0.0091` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2995` n `142` status `ready` deltaP `-9.3073` edge `0.0091` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
