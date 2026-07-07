# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T18:22:27.367340+00:00`
- Price records: `672`
- Market context records: `6005`
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

- `news_risk_high->fx_24h` score `7.5899` n `30` status `ready` deltaP `68.9236` edge `0.173` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1725` n `30` status `ready` deltaP `43.2012` edge `0.0643` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8641` n `30` status `ready` deltaP `30.9375` edge `0.1363` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.219` n `30` status `ready` deltaP `26.6267` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.175` n `220` status `ready` deltaP `7.5693` edge `0.1569` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7577` n `30` status `ready` deltaP `9.8902` edge `0.0779` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1678` n `30` status `ready` deltaP `5.3194` edge `0.0322` maxDD `-1.6923`
- `market_context_high->equity_24h` score `0.152` n `194` status `ready` deltaP `24.2698` edge `0.396` maxDD `-31.6107`
- `news_risk_high->index_24h` score `0.1218` n `30` status `ready` deltaP `9.2361` edge `0.0412` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4126` n `30` status `ready` deltaP `1.5369` edge `-0.0265` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4998` n `220` status `ready` deltaP `2.2945` edge `0.0005` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5811` n `220` status `ready` deltaP `-0.6042` edge `0.002` maxDD `-0.7117`
- `market_context_high->equity_1h` score `-0.5879` n `220` status `ready` deltaP `2.006` edge `0.0241` maxDD `-4.3608`
- `market_context_high->fx_1h` score `-0.654` n `220` status `ready` deltaP `-0.343` edge `-0.0014` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0399` n `30` status `ready` deltaP `-9.4012` edge `-0.0192` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.1219` n `220` status `ready` deltaP `-1.3415` edge `-0.0053` maxDD `-3.0339`
- `market_context_high->index_4h` score `-1.1548` n `220` status `ready` deltaP `0.449` edge `0.0158` maxDD `-3.0139`
- `market_context_high->crypto_major_1h` score `-1.1945` n `220` status `ready` deltaP `2.0114` edge `0.0102` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2196` n `220` status `ready` deltaP `1.38` edge `0.0097` maxDD `-9.3536`
- `market_context_high->index_1h` score `-1.3575` n `220` status `ready` deltaP `-3.4921` edge `0.0015` maxDD `-1.3078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
