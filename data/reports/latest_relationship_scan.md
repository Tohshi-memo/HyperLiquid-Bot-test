# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T13:29:59.902566+00:00`
- Price records: `672`
- Market context records: `5985`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.4154` n `30` status `ready` deltaP `67.8819` edge `0.1654` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.6339` n `30` status `ready` deltaP `34.4098` edge `0.1773` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.0862` n `30` status `ready` deltaP `42.2866` edge `0.0632` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1891` n `30` status `ready` deltaP `26.3273` edge `0.0208` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0916` n `235` status `ready` deltaP `7.8911` edge `0.1478` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7702` n `30` status `ready` deltaP `9.7405` edge `0.0805` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1327` n `30` status `ready` deltaP `4.8703` edge `0.0307` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0594` n `30` status `ready` deltaP `9.2361` edge `0.0332` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.4073` n `236` status `ready` deltaP `-0.647` edge `0.0039` maxDD `-1.1447`
- `news_risk_high->metal_1h` score `-0.4266` n `30` status `ready` deltaP `1.3872` edge `-0.0273` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4961` n `236` status `ready` deltaP `3.3366` edge `0.027` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5407` n `236` status `ready` deltaP `1.8675` edge `-0.0019` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.7305` n `236` status `ready` deltaP `-1.2433` edge `-0.0009` maxDD `-0.8015`
- `market_context_high->equity_24h` score `-1.0104` n `209` status `ready` deltaP `21.3725` edge `0.3101` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0867` n `30` status `ready` deltaP `-10.1497` edge `-0.0202` maxDD `-1.1161`
- `market_context_high->index_1h` score `-1.1411` n `236` status `ready` deltaP `-0.9972` edge `0.0029` maxDD `-1.3078`
- `market_context_high->index_4h` score `-1.1592` n `235` status `ready` deltaP `0.6319` edge `0.0159` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.187` n `236` status `ready` deltaP `1.9157` edge `0.0118` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2484` n `236` status `ready` deltaP `1.1697` edge `0.0074` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.2944` n `235` status `ready` deltaP `-0.4981` edge `-0.0028` maxDD `-5.4524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
