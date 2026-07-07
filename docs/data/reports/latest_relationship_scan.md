# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T13:37:28.689602+00:00`
- Price records: `672`
- Market context records: `5986`
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

- `news_risk_high->fx_24h` score `7.434` n `30` status `ready` deltaP `68.0556` edge `0.1658` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.6008` n `30` status `ready` deltaP `34.2361` edge `0.1757` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.0995` n `30` status `ready` deltaP `42.439` edge `0.0633` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1891` n `30` status `ready` deltaP `26.3273` edge `0.0208` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0265` n `235` status `ready` deltaP `7.6181` edge `0.1442` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7959` n `30` status `ready` deltaP `9.8902` edge `0.0828` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1608` n `30` status `ready` deltaP `5.02` edge `0.0333` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0618` n `30` status `ready` deltaP `9.2361` edge `0.0335` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4219` n `30` status `ready` deltaP `1.3872` edge `-0.0267` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4227` n `235` status `ready` deltaP `-0.867` edge `0.0034` maxDD `-1.1447`
- `market_context_high->equity_1h` score `-0.5057` n `235` status `ready` deltaP `3.3023` edge `0.026` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5611` n `235` status `ready` deltaP `1.6709` edge `-0.0032` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.7502` n `235` status `ready` deltaP `-1.4741` edge `-0.001` maxDD `-0.8015`
- `market_context_high->equity_24h` score `-0.9529` n `208` status `ready` deltaP `21.7014` edge `0.3127` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0765` n `30` status `ready` deltaP `-10.0` edge `-0.0199` maxDD `-1.1161`
- `market_context_high->index_1h` score `-1.1489` n `235` status `ready` deltaP `-1.0638` edge `0.0027` maxDD `-1.3078`
- `market_context_high->index_4h` score `-1.1773` n `235` status `ready` deltaP `0.3587` edge `0.0154` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.2016` n `235` status `ready` deltaP `1.876` edge `0.0102` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2682` n `235` status `ready` deltaP `1.1193` edge `0.0052` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.2722` n `235` status `ready` deltaP `-0.4981` edge `-0.0024` maxDD `-5.2568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
