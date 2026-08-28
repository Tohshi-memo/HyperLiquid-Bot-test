# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T10:22:29.177315+00:00`
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

- `news_risk_high->unknown_24h` score `53.3521` n `50` status `ready` deltaP `11.6118` edge `4.3686` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.509` n `50` status `ready` deltaP `39.5009` edge `2.3232` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.8866` n `50` status `ready` deltaP `26.0122` edge `0.9104` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4643` n `50` status `ready` deltaP `30.1005` edge `0.3475` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.0235` n `50` status `ready` deltaP `47.3934` edge `0.1069` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9869` n `50` status `ready` deltaP `46.4207` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `2.613` n `50` status `ready` deltaP `19.182` edge `0.1392` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5655` n `50` status `ready` deltaP `28.9012` edge `0.0362` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.5114` n `133` status `ready` deltaP `5.5968` edge `0.2452` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.3944` n `143` status `ready` deltaP `18.7255` edge `0.1154` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.1325` n `55` status `ready` deltaP `11.8209` edge `0.1346` maxDD `-0.8558`
- `news_risk_high->equity_4h` score `1.8703` n `50` status `ready` deltaP `24.4756` edge `0.069` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.423` n `55` status `ready` deltaP `19.2406` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0814` n `55` status `ready` deltaP `15.1987` edge `0.0193` maxDD `-0.4409`
- `market_context_high->metal_24h` score `1.0536` n `133` status `ready` deltaP `17.0626` edge `0.1093` maxDD `-3.1535`
- `market_context_high->unknown_1h` score `0.9293` n `143` status `ready` deltaP `8.6041` edge `0.0651` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.4473` n `55` status `ready` deltaP `13.0158` edge `0.0026` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3158` n `55` status `ready` deltaP `6.663` edge `0.0045` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.2012` n `50` status `ready` deltaP `10.5122` edge `-0.0002` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1468` n `50` status `ready` deltaP `7.5427` edge `0.0016` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
