# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T22:52:29.462194+00:00`
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

- `market_context_high->unknown_24h` score `91.1561` n `150` status `ready` deltaP `-27.5417` edge `8.0712` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7108` n `32` status `ready` deltaP `-41.6667` edge `4.6747` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7108` n `32` status `ready` deltaP `-41.6667` edge `4.6747` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5386` n `36` status `ready` deltaP `10.0694` edge `0.7657` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5465` n `36` status `ready` deltaP `35.061` edge `0.3118` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.6869` n `32` status `ready` deltaP `32.2917` edge `0.1753` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6869` n `32` status `ready` deltaP `32.2917` edge `0.1753` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.981` n `32` status `ready` deltaP `21.1128` edge `0.1259` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.981` n `32` status `ready` deltaP `21.1128` edge `0.1259` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.7598` n `150` status `ready` deltaP `22.2917` edge `0.1617` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.3355` n `36` status `ready` deltaP `14.5833` edge `0.0974` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.6194` n `150` status `ready` deltaP `17.6545` edge `0.0811` maxDD `-2.1077`
- `news_risk_high->index_4h` score `1.5741` n `36` status `ready` deltaP `18.6992` edge `0.0197` maxDD `-0.0546`
- `risk_on_high->fx_24h` score `1.541` n `32` status `ready` deltaP `17.7083` edge `0.0288` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.541` n `32` status `ready` deltaP `17.7083` edge `0.0288` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.4361` n `36` status `ready` deltaP `6.7865` edge `0.1063` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3725` n `32` status `ready` deltaP `14.5584` edge `0.0406` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3725` n `32` status `ready` deltaP `14.5584` edge `0.0406` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2165` n `32` status `ready` deltaP `11.9792` edge `0.1917` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2165` n `32` status `ready` deltaP `11.9792` edge `0.1917` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
