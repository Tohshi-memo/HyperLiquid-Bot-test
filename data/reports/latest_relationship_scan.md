# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T11:37:33.358940+00:00`
- Price records: `672`
- Market context records: `6279`
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

- `news_risk_high->crypto_alt_24h` score `15.1549` n `32` status `ready` deltaP `43.058` edge `0.9906` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9694` n `32` status `ready` deltaP `50.692` edge `0.1595` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2109` n `32` status `ready` deltaP `44.1311` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0308` n `32` status `ready` deltaP `16.4901` edge `0.4848` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.6178` n `32` status `ready` deltaP `25.7245` edge `0.0672` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3224` n `32` status `ready` deltaP `27.994` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7999` n `206` status `ready` deltaP `2.5958` edge `0.2335` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3088` n `32` status `ready` deltaP `13.3795` edge `0.1253` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.1583` n `194` status `ready` deltaP `-0.9068` edge `0.3558` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7888` n `32` status `ready` deltaP `10.5726` edge `0.0768` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.1402` n `194` status `ready` deltaP `6.1353` edge `0.0625` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2571` n `32` status `ready` deltaP `7.9801` edge `0.001` maxDD `-2.3058`
- `market_context_high->metal_4h` score `-0.3185` n `194` status `ready` deltaP `4.5889` edge `0.0284` maxDD `-2.9862`
- `market_context_high->metal_24h` score `-0.3931` n `189` status `ready` deltaP `16.5962` edge `0.0958` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.4603` n `206` status `ready` deltaP `1.0523` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.4985` n `206` status `ready` deltaP `0.0727` edge `0.004` maxDD `-0.682`
- `market_context_high->crypto_alt_1h` score `-0.6723` n `206` status `ready` deltaP `7.5083` edge `0.039` maxDD `-9.3536`
- `news_risk_high->metal_1h` score `-0.6873` n `32` status `ready` deltaP `-2.2455` edge `-0.0234` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7777` n `206` status `ready` deltaP `2.1234` edge `-0.0012` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.8016` n `206` status `ready` deltaP `-2.6176` edge `0.0016` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
