# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T09:07:38.994173+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `news_risk_high->unknown_24h` score `2609.0892` n `139` status `ready` deltaP `1.2153` edge `217.416` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.417` n `139` status `ready` deltaP `32.9349` edge `1.5437` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.2211` n `139` status `ready` deltaP `34.0952` edge `0.8801` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.1094` n `139` status `ready` deltaP `27.3243` edge `1.0204` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.2151` n `139` status `ready` deltaP `38.3381` edge `0.1652` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.9137` n `139` status `ready` deltaP `31.7596` edge `0.2999` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5307` n `140` status `ready` deltaP `27.6481` edge `0.1875` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.8967` n `140` status `ready` deltaP `8.2927` edge `0.2854` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8149` n `142` status `ready` deltaP `7.1203` edge `0.1115` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6625` n `142` status `ready` deltaP `8.4507` edge `0.065` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4622` n `142` status `ready` deltaP `8.6004` edge `0.0102` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0536` n `140` status `ready` deltaP `8.0488` edge `0.0272` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4125` n `142` status `ready` deltaP `1.691` edge `0.0641` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5062` n `142` status `ready` deltaP `1.3135` edge `0.012` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3344` n `140` status `ready` deltaP `8.5758` edge `-0.0069` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3983` n `140` status `ready` deltaP `-8.5104` edge `0.0269` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8698` n `140` status `ready` deltaP `-5.0` edge `0.0651` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8948` n `142` status `ready` deltaP `-9.8929` edge `-0.0039` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0684` n `142` status `ready` deltaP `-12.2986` edge `-0.0157` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-4.0658` n `140` status `ready` deltaP `-12.3824` edge `-0.0144` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
