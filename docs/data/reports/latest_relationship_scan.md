# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T22:07:17.071976+00:00`
- Price records: `672`
- Market context records: `1361`
- Flow alert records: `5832`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.2972` n `135` status `ready` deltaP `32.4884` edge `1.0047` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6748` n `135` status `ready` deltaP `13.1019` edge `1.1356` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.9542` n `135` status `ready` deltaP `28.507` edge `0.8411` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1449` n `135` status `ready` deltaP `23.1365` edge `0.2998` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8121` n `135` status `ready` deltaP `16.0995` edge `0.3597` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.2363` n `160` status `ready` deltaP `11.753` edge `0.1785` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.1435` n `135` status `ready` deltaP `13.4607` edge `0.0549` maxDD `-0.6147`
- `market_context_high->commodity_24h` score `0.169` n `135` status `ready` deltaP `-9.9074` edge `0.3416` maxDD `-15.9173`
- `market_context_high->metal_4h` score `0.1653` n `160` status `ready` deltaP `12.8963` edge `0.0709` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.0117` n `172` status `ready` deltaP `4.787` edge `0.015` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0219` n `160` status `ready` deltaP `4.6341` edge `0.0752` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0221` n `172` status `ready` deltaP `2.4092` edge `0.0267` maxDD `-1.9017`
- `market_context_high->metal_1h` score `-0.2351` n `172` status `ready` deltaP `6.5555` edge `0.0011` maxDD `-2.9951`
- `market_context_high->fx_1h` score `-0.3362` n `172` status `ready` deltaP `1.1106` edge `-0.004` maxDD `-0.3875`
- `market_context_high->commodity_1h` score `-0.5609` n `172` status `ready` deltaP `0.5466` edge `0.0111` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8633` n `172` status `ready` deltaP `-0.5535` edge `0.0188` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1321` n `172` status `ready` deltaP `-3.2586` edge `-0.0169` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.3838` n `160` status `ready` deltaP `7.8354` edge `0.1644` maxDD `-19.5565`
- `market_context_high->unknown_24h` score `-1.7473` n `135` status `ready` deltaP `-3.9815` edge `0.1539` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `-1.8907` n `160` status `ready` deltaP `1.1433` edge `-0.0229` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
