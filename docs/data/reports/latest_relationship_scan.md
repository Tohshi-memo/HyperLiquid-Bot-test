# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T15:12:55.007301+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `65.0811` n `161` status `ready` deltaP `-23.6898` edge `5.8726` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `28.549` n `32` status `ready` deltaP `-42.1875` edge `4.0164` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `28.549` n `32` status `ready` deltaP `-42.1875` edge `4.0164` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.2866` n `36` status `ready` deltaP `10.0694` edge `0.7447` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6061` n `36` status `ready` deltaP `35.6707` edge `0.3127` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.9106` n `32` status `ready` deltaP `27.7778` edge `0.1407` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.9106` n `32` status `ready` deltaP `27.7778` edge `0.1407` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6844` n `32` status `ready` deltaP `19.1311` edge `0.1144` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6844` n `32` status `ready` deltaP `19.1311` edge `0.1144` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5736` n `36` status `ready` deltaP `15.625` edge `0.1103` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.9662` n `32` status `ready` deltaP `22.0486` edge `0.0353` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9662` n `32` status `ready` deltaP `22.0486` edge `0.0353` maxDD `-0.1418`
- `market_context_high->commodity_24h` score `1.9416` n `161` status `ready` deltaP `17.8399` edge `0.1232` maxDD `-2.4263`
- `news_risk_high->index_4h` score `1.7039` n `36` status `ready` deltaP `19.7662` edge `0.0234` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5028` n `161` status `ready` deltaP `16.7825` edge `0.0772` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.3665` n `36` status `ready` deltaP `6.7865` edge `0.1005` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2263` n `32` status `ready` deltaP `13.2111` edge `0.0374` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2263` n `32` status `ready` deltaP `13.2111` edge `0.0374` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.1563` n `32` status `ready` deltaP `11.6319` edge `0.1863` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.1563` n `32` status `ready` deltaP `11.6319` edge `0.1863` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
