# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T11:37:30.791619+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7916`

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

- `news_risk_high->unknown_24h` score `1066.092` n `139` status `ready` deltaP `1.2153` edge `88.8329` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.1161` n `139` status `ready` deltaP `19.9141` edge `0.7721` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.4112` n `139` status `ready` deltaP `15.6924` edge `0.6231` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `2.9547` n `139` status `ready` deltaP `19.1646` edge `0.3741` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.4994` n `139` status `ready` deltaP `24.7964` edge `0.1125` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.7406` n `139` status `ready` deltaP `22.7529` edge `0.1543` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.4202` n `139` status `ready` deltaP `20.3013` edge `0.1685` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.8317` n `139` status `ready` deltaP `7.736` edge `0.2837` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6255` n `139` status `ready` deltaP `6.8679` edge `0.0974` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.315` n `139` status `ready` deltaP `7.2546` edge `0.0069` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.279` n `139` status `ready` deltaP `5.9073` edge `0.05` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.4184` n `139` status `ready` deltaP `4.5239` edge `0.0203` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5412` n `139` status `ready` deltaP `1.1911` edge `0.0099` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6971` n `139` status `ready` deltaP `-0.4513` edge `0.0419` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1235` n `139` status `ready` deltaP `-8.0699` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1376` n `139` status `ready` deltaP `11.5064` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4927` n `139` status `ready` deltaP `-10.0708` edge `0.0252` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0388` n `139` status `ready` deltaP `-11.8662` edge `-0.0148` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.0912` n `139` status `ready` deltaP `-6.7677` edge `0.0485` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0089` n `139` status `ready` deltaP `-12.5417` edge `-0.0086` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
