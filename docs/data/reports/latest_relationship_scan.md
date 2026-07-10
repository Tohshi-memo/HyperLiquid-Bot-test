# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T12:52:30.965619+00:00`
- Price records: `672`
- Market context records: `6284`
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

- `news_risk_high->crypto_alt_24h` score `15.2001` n `32` status `ready` deltaP `43.1434` edge `0.9938` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9661` n `32` status `ready` deltaP `50.6066` edge `0.1598` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1987` n `32` status `ready` deltaP `43.9787` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0885` n `32` status `ready` deltaP `16.5782` edge `0.4916` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.7118` n `32` status `ready` deltaP `25.9695` edge `0.0734` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3476` n `32` status `ready` deltaP `28.2934` edge `0.0209` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5816` n `206` status `ready` deltaP `0.9171` edge `0.2265` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3595` n `32` status `ready` deltaP `13.8286` edge `0.1288` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8426` n `32` status `ready` deltaP `11.1714` edge `0.0797` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.668` n `194` status `ready` deltaP `-1.9959` edge `0.3222` maxDD `-11.925`
- `market_context_high->equity_4h` score `0.241` n `194` status `ready` deltaP `6.1353` edge `0.0709` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.2362` n `194` status `ready` deltaP `5.315` edge `0.0306` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.2947` n `32` status `ready` deltaP `7.3765` edge `0.0002` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.3049` n `184` status `ready` deltaP `18.0534` edge `0.0974` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.4472` n `206` status `ready` deltaP `0.7441` edge `0.0038` maxDD `-0.682`
- `market_context_high->fx_1h` score `-0.5164` n `206` status `ready` deltaP `0.3808` edge `-0.001` maxDD `-0.5659`
- `news_risk_high->metal_1h` score `-0.6959` n `32` status `ready` deltaP `-2.3952` edge `-0.0235` maxDD `-1.6464`
- `market_context_high->commodity_4h` score `-0.7347` n `194` status `ready` deltaP `-2.1341` edge `0.0101` maxDD `-1.2054`
- `market_context_high->metal_1h` score `-0.7484` n `206` status `ready` deltaP `2.4592` edge `-0.001` maxDD `-1.8877`
- `market_context_high->crypto_alt_1h` score `-0.7929` n `206` status `ready` deltaP `6.1653` edge `0.0325` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
