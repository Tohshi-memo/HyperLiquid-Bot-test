# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T19:07:34.560568+00:00`
- Price records: `672`
- Market context records: `6009`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11142`

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

- `news_risk_high->fx_24h` score `7.6055` n `30` status `ready` deltaP `68.9236` edge `0.1743` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1749` n `30` status `ready` deltaP `43.2012` edge `0.0645` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7504` n `30` status `ready` deltaP `30.4167` edge `0.1303` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2442` n `30` status `ready` deltaP `26.9261` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1161` n `218` status `ready` deltaP `7.3423` edge `0.1535` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8263` n `30` status `ready` deltaP `10.489` edge `0.0827` maxDD `-2.0691`
- `market_context_high->equity_24h` score `0.436` n `192` status `ready` deltaP `25.0` edge `0.4148` maxDD `-31.6107`
- `news_risk_high->crypto_alt_1h` score `0.2021` n `30` status `ready` deltaP `5.4691` edge `0.0356` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1257` n `30` status `ready` deltaP `9.2361` edge `0.0417` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4079` n `30` status `ready` deltaP `1.5369` edge `-0.0259` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4638` n `218` status `ready` deltaP `2.7908` edge `0.0018` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.572` n `218` status `ready` deltaP `2.0423` edge `0.0259` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.6241` n `218` status `ready` deltaP `-1.0671` edge `0.0015` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.6694` n `218` status `ready` deltaP `-0.5356` edge `-0.0014` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0368` n `30` status `ready` deltaP `-9.4012` edge `-0.0188` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1514` n `218` status `ready` deltaP `0.4629` edge `0.0154` maxDD `-2.9546`
- `market_context_high->commodity_4h` score `-1.1552` n `218` status `ready` deltaP `-1.8461` edge `-0.0062` maxDD `-3.0339`
- `market_context_high->crypto_major_1h` score `-1.1675` n `218` status `ready` deltaP `2.2016` edge `0.0124` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1863` n `218` status `ready` deltaP `1.5547` edge `0.0128` maxDD `-9.3536`
- `market_context_high->index_1h` score `-1.3156` n `218` status `ready` deltaP `-3.0709` edge `0.0019` maxDD `-1.2846`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
