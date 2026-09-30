# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T01:37:40.216159+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1578.4972` n `136` status `ready` deltaP `1.9097` edge `131.5287` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.487` n `136` status `ready` deltaP `29.0951` edge `1.4019` maxDD `-16.4229`
- `news_risk_high->equity_24h` score `8.6972` n `136` status `ready` deltaP `29.2586` edge `0.7646` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `8.2954` n `136` status `ready` deltaP `24.7447` edge `0.8417` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.8718` n `136` status `ready` deltaP `35.3963` edge `0.1437` maxDD `-1.2285`
- `news_risk_high->metal_24h` score `3.3239` n `136` status `ready` deltaP `27.7574` edge `0.2475` maxDD `-4.4443`
- `news_risk_high->equity_4h` score `2.9053` n `139` status `ready` deltaP `29.3746` edge `0.2064` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.372` n `139` status `ready` deltaP `12.9189` edge `0.3775` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.3283` n `139` status `ready` deltaP `9.9535` edge `0.1354` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8094` n `139` status `ready` deltaP `8.5437` edge `0.0728` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5181` n `139` status `ready` deltaP `9.1425` edge `0.011` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0208` n `139` status `ready` deltaP `8.2492` edge `0.0286` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.174` n `139` status `ready` deltaP `3.8319` edge `0.0804` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5433` n `139` status `ready` deltaP `0.5342` edge `0.0141` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2549` n `139` status `ready` deltaP `-1.8896` edge `0.1232` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.3294` n `139` status `ready` deltaP `-8.2175` edge `0.0286` maxDD `-3.2072`
- `news_risk_high->fx_4h` score `-1.4277` n `139` status `ready` deltaP `6.976` edge `-0.0082` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8707` n `139` status `ready` deltaP `-9.4128` edge `-0.0096` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8843` n `139` status `ready` deltaP `-9.6875` edge `-0.0044` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.278` n `139` status `ready` deltaP `-9.2977` edge `0.0118` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
