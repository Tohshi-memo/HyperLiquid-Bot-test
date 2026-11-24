# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T16:37:38.177632+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4272`

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

- `market_context_high->unknown_1h` score `32296.3754` n `45` status `ready` deltaP `1.7165` edge `2691.3626` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22113.7891` n `45` status `ready` deltaP `2.7202` edge `1842.8115` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1061.4204` n `31` status `ready` deltaP `1.9316` edge `88.4564` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `860.8416` n `31` status `ready` deltaP `3.9388` edge `71.7162` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.4251` n `31` status `ready` deltaP `49.4792` edge `2.7889` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.2765` n `31` status `ready` deltaP `41.1458` edge `2.6654` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5903` n `31` status `ready` deltaP `47.0486` edge `2.4022` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.0967` n `31` status `ready` deltaP `41.2355` edge `0.6773` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.0955` n `31` status `ready` deltaP `24.4738` edge `0.8485` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.411` n `31` status `ready` deltaP `32.9564` edge `0.6126` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.8602` n `31` status `ready` deltaP `15.711` edge `0.9165` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.3889` n `31` status `ready` deltaP `53.6907` edge `0.1873` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.2147` n `31` status `ready` deltaP `38.8889` edge `0.1753` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.56` n `31` status `ready` deltaP `19.0892` edge `0.1881` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9339` n `31` status `ready` deltaP `32.0417` edge `0.0569` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.9133` n `45` status `ready` deltaP `35.271` edge `0.0361` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6223` n `31` status `ready` deltaP `11.807` edge `0.3036` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5812` n `31` status `ready` deltaP `30.6452` edge `0.0193` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.28` n `31` status `ready` deltaP `11.3579` edge `0.2523` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6614` n `31` status `ready` deltaP `31.0797` edge `0.0337` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
