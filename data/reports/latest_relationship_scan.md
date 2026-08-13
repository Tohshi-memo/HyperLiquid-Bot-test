# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T13:07:31.365032+00:00`
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

- `market_context_high->unknown_24h` score `46.6527` n `161` status `ready` deltaP `-23.6898` edge `4.3369` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `16.5705` n `32` status `ready` deltaP `-42.1875` edge `2.4807` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `16.5705` n `32` status `ready` deltaP `-42.1875` edge `2.4807` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `8.6899` n `30` status `ready` deltaP `6.7361` edge `0.7172` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.9556` n `36` status `ready` deltaP `36.8902` edge `0.3337` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.6255` n `32` status `ready` deltaP `26.3889` edge `0.1262` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.6255` n `32` status `ready` deltaP `26.3889` edge `0.1262` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.5728` n `32` status `ready` deltaP `18.2165` edge `0.1112` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.5728` n `32` status `ready` deltaP `18.2165` edge `0.1112` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5697` n `30` status `ready` deltaP `16.1458` edge `0.1065` maxDD `0.0`
- `risk_on_high->fx_24h` score `2.0525` n `32` status `ready` deltaP `22.9167` edge `0.0367` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0525` n `32` status `ready` deltaP `22.9167` edge `0.0367` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.8447` n `36` status `ready` deltaP `20.9857` edge `0.027` maxDD `-0.0546`
- `market_context_high->commodity_24h` score `1.6565` n `161` status `ready` deltaP `16.451` edge `0.1087` maxDD `-2.4263`
- `news_risk_high->equity_1h` score `1.5727` n `36` status `ready` deltaP `7.6847` edge `0.1117` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.3913` n `161` status `ready` deltaP `15.8679` edge `0.074` maxDD `-2.1077`
- `risk_on_high->crypto_major_24h` score `1.3498` n `32` status `ready` deltaP `12.8472` edge `0.203` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3498` n `32` status `ready` deltaP `12.8472` edge `0.203` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.1844` n `32` status `ready` deltaP `12.762` edge `0.0369` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1844` n `32` status `ready` deltaP `12.762` edge `0.0369` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
