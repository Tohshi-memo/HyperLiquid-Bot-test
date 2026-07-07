# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T21:52:30.853139+00:00`
- Price records: `672`
- Market context records: `6021`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11124`

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

- `news_risk_high->fx_24h` score `7.7476` n `30` status `ready` deltaP `69.9653` edge `0.1792` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2601` n `30` status `ready` deltaP `44.1159` edge `0.0655` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.2508` n `30` status `ready` deltaP `28.507` edge `0.1014` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.243` n `30` status `ready` deltaP `26.9261` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6204` n `207` status `ready` deltaP `8.963` edge `0.167` maxDD `-2.671`
- `market_context_high->equity_24h` score `1.4284` n `181` status `ready` deltaP `29.3048` edge `0.5329` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8395` n `30` status `ready` deltaP `10.3393` edge `0.0854` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2278` n `30` status `ready` deltaP `5.4691` edge `0.0389` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1421` n `30` status `ready` deltaP `9.2361` edge `0.0438` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3838` n `207` status `ready` deltaP `3.7592` edge `0.0056` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4032` n `30` status `ready` deltaP `1.5369` edge `-0.0253` maxDD `-1.2643`
- `market_context_high->index_24h` score `-0.5211` n `181` status `ready` deltaP `5.0741` edge `0.0756` maxDD `-6.099`
- `market_context_high->fx_1h` score `-0.6091` n `207` status `ready` deltaP `-0.5135` edge `-0.0015` maxDD `-0.6666`
- `market_context_high->commodity_1h` score `-0.6436` n `207` status `ready` deltaP `-1.2894` edge `-0.0004` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.9408` n `207` status `ready` deltaP `2.6077` edge `0.0184` maxDD `-2.1782`
- `market_context_high->metal_4h` score `-0.9425` n `207` status `ready` deltaP `4.9503` edge `0.0072` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.9781` n `207` status `ready` deltaP `0.8606` edge `0.0256` maxDD `-4.3608`
- `market_context_high->crypto_major_1h` score `-1.0026` n `207` status `ready` deltaP `3.5277` edge `0.0247` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.0042` n `207` status `ready` deltaP `3.3918` edge `0.0239` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.0197` n `30` status `ready` deltaP `-9.1018` edge `-0.0186` maxDD `-1.1161`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
