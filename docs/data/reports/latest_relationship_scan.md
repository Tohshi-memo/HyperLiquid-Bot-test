# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T09:52:28.469076+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7906`

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

- `news_risk_high->unknown_24h` score `902.5788` n `139` status `ready` deltaP `1.2153` edge `75.2068` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.4287` n `139` status `ready` deltaP `19.046` edge `0.7206` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `2.6816` n `139` status `ready` deltaP `14.4771` edge `0.5704` maxDD `-26.1424`
- `news_risk_high->index_24h` score `2.323` n `139` status `ready` deltaP `23.5811` edge `0.1059` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `2.3055` n `139` status `ready` deltaP `17.9493` edge `0.3281` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.5029` n `139` status `ready` deltaP `21.6858` edge `0.1416` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.3062` n `139` status `ready` deltaP `20.3013` edge `0.159` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.6834` n `139` status `ready` deltaP `7.1262` edge `0.2754` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6315` n `139` status `ready` deltaP `7.0176` edge `0.0969` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.3413` n `139` status `ready` deltaP `6.5061` edge `0.0512` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2898` n `139` status `ready` deltaP `6.9552` edge `0.0068` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.5144` n `139` status `ready` deltaP `3.6092` edge `0.0184` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5723` n `139` status `ready` deltaP `0.8917` edge `0.0093` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.7088` n `139` status `ready` deltaP `-0.601` edge `0.0414` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.157` n `139` status `ready` deltaP `-8.6687` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1993` n `139` status `ready` deltaP `10.4393` edge `-0.002` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5132` n `139` status `ready` deltaP `-10.3757` edge `0.0246` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0209` n `139` status `ready` deltaP `-11.5668` edge `-0.0145` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1632` n `139` status `ready` deltaP `-7.0725` edge `0.0413` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.8563` n `139` status `ready` deltaP `-11.4746` edge `-0.003` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
