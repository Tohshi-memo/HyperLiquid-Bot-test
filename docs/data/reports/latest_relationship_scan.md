# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T10:52:30.800239+00:00`
- Price records: `672`
- Market context records: `7977`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11787`

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

- `market_context_high->equity_24h` score `16.169` n `82` status `ready` deltaP `23.8651` edge `1.3225` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0912` n `82` status `ready` deltaP `35.8752` edge `0.4351` maxDD `0.0`
- `market_context_high->equity_4h` score `6.5448` n `96` status `ready` deltaP `25.6775` edge `0.4635` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.9548` n `82` status `ready` deltaP `28.4002` edge `0.2935` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.7012` n `96` status `ready` deltaP `28.1377` edge `0.0735` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5561` n `96` status `ready` deltaP `22.9421` edge `0.1223` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6832` n `102` status `ready` deltaP `14.1936` edge `0.1274` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.12` n `82` status `ready` deltaP `8.7018` edge `0.1526` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.0688` n `82` status `ready` deltaP `24.4537` edge `0.0348` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.0687` n `96` status `ready` deltaP `9.1463` edge `0.1398` maxDD `-3.9374`
- `market_context_high->index_1h` score `1.0507` n `102` status `ready` deltaP `16.3752` edge `0.0214` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.8562` n `96` status `ready` deltaP `9.9085` edge `0.1771` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.704` n `102` status `ready` deltaP `10.1855` edge `0.0286` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5771` n `102` status `ready` deltaP `11.1659` edge `0.0406` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0944` n `102` status `ready` deltaP `-0.2319` edge `0.0327` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2557` n `102` status `ready` deltaP `0.4416` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.6507` n `96` status `ready` deltaP `2.5556` edge `0.0035` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.727` n `102` status `ready` deltaP `0.7596` edge `-0.0039` maxDD `-1.9395`
- `market_context_high->commodity_4h` score `-0.9773` n `96` status `ready` deltaP `2.0785` edge `0.0079` maxDD `-3.589`
- `market_context_high->unknown_1h` score `-2.0139` n `102` status `ready` deltaP `5.8677` edge `-0.1646` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
