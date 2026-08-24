# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T19:52:24.956335+00:00`
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

- `news_risk_high->unknown_24h` score `45.4932` n `51` status `ready` deltaP `11.8056` edge `3.7124` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.8839` n `51` status `ready` deltaP `40.237` edge `0.8985` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8327` n `51` status `ready` deltaP `23.9538` edge `0.9143` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.3704` n `51` status `ready` deltaP `48.9481` edge `0.1364` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.0268` n `97` status `ready` deltaP `6.651` edge `0.3205` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `3.8958` n `51` status `ready` deltaP `26.7755` edge `0.2232` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6005` n `51` status `ready` deltaP `16.784` edge `0.2186` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3808` n `51` status `ready` deltaP `39.7597` edge `0.0301` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6282` n `130` status `ready` deltaP `18.9915` edge `0.0499` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2709` n `51` status `ready` deltaP `17.2948` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9834` n `51` status `ready` deltaP `18.3427` edge `0.0402` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9725` n `51` status `ready` deltaP `14.0064` edge `0.0274` maxDD `-0.1788`
- `news_risk_high->metal_24h` score `0.4306` n `51` status `ready` deltaP `25.817` edge `-0.132` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.2938` n `51` status `ready` deltaP `9.2873` edge `-0.0066` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.2165` n `130` status `ready` deltaP `11.63` edge `-0.0136` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.1983` n `51` status `ready` deltaP `8.3744` edge `0.0049` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0576` n `130` status `ready` deltaP `11.3542` edge `-0.026` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1286` n `51` status `ready` deltaP `1.8933` edge `-0.0068` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2095` n `51` status `ready` deltaP `6.7582` edge `-0.0094` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4147` n `130` status `ready` deltaP `2.8604` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
