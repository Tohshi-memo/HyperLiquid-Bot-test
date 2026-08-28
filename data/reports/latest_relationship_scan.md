# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T09:52:26.054316+00:00`
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

- `news_risk_high->unknown_24h` score `53.3005` n `50` status `ready` deltaP `11.6118` edge `4.3643` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.2497` n `50` status `ready` deltaP `39.1542` edge `2.3039` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.842` n `50` status `ready` deltaP `25.8598` edge `0.9077` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4451` n `50` status `ready` deltaP `30.1005` edge `0.3459` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.0932` n `50` status `ready` deltaP `47.74` edge `0.1104` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9735` n `50` status `ready` deltaP `46.2683` edge `0.0317` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.6854` n `133` status `ready` deltaP `5.5968` edge `0.2597` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.5679` n `50` status `ready` deltaP `28.9012` edge `0.0364` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.5193` n `53` status `ready` deltaP `14.3345` edge `0.15` maxDD `-0.8495`
- `market_context_high->unknown_4h` score `2.4161` n `145` status `ready` deltaP `18.7564` edge `0.117` maxDD `-0.5894`
- `news_risk_high->crypto_major_24h` score `2.3489` n `50` status `ready` deltaP `18.8354` edge `0.1195` maxDD `-2.6128`
- `news_risk_high->equity_4h` score `1.8351` n `50` status `ready` deltaP `24.1707` edge `0.0681` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.6124` n `53` status `ready` deltaP `21.5484` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1632` n `53` status `ready` deltaP `15.7694` edge `0.021` maxDD `-0.3355`
- `market_context_high->unknown_1h` score `0.9022` n `145` status `ready` deltaP `8.7001` edge `0.0622` maxDD `-1.6015`
- `market_context_high->metal_24h` score `0.7145` n `133` status `ready` deltaP `15.9054` edge `0.0976` maxDD `-3.1944`
- `news_risk_high->commodity_1h` score `0.4618` n `53` status `ready` deltaP `13.3121` edge `0.0022` maxDD `-0.5397`
- `news_risk_high->metal_4h` score `0.2436` n `50` status `ready` deltaP `10.8171` edge `0.0013` maxDD `-0.249`
- `news_risk_high->metal_1h` score `0.1865` n `53` status `ready` deltaP `5.3158` edge `0.0027` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.1334` n `50` status `ready` deltaP `7.3902` edge `0.0015` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
