# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T02:07:24.147394+00:00`
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

- `market_context_high->unknown_24h` score `90.7634` n `150` status `ready` deltaP `-28.2361` edge `8.0431` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.4555` n `32` status `ready` deltaP `-42.3611` edge `4.6466` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.4555` n `32` status `ready` deltaP `-42.3611` edge `4.6466` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6934` n `36` status `ready` deltaP `10.0694` edge `0.7786` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6663` n `36` status `ready` deltaP `35.8232` edge `0.3167` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7385` n `32` status `ready` deltaP `32.2917` edge `0.1796` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7385` n `32` status `ready` deltaP `32.2917` edge `0.1796` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9882` n `32` status `ready` deltaP `21.1128` edge `0.1265` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9882` n `32` status `ready` deltaP `21.1128` edge `0.1265` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.8114` n `150` status `ready` deltaP `22.2917` edge `0.166` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.2899` n `36` status `ready` deltaP `14.5833` edge `0.0936` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.6266` n `150` status `ready` deltaP `17.6545` edge `0.0817` maxDD `-2.1077`
- `news_risk_high->index_4h` score `1.5062` n `36` status `ready` deltaP `18.0894` edge `0.0181` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.478` n `36` status `ready` deltaP `7.0859` edge `0.1078` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.333` n `32` status `ready` deltaP `14.1093` edge `0.0403` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.333` n `32` status `ready` deltaP `14.1093` edge `0.0403` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.3208` n `32` status `ready` deltaP `15.4514` edge `0.0255` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.3208` n `32` status `ready` deltaP `15.4514` edge `0.0255` maxDD `-0.1418`
- `risk_on_high->fx_4h` score `1.0049` n `32` status `ready` deltaP `11.6616` edge `0.0201` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0049` n `32` status `ready` deltaP `11.6616` edge `0.0201` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
