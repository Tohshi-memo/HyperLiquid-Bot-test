# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T23:22:29.617131+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10281`

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

- `risk_on_high->unknown_24h` score `4166.7909` n `117` status `ready` deltaP `20.4861` edge `347.096` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4166.7909` n `117` status `ready` deltaP `20.4861` edge `347.096` maxDD `0.0`
- `market_context_high->unknown_24h` score `2759.6071` n `237` status `ready` deltaP `19.6422` edge `229.8415` maxDD `-0.0819`
- `risk_on_high->crypto_alt_24h` score `9.5081` n `117` status `ready` deltaP `25.414` edge `0.6459` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.5081` n `117` status `ready` deltaP `25.414` edge `0.6459` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8574` n `117` status `ready` deltaP `31.0924` edge `0.318` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8574` n `117` status `ready` deltaP `31.0924` edge `0.318` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.3351` n `117` status `ready` deltaP `21.1005` edge `0.9501` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3351` n `117` status `ready` deltaP `21.1005` edge `0.9501` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `5.2645` n `237` status `ready` deltaP `19.5609` edge `0.3658` maxDD `-2.5998`
- `risk_on_high->crypto_major_4h` score `4.8179` n `117` status `ready` deltaP `25.5238` edge `0.3172` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8179` n `117` status `ready` deltaP `25.5238` edge `0.3172` maxDD `-3.8693`
- `market_context_high->equity_24h` score `2.4813` n `237` status `ready` deltaP `12.3264` edge `0.1246` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.7313` n `117` status `ready` deltaP `12.3264` edge `0.0621` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7313` n `117` status `ready` deltaP `12.3264` edge `0.0621` maxDD `0.0`
- `risk_on_high->index_24h` score `1.5149` n `117` status `ready` deltaP `14.2762` edge `0.0353` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.5149` n `117` status `ready` deltaP `14.2762` edge `0.0353` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.0352` n `117` status `ready` deltaP `4.6958` edge `0.0902` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0352` n `117` status `ready` deltaP `4.6958` edge `0.0902` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.7918` n `237` status `ready` deltaP `9.2454` edge `0.0437` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
