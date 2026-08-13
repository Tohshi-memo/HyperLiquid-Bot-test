# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T21:37:24.380866+00:00`
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

- `market_context_high->unknown_24h` score `89.3996` n `151` status `ready` deltaP `-27.1179` edge `7.922` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7209` n `32` status `ready` deltaP `-41.6667` edge `4.676` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7209` n `32` status `ready` deltaP `-41.6667` edge `4.676` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.541` n `36` status `ready` deltaP `10.0694` edge `0.7659` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5855` n `36` status `ready` deltaP `35.5183` edge `0.312` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.6569` n `32` status `ready` deltaP `32.2917` edge `0.1728` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6569` n `32` status `ready` deltaP `32.2917` edge `0.1728` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.953` n `32` status `ready` deltaP `20.8079` edge `0.1256` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.953` n `32` status `ready` deltaP `20.8079` edge `0.1256` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.6473` n `151` status `ready` deltaP `21.6957` edge `0.1563` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.3607` n `36` status `ready` deltaP `14.5833` edge `0.0995` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.626` n `32` status `ready` deltaP `18.5764` edge `0.0301` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.626` n `32` status `ready` deltaP `18.5764` edge `0.0301` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6069` n `36` status `ready` deltaP `19.004` edge `0.0204` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.6012` n `151` status `ready` deltaP `17.5173` edge `0.0805` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.4325` n `36` status `ready` deltaP `6.7865` edge `0.106` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3318` n `32` status `ready` deltaP `14.1093` edge `0.0402` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3318` n `32` status `ready` deltaP `14.1093` edge `0.0402` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2974` n `32` status `ready` deltaP `12.5` edge `0.1986` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2974` n `32` status `ready` deltaP `12.5` edge `0.1986` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
