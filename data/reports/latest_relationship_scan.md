# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T11:22:27.936428+00:00`
- Price records: `672`
- Market context records: `6278`
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
- `news_risk_high->fx_24h` score `5.9682` n `32` status `ready` deltaP `50.692` edge `0.1594` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2109` n `32` status `ready` deltaP `44.1311` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0254` n `32` status `ready` deltaP `16.4901` edge `0.4841` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.5848` n `32` status `ready` deltaP `25.5515` edge `0.0656` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3224` n `32` status `ready` deltaP `27.994` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8316` n `206` status `ready` deltaP `2.9315` edge `0.2339` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3081` n `32` status `ready` deltaP `13.3795` edge `0.1252` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.1967` n `194` status `ready` deltaP `-0.9068` edge `0.359` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7865` n `32` status `ready` deltaP `10.5726` edge `0.0765` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.127` n `194` status `ready` deltaP `6.1353` edge `0.0614` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2449` n `32` status `ready` deltaP `8.1531` edge `0.0014` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2992` n `206` status `ready` deltaP `1.0523` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.3716` n `194` status `ready` deltaP `4.5889` edge `0.0283` maxDD `-3.1893`
- `market_context_high->metal_24h` score `-0.4045` n `190` status `ready` deltaP `16.4378` edge `0.0954` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.5021` n `206` status `ready` deltaP `0.0727` edge `0.0037` maxDD `-0.682`
- `market_context_high->crypto_alt_1h` score `-0.6684` n `206` status `ready` deltaP `7.5083` edge `0.0395` maxDD `-9.3536`
- `news_risk_high->metal_1h` score `-0.6865` n `32` status `ready` deltaP `-2.2455` edge `-0.0233` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7932` n `206` status `ready` deltaP `2.1234` edge `-0.0013` maxDD `-1.983`
- `market_context_high->index_1h` score `-0.8023` n `206` status `ready` deltaP `-2.6176` edge `0.0015` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
