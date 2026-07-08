# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T19:07:30.770568+00:00`
- Price records: `672`
- Market context records: `6115`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `9.2311` n `30` status `ready` deltaP `36.7361` edge `0.5391` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.9628` n `30` status `ready` deltaP `70.6597` edge `0.1925` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2007` n `32` status `ready` deltaP `43.6738` edge `0.0635` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3416` n `32` status `ready` deltaP `28.1437` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2589` n `32` status `ready` deltaP `13.6789` edge `0.1169` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.9115` n `195` status `ready` deltaP `6.3415` edge `0.1254` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.626` n `32` status `ready` deltaP `8.6265` edge `0.0689` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0134` n `30` status `ready` deltaP `9.2361` edge `0.0273` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3081` n `195` status `ready` deltaP `0.836` edge `-0.0005` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4536` n `30` status `ready` deltaP `14.2709` edge `-0.1124` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6658` n `195` status `ready` deltaP `3.2372` edge `0.0118` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.696` n `195` status `ready` deltaP `-1.54` edge `-0.0031` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.7237` n `195` status `ready` deltaP `0.1896` edge `0.0175` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.7871` n `32` status `ready` deltaP `-3.1437` edge `-0.0302` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8452` n `195` status `ready` deltaP `2.2409` edge `-0.0055` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.92` n `195` status `ready` deltaP `1.2414` edge `0.0202` maxDD `-1.381`
- `market_context_high->crypto_major_1h` score `-0.9391` n `195` status `ready` deltaP `4.4642` edge `0.0266` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9499` n `195` status `ready` deltaP `3.6105` edge `0.0294` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.1435` n `32` status `ready` deltaP `-10.4229` edge `-0.0208` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2862` n `195` status `ready` deltaP `-3.3556` edge `0.0021` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
