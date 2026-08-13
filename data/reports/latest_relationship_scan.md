# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T02:52:32.259261+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11840`

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

- `news_risk_high->equity_4h` score `7.0774` n `36` status `ready` deltaP `38.2622` edge `0.3347` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.3224` n `32` status `ready` deltaP `19.4444` edge `0.0639` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.3224` n `32` status `ready` deltaP `19.4444` edge `0.0639` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2877` n `32` status `ready` deltaP `15.7774` edge `0.1037` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2877` n `32` status `ready` deltaP `15.7774` edge `0.1037` maxDD `-0.1258`
- `news_risk_high->index_4h` score `2.0646` n `36` status `ready` deltaP `23.1199` edge `0.0311` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.0193` n `32` status `ready` deltaP `15.9722` edge `0.268` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.0193` n `32` status `ready` deltaP `15.9722` edge `0.268` maxDD `-6.2481`
- `risk_on_high->fx_24h` score `1.8225` n `32` status `ready` deltaP `20.3125` edge `0.0349` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8225` n `32` status `ready` deltaP `20.3125` edge `0.0349` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.5787` n `36` status `ready` deltaP `7.9841` edge `0.1102` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.1904` n `32` status `ready` deltaP `13.0614` edge `0.0354` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1904` n `32` status `ready` deltaP `13.0614` edge `0.0354` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.1061` n `161` status `ready` deltaP `13.4288` edge `0.0665` maxDD `-2.1077`
- `risk_on_high->fx_4h` score `1.0814` n `32` status `ready` deltaP `12.4238` edge `0.0214` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0814` n `32` status `ready` deltaP `12.4238` edge `0.0214` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.9164` n `161` status `ready` deltaP `11.3921` edge `0.0301` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `0.3534` n `161` status `ready` deltaP `9.5065` edge `0.0464` maxDD `-2.4263`
- `news_risk_high->fx_4h` score `0.2365` n `36` status `ready` deltaP `7.9099` edge `-0.0005` maxDD `-0.0863`
- `risk_on_high->index_1h` score `0.2338` n `32` status `ready` deltaP `8.9072` edge `0.0081` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
