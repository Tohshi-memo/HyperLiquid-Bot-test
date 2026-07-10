# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T12:07:30.293679+00:00`
- Price records: `672`
- Market context records: `6281`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `15.1621` n `32` status `ready` deltaP `43.058` edge `0.9912` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9718` n `32` status `ready` deltaP `50.692` edge `0.1597` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2109` n `32` status `ready` deltaP `44.1311` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0418` n `32` status `ready` deltaP `16.4901` edge `0.4862` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.6526` n `32` status `ready` deltaP `25.7245` edge `0.0701` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3224` n `32` status `ready` deltaP `27.994` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.721` n `206` status `ready` deltaP `1.9243` edge `0.2314` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3205` n `32` status `ready` deltaP `13.5292` edge `0.1258` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.0539` n `194` status `ready` deltaP `-0.9068` edge `0.3471` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.8114` n `32` status `ready` deltaP `10.872` edge `0.0777` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.1774` n `194` status `ready` deltaP `6.1353` edge `0.0656` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2699` n `32` status `ready` deltaP `7.8071` edge `0.0005` maxDD `-2.3058`
- `market_context_high->metal_4h` score `-0.2879` n `194` status `ready` deltaP `4.5889` edge `0.029` maxDD `-2.7204`
- `market_context_high->metal_24h` score `-0.3632` n `187` status `ready` deltaP `17.0966` edge `0.0963` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.4364` n `206` status `ready` deltaP `0.7441` edge `0.0047` maxDD `-0.682`
- `market_context_high->fx_1h` score `-0.4615` n `206` status `ready` deltaP `1.0523` edge `-0.0009` maxDD `-0.5659`
- `news_risk_high->metal_1h` score `-0.7037` n `32` status `ready` deltaP `-2.5449` edge `-0.0235` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7204` n `206` status `ready` deltaP `2.7949` edge `-0.0009` maxDD `-1.8877`
- `market_context_high->crypto_alt_1h` score `-0.7229` n `206` status `ready` deltaP `6.8368` edge `0.037` maxDD `-9.3536`
- `market_context_high->index_1h` score `-0.8221` n `206` status `ready` deltaP `-2.9533` edge `0.0012` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
