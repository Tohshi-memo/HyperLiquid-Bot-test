# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T07:37:24.003970+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `50.1987` n `51` status `ready` deltaP `17.0139` edge `4.0698` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.2987` n `51` status `ready` deltaP `40.237` edge `1.0164` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9535` n `51` status `ready` deltaP `23.649` edge `0.9264` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7544` n `51` status `ready` deltaP `48.9481` edge `0.1684` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7692` n `51` status `ready` deltaP `27.2328` edge `0.2096` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6341` n `51` status `ready` deltaP `16.9337` edge `0.2204` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.237` n `51` status `ready` deltaP `38.0829` edge `0.0293` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.9888` n `145` status `ready` deltaP `20.7822` edge `0.0584` maxDD `-0.4975`
- `news_risk_high->metal_24h` score `1.7116` n `51` status `ready` deltaP `34.1503` edge `-0.0808` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2422` n `51` status `ready` deltaP `16.9954` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9787` n `51` status `ready` deltaP `18.7918` edge `0.0366` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9715` n `51` status `ready` deltaP `14.1589` edge `0.0263` maxDD `-0.1788`
- `market_context_high->unknown_24h` score `0.3069` n `91` status `ready` deltaP `4.926` edge `0.0434` maxDD `-1.0533`
- `news_risk_high->index_1h` score `0.2753` n `51` status `ready` deltaP `9.8714` edge `0.0048` maxDD `-0.1583`
- `news_risk_high->crypto_alt_24h` score `0.2012` n `51` status `ready` deltaP `23.7847` edge `-0.1418` maxDD `0.0`
- `news_risk_high->commodity_1h` score `0.1919` n `51` status `ready` deltaP `8.5388` edge `-0.0101` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `-0.1224` n `51` status `ready` deltaP `2.043` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1851` n `51` status `ready` deltaP `7.063` edge `-0.0094` maxDD `-0.249`
- `market_context_high->metal_4h` score `-0.1981` n `145` status `ready` deltaP `7.9825` edge `-0.0155` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.2095` n `147` status `ready` deltaP `9.4107` edge `-0.0353` maxDD `-1.5916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
