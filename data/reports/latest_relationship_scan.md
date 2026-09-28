# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T08:07:29.465992+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7870`

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

- `news_risk_high->unknown_24h` score `739.5768` n `139` status `ready` deltaP `1.2153` edge `61.6233` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.4903` n `139` status `ready` deltaP `17.8308` edge `0.6505` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.155` n `139` status `ready` deltaP `22.3659` edge `0.1` maxDD `-2.2287`
- `news_risk_high->crypto_major_24h` score `1.8008` n `139` status `ready` deltaP `13.2618` edge `0.5051` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `1.7006` n `139` status `ready` deltaP `16.7341` edge `0.2858` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.2533` n `139` status `ready` deltaP `20.7712` edge `0.1269` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.1946` n `139` status `ready` deltaP `20.3013` edge `0.1497` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.4936` n `139` status `ready` deltaP `6.2691` edge `0.0904` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.2538` n `139` status `ready` deltaP `6.2116` edge `0.2457` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.2215` n `139` status `ready` deltaP `5.6079` edge `0.0472` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2144` n `139` status `ready` deltaP `6.057` edge `0.0065` maxDD `-0.3214`
- `news_risk_high->metal_1h` score `-0.546` n `139` status `ready` deltaP `1.1911` edge `0.0095` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.6178` n `139` status `ready` deltaP `2.5422` edge `0.0169` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.7703` n `139` status `ready` deltaP `-1.0501` edge `0.0365` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1671` n `139` status `ready` deltaP `-8.8184` edge `-0.0028` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2626` n `139` status `ready` deltaP `9.3722` edge `-0.003` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.6023` n `139` status `ready` deltaP `-11.4427` edge `0.0203` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9656` n `139` status `ready` deltaP `-10.8183` edge `-0.0124` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.3606` n `139` status `ready` deltaP `-7.9872` edge `0.0221` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.7206` n `139` status `ready` deltaP `-10.4075` edge `0.0012` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
