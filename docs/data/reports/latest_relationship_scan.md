# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T18:52:27.534109+00:00`
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

- `market_context_high->unknown_24h` score `79.2421` n `157` status `ready` deltaP `-24.8618` edge `7.0605` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6955` n `32` status `ready` deltaP `-41.8403` edge `4.6739` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6955` n `32` status `ready` deltaP `-41.8403` edge `4.6739` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5122` n `36` status `ready` deltaP `10.0694` edge `0.7635` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5761` n `36` status `ready` deltaP `35.6707` edge `0.3102` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.3134` n `32` status `ready` deltaP `30.3819` edge `0.1569` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.3134` n `32` status `ready` deltaP `30.3819` edge `0.1569` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7132` n `32` status `ready` deltaP `19.1311` edge `0.1168` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7132` n `32` status `ready` deltaP `19.1311` edge `0.1168` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5028` n `36` status `ready` deltaP `15.625` edge `0.1044` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.3637` n `157` status `ready` deltaP `20.1908` edge `0.1427` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.8124` n `32` status `ready` deltaP `20.4861` edge `0.0329` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8124` n `32` status `ready` deltaP `20.4861` edge `0.0329` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6507` n `36` status `ready` deltaP `19.4613` edge `0.021` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.556` n `157` status `ready` deltaP `16.8023` edge `0.0815` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.3389` n `36` status `ready` deltaP `6.7865` edge `0.0982` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.2964` n `32` status `ready` deltaP `13.0208` edge `0.195` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2964` n `32` status `ready` deltaP `13.0208` edge `0.195` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2886` n `32` status `ready` deltaP `13.8099` edge `0.0386` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2886` n `32` status `ready` deltaP `13.8099` edge `0.0386` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
