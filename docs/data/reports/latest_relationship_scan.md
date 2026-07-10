# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T11:07:30.244214+00:00`
- Price records: `672`
- Market context records: `6277`
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

- `news_risk_high->crypto_alt_24h` score `15.1513` n `32` status `ready` deltaP `43.058` edge `0.9903` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.967` n `32` status `ready` deltaP `50.692` edge `0.1593` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2109` n `32` status `ready` deltaP `44.1311` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0215` n `32` status `ready` deltaP `16.4901` edge `0.4836` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.5644` n `32` status `ready` deltaP `25.5515` edge `0.0639` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3224` n `32` status `ready` deltaP `27.994` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8352` n `206` status `ready` deltaP `2.9315` edge `0.2342` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3065` n `32` status `ready` deltaP `13.3795` edge `0.125` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.2363` n `194` status `ready` deltaP `-0.9068` edge `0.3623` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7857` n `32` status `ready` deltaP `10.5726` edge `0.0764` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.0994` n `194` status `ready` deltaP `6.1353` edge `0.0591` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.232` n `32` status `ready` deltaP `8.3261` edge `0.0019` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2992` n `206` status `ready` deltaP `1.0523` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.4133` n `191` status `ready` deltaP `16.2829` edge `0.0953` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.4286` n `194` status `ready` deltaP `4.5889` edge `0.028` maxDD `-3.417`
- `market_context_high->commodity_1h` score `-0.5057` n `206` status `ready` deltaP `0.0727` edge `0.0034` maxDD `-0.682`
- `market_context_high->crypto_alt_1h` score `-0.6661` n `206` status `ready` deltaP `7.5083` edge `0.0398` maxDD `-9.3536`
- `news_risk_high->metal_1h` score `-0.678` n `32` status `ready` deltaP `-2.0958` edge `-0.0232` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.8045` n `206` status `ready` deltaP `5.5215` edge `0.0368` maxDD `-9.807`
- `market_context_high->index_1h` score `-0.8214` n `206` status `ready` deltaP `-2.9533` edge `0.0013` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
