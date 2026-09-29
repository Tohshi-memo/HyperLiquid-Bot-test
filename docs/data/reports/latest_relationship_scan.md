# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T20:52:37.099514+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7174`

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

- `news_risk_high->unknown_24h` score `2596.7524` n `139` status `ready` deltaP `1.9097` edge `216.3833` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.8792` n `139` status `ready` deltaP `29.4627` edge `1.4387` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.089` n `139` status `ready` deltaP `30.9702` edge `0.8056` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.0423` n `139` status `ready` deltaP `24.7202` edge `0.8655` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.9156` n `139` status `ready` deltaP `36.9492` edge `0.1495` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.3421` n `139` status `ready` deltaP `29.8499` edge `0.265` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `3.1009` n `142` status `ready` deltaP `30.724` edge `0.2137` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.2254` n `142` status `ready` deltaP `11.9869` edge `0.3715` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0834` n `142` status `ready` deltaP `8.6173` edge `0.1239` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7294` n `142` status `ready` deltaP `8.4507` edge `0.0704` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4946` n `142` status `ready` deltaP `8.8998` edge `0.0109` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1694` n `142` status `ready` deltaP `10.207` edge `0.0314` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.259` n `142` status `ready` deltaP `3.188` edge `0.0738` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.554` n `142` status `ready` deltaP `0.565` edge `0.013` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2397` n `142` status `ready` deltaP `-6.63` edge `0.0347` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.2481` n `142` status `ready` deltaP `-1.9388` edge `0.1244` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3175` n `142` status `ready` deltaP `8.8265` edge `-0.0064` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8199` n `142` status `ready` deltaP `-8.5561` edge `-0.0088` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8313` n `142` status `ready` deltaP `-9.1444` edge `-0.0036` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2617` n `142` status `ready` deltaP `-8.85` edge `0.0109` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
