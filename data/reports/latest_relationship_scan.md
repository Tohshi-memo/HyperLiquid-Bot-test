# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T19:41:16.288186+00:00`
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

- `market_context_high->unknown_24h` score `79.2613` n `157` status `ready` deltaP `-24.8618` edge `7.0621` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.708` n `32` status `ready` deltaP `-41.8403` edge `4.6755` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.708` n `32` status `ready` deltaP `-41.8403` edge `4.6755` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6478` n `36` status `ready` deltaP `10.0694` edge `0.7748` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6748` n `36` status `ready` deltaP `35.9756` edge `0.3164` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.3946` n `32` status `ready` deltaP `30.9028` edge `0.1602` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.3946` n `32` status `ready` deltaP `30.9028` edge `0.1602` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7738` n `32` status `ready` deltaP `19.5884` edge `0.1188` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7738` n `32` status `ready` deltaP `19.5884` edge `0.1188` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5016` n `36` status `ready` deltaP `15.625` edge `0.1043` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.445` n `157` status `ready` deltaP `20.7117` edge `0.146` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.7612` n `32` status `ready` deltaP `19.9653` edge `0.0321` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.7612` n `32` status `ready` deltaP `19.9653` edge `0.0321` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6677` n `36` status `ready` deltaP `19.6138` edge `0.0214` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.6166` n `157` status `ready` deltaP `17.2596` edge `0.0835` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.4277` n `36` status `ready` deltaP `6.9362` edge `0.1046` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.3307` n `32` status `ready` deltaP `13.0208` edge `0.1994` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3307` n `32` status `ready` deltaP `13.0208` edge `0.1994` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2707` n `32` status `ready` deltaP `13.6602` edge `0.0381` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2707` n `32` status `ready` deltaP `13.6602` edge `0.0381` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
