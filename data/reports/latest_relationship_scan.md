# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T11:52:29.932037+00:00`
- Price records: `672`
- Market context records: `6280`
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

- `news_risk_high->crypto_alt_24h` score `15.1597` n `32` status `ready` deltaP `43.058` edge `0.991` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9706` n `32` status `ready` deltaP `50.692` edge `0.1596` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2109` n `32` status `ready` deltaP `44.1311` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0386` n `32` status `ready` deltaP `16.4901` edge `0.4858` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.6346` n `32` status `ready` deltaP `25.7245` edge `0.0686` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3224` n `32` status `ready` deltaP `27.994` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7575` n `206` status `ready` deltaP `2.2601` edge `0.2322` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.319` n `32` status `ready` deltaP `13.5292` edge `0.1256` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.1151` n `194` status `ready` deltaP `-0.9068` edge `0.3522` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7997` n `32` status `ready` deltaP `10.7223` edge `0.0772` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.157` n `194` status `ready` deltaP `6.1353` edge `0.0639` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2684` n `32` status `ready` deltaP `7.8071` edge `0.0007` maxDD `-2.3058`
- `market_context_high->metal_4h` score `-0.306` n `194` status `ready` deltaP `4.5889` edge `0.0288` maxDD `-2.89`
- `market_context_high->metal_24h` score `-0.3839` n `188` status `ready` deltaP `16.7581` edge `0.0959` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.4603` n `206` status `ready` deltaP `1.0523` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.4668` n `206` status `ready` deltaP `0.4084` edge `0.0044` maxDD `-0.682`
- `news_risk_high->metal_1h` score `-0.6959` n `32` status `ready` deltaP `-2.3952` edge `-0.0235` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.6976` n `206` status `ready` deltaP `7.1725` edge `0.038` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.7484` n `206` status `ready` deltaP `2.4592` edge `-0.001` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.8016` n `206` status `ready` deltaP `-2.6176` edge `0.0016` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
