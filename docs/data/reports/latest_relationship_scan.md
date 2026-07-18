# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T05:22:35.600649+00:00`
- Price records: `672`
- Market context records: `7106`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.39` n `151` status `ready` deltaP `15.9001` edge `0.014` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1157` n `151` status `ready` deltaP `0.0773` edge `0.0457` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.141` n `151` status `ready` deltaP `4.5406` edge `0.0031` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3594` n `151` status `ready` deltaP `1.4197` edge `0.0309` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5297` n `151` status `ready` deltaP `4.3681` edge `0.0382` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.605` n `151` status `ready` deltaP `-1.3513` edge `-0.0066` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8464` n `151` status `ready` deltaP `-4.1371` edge `-0.0193` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3624` n `151` status `ready` deltaP `-4.2794` edge `-0.0426` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.5323` n `151` status `ready` deltaP `-6.2167` edge `0.0052` maxDD `-4.4825`
- `market_context_high->metal_1h` score `-1.5702` n `151` status `ready` deltaP `-7.2888` edge `-0.0057` maxDD `-2.1249`
- `market_context_high->equity_1h` score `-2.056` n `151` status `ready` deltaP `3.4342` edge `-0.0442` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.5517` n `151` status `ready` deltaP `-1.6708` edge `-0.0461` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-2.9958` n `151` status `ready` deltaP `4.557` edge `0.014` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.0446` n `151` status `ready` deltaP `0.526` edge `-0.0153` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.4134` n `151` status `ready` deltaP `-8.17` edge `-0.0991` maxDD `-4.4704`
- `market_context_high->metal_4h` score `-4.3826` n `151` status `ready` deltaP `-8.476` edge `-0.0114` maxDD `-5.4518`
- `market_context_high->fx_24h` score `-4.4747` n `151` status `ready` deltaP `-10.3614` edge `-0.0211` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-8.7573` n `151` status `ready` deltaP `-1.7232` edge `-0.2242` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-9.1467` n `151` status `ready` deltaP `-25.8819` edge `-0.075` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.8526` n `151` status `ready` deltaP `-25.9072` edge `-0.148` maxDD `-42.6932`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
