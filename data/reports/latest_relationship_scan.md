# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T10:52:28.887811+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11608`

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

- `news_risk_high->unknown_24h` score `53.3965` n `50` status `ready` deltaP `11.6118` edge `4.3723` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.6724` n `50` status `ready` deltaP `39.8475` edge `2.3345` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.937` n `50` status `ready` deltaP `26.0122` edge `0.9146` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4679` n `50` status `ready` deltaP `30.1005` edge `0.3478` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.9597` n `50` status `ready` deltaP `47.0468` edge `0.1039` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9601` n `50` status `ready` deltaP `46.1159` edge `0.0316` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `2.7378` n `50` status `ready` deltaP `19.182` edge `0.1496` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5619` n `50` status `ready` deltaP `28.9012` edge `0.0359` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.3638` n `133` status `ready` deltaP `5.5968` edge `0.2329` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.2809` n `141` status `ready` deltaP `18.537` edge `0.1072` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.0957` n `56` status `ready` deltaP `12.2754` edge `0.1285` maxDD `-0.8558`
- `news_risk_high->equity_4h` score `1.8643` n `50` status `ready` deltaP `24.4756` edge `0.0685` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.4696` n `56` status `ready` deltaP `19.7926` edge `0.0075` maxDD `-0.0257`
- `market_context_high->metal_24h` score `1.3662` n `133` status `ready` deltaP `18.2197` edge `0.1193` maxDD `-3.1535`
- `news_risk_high->equity_1h` score `1.1303` n `56` status `ready` deltaP `15.7507` edge `0.0197` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.9364` n `141` status `ready` deltaP `8.1974` edge `0.0684` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.4859` n `56` status `ready` deltaP `13.6976` edge `0.003` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3746` n `56` status `ready` deltaP `7.2926` edge `0.0052` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.1806` n `50` status `ready` deltaP `10.3598` edge `-0.0009` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1322` n `50` status `ready` deltaP `7.3902` edge `0.0014` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
