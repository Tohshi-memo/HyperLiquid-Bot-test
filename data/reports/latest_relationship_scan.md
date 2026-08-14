# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T08:07:29.284706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `90.1294` n `150` status `ready` deltaP `-30.1458` edge `8.003` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.0434` n `32` status `ready` deltaP `-44.2708` edge `4.6065` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.0434` n `32` status `ready` deltaP `-44.2708` edge `4.6065` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0222` n `36` status `ready` deltaP `10.0694` edge `0.806` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.2957` n `36` status `ready` deltaP `39.1768` edge `0.3468` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7582` n `32` status `ready` deltaP `32.1181` edge `0.1824` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7582` n `32` status `ready` deltaP `32.1181` edge `0.1824` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.8311` n `150` status `ready` deltaP `22.1181` edge `0.1688` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.7166` n `32` status `ready` deltaP `18.9787` edge `0.1181` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7166` n `32` status `ready` deltaP `18.9787` edge `0.1181` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.2587` n `36` status `ready` deltaP `14.5833` edge `0.091` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7249` n `36` status `ready` deltaP `20.2235` edge `0.0221` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6746` n `36` status `ready` deltaP `8.7326` edge `0.1132` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.468` n `32` status `ready` deltaP `13.0208` edge `0.217` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.468` n `32` status `ready` deltaP `13.0208` edge `0.217` maxDD `-6.2481`
- `market_context_high->commodity_4h` score `1.3551` n `150` status `ready` deltaP `15.5204` edge `0.0733` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.2431` n `32` status `ready` deltaP `13.2111` edge `0.0388` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2431` n `32` status `ready` deltaP `13.2111` edge `0.0388` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1936` n `32` status `ready` deltaP `14.2361` edge `0.023` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1936` n `32` status `ready` deltaP `14.2361` edge `0.023` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
