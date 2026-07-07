# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T16:37:28.273132+00:00`
- Price records: `672`
- Market context records: `5998`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11122`

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

- `news_risk_high->fx_24h` score `7.5551` n `30` status `ready` deltaP `68.9236` edge `0.1701` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1677` n `30` status `ready` deltaP `43.2012` edge `0.0639` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1365` n `30` status `ready` deltaP `32.1528` edge `0.1509` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.231` n `30` status `ready` deltaP `26.7764` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.143` n `223` status `ready` deltaP `7.3635` edge `0.1556` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7429` n `30` status `ready` deltaP `9.7405` edge `0.077` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1397` n `30` status `ready` deltaP `5.02` edge `0.0306` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1179` n `30` status `ready` deltaP `9.2361` edge `0.0407` maxDD `-2.3058`
- `market_context_high->equity_24h` score `-0.0359` n `196` status `ready` deltaP `23.5545` edge `0.3744` maxDD `-31.0873`
- `news_risk_high->metal_1h` score `-0.4133` n `30` status `ready` deltaP `1.5369` edge `-0.0266` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4894` n `223` status `ready` deltaP `2.4637` edge `0.0007` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.5229` n `223` status `ready` deltaP `2.7611` edge `0.0274` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.5531` n `223` status `ready` deltaP `-0.3739` edge `0.0028` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.6919` n `223` status `ready` deltaP `-0.817` edge `-0.0014` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0119` n `30` status `ready` deltaP `-8.9521` edge `-0.0186` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0213` n `223` status `ready` deltaP `0.0082` edge `-0.0014` maxDD `-3.0339`
- `market_context_high->index_4h` score `-1.1757` n `223` status `ready` deltaP `0.2153` edge `0.016` maxDD `-3.1199`
- `market_context_high->crypto_major_1h` score `-1.1952` n `223` status `ready` deltaP `2.0126` edge `0.0101` maxDD `-9.807`
- `market_context_high->index_1h` score `-1.255` n `223` status `ready` deltaP `-2.3153` edge `0.0022` maxDD `-1.3078`
- `market_context_high->crypto_alt_1h` score `-1.2721` n `223` status `ready` deltaP `0.8197` edge `0.0067` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
