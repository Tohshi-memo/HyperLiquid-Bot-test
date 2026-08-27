# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T12:07:27.275527+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `news_risk_high->unknown_24h` score `51.2273` n `50` status `ready` deltaP `11.5717` edge `4.1918` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.8484` n `50` status `ready` deltaP `37.6235` edge `1.364` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6618` n `50` status `ready` deltaP `26.622` edge `0.8876` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.6705` n `50` status `ready` deltaP `25.6235` edge `0.3112` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.1797` n `50` status `ready` deltaP `43.9413` edge `0.0596` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.06` n `50` status `ready` deltaP `47.3354` edge `0.0318` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.4584` n `131` status `ready` deltaP `24.2251` edge `0.1674` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9443` n `50` status `ready` deltaP `16.8263` edge `0.1688` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.696` n `50` status `ready` deltaP `30.1416` edge `0.0388` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.803` n `128` status `ready` deltaP `5.3217` edge `0.188` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5947` n `50` status `ready` deltaP `21.2515` edge `0.0082` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.2057` n `141` status `ready` deltaP `11.2944` edge `0.0702` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.1594` n `50` status `ready` deltaP `16.8144` edge `0.0124` maxDD `-0.2301`
- `news_risk_high->commodity_1h` score `0.5938` n `50` status `ready` deltaP `15.497` edge `0.0041` maxDD `-0.5024`
- `news_risk_high->equity_4h` score `0.5653` n `50` status `ready` deltaP `17.4634` edge `0.007` maxDD `-2.105`
- `news_risk_high->index_1h` score `0.1366` n `50` status `ready` deltaP `7.6587` edge `0.0004` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0703` n `50` status `ready` deltaP `5.1018` edge `-0.0024` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1731` n `50` status `ready` deltaP `6.8537` edge `-0.007` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1841` n `50` status `ready` deltaP `4.0366` edge `-0.0026` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.5657` n `141` status `ready` deltaP `0.3153` edge `-0.0014` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
