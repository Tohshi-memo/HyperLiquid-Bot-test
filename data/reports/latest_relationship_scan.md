# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T11:38:42.119303+00:00`
- Price records: `672`
- Market context records: `6179`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.6398` n `32` status `ready` deltaP `42.3848` edge `0.7855` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.133` n `32` status `ready` deltaP `62.628` edge `0.1769` maxDD `0.0`
- `news_risk_high->fx_4h` score `3.9995` n `32` status `ready` deltaP `41.6084` edge `0.0605` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `1.8209` n `32` status `ready` deltaP `15.7956` edge `0.2061` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.773` n `194` status `ready` deltaP `1.1946` edge `0.2406` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2815` n `32` status `ready` deltaP `13.3795` edge `0.1218` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6821` n `32` status `ready` deltaP `8.7762` edge `0.0751` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3557` n `194` status `ready` deltaP `-1.2188` edge `0.291` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.163` n `194` status `ready` deltaP `20.3916` edge `0.1418` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.0399` n `194` status `ready` deltaP `2.759` edge `0.07` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1001` n `32` status `ready` deltaP `9.663` edge `0.0099` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3` n `194` status `ready` deltaP `1.0818` edge `-0.0011` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.3782` n `32` status `ready` deltaP `14.2385` edge `-0.1059` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6466` n `194` status `ready` deltaP `3.7565` edge `0.0108` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7771` n `194` status `ready` deltaP `-2.3288` edge `-0.0046` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7894` n `32` status `ready` deltaP `-3.2934` edge `-0.0295` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.878` n `194` status `ready` deltaP `1.8612` edge `-0.0057` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9216` n `194` status `ready` deltaP `3.5249` edge `0.0336` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9421` n `194` status `ready` deltaP `3.9401` edge `0.0297` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
