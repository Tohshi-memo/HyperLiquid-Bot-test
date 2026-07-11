# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T10:22:29.285127+00:00`
- Price records: `672`
- Market context records: `6381`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11072`

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

- `news_risk_high->crypto_alt_24h` score `14.1637` n `32` status `ready` deltaP `37.6736` edge `0.9439` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3709` n `32` status `ready` deltaP `52.9514` edge `0.1779` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2926` n `32` status `ready` deltaP `17.5347` edge `0.5114` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.2152` n `32` status `ready` deltaP `36.6319` edge `0.1276` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.923` n `32` status `ready` deltaP `40.4726` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3727` n `32` status `ready` deltaP `28.5928` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.517` n `32` status `ready` deltaP `14.7268` edge `0.143` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8574` n `32` status `ready` deltaP `10.7223` edge `0.0846` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4875` n `220` status `ready` deltaP `15.1136` edge `0.0414` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2056` n `227` status `ready` deltaP `-5.558` edge `0.155` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.18` n `220` status `ready` deltaP `9.1852` edge `0.0214` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2513` n `32` status `ready` deltaP `6.6804` edge `-0.031` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2681` n `145` status `ready` deltaP `19.3607` edge `0.0934` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.3992` n `227` status `ready` deltaP `3.5519` edge `0.0029` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.6214` n `227` status `ready` deltaP `-1.5761` edge `0.0028` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.706` n `227` status `ready` deltaP `-0.5922` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7091` n `32` status `ready` deltaP `-2.3952` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.7346` n `32` status `ready` deltaP `0.5208` edge `-0.0105` maxDD `-2.3058`
- `market_context_high->commodity_24h` score `-0.8239` n `145` status `ready` deltaP `-5.6741` edge `0.1186` maxDD `-6.2457`
- `market_context_high->equity_4h` score `-0.8731` n `220` status `ready` deltaP `7.0981` edge `0.0498` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
