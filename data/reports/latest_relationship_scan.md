# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T12:52:30.893556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11609`

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

- `news_risk_high->unknown_24h` score `53.5621` n `50` status `ready` deltaP `11.6118` edge `4.3861` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.0941` n `50` status `ready` deltaP `41.234` edge `2.3604` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.9486` n `53` status `ready` deltaP `24.7699` edge `0.8448` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4463` n `50` status `ready` deltaP `30.1005` edge `0.346` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.7012` n `50` status `ready` deltaP `45.6603` edge `0.0916` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9181` n `53` status `ready` deltaP `45.5016` edge `0.0322` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.2174` n `50` status `ready` deltaP `19.7019` edge `0.1861` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5313` n `50` status `ready` deltaP `28.7279` edge `0.0345` maxDD `-0.2064`
- `market_context_high->metal_24h` score `2.5308` n `133` status `ready` deltaP `22.8483` edge `0.1605` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.4445` n `133` status `ready` deltaP `18.0314` edge `0.1242` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.1064` n `56` status `ready` deltaP `12.4251` edge `0.1284` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `1.8118` n `133` status `ready` deltaP `5.5968` edge `0.1869` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.4935` n `56` status `ready` deltaP `20.092` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1123` n `56` status `ready` deltaP `15.601` edge `0.0192` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `1.0306` n `133` status `ready` deltaP `7.3499` edge `0.0819` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.9526` n `53` status `ready` deltaP `21.7556` edge `0.0534` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5202` n `56` status `ready` deltaP `14.1467` edge `0.0044` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3495` n `56` status `ready` deltaP `6.9932` edge `0.0051` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.3262` n `53` status `ready` deltaP `11.3696` edge `0.0045` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.0501` n `56` status `ready` deltaP `5.9346` edge `0.0008` maxDD `-0.0486`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
