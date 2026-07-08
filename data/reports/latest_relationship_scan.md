# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T00:07:27.271841+00:00`
- Price records: `672`
- Market context records: `6032`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `7.9278` n `30` status `ready` deltaP `71.5278` edge `0.1838` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3063` n `30` status `ready` deltaP `44.5732` edge `0.0663` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.8342` n `30` status `ready` deltaP `26.9445` edge `0.0771` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2562` n `30` status `ready` deltaP `27.0758` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_24h` score `1.7185` n `180` status `ready` deltaP `29.7223` edge `0.5673` maxDD `-31.6107`
- `market_context_high->equity_4h` score `1.6675` n `206` status `ready` deltaP `9.2514` edge `0.169` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.8263` n `30` status `ready` deltaP `10.1896` edge `0.0847` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2496` n `30` status `ready` deltaP `5.7685` edge `0.0397` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1499` n `30` status `ready` deltaP `9.2361` edge `0.0448` maxDD `-2.3058`
- `news_risk_high->crypto_alt_24h` score `-0.2184` n `30` status `ready` deltaP `23.5416` edge `-0.1604` maxDD `-0.5131`
- `market_context_high->metal_1h` score `-0.3955` n `206` status `ready` deltaP `3.5797` edge `0.0053` maxDD `-2.0564`
- `market_context_high->index_24h` score `-0.4296` n `180` status `ready` deltaP `5.3472` edge `0.0793` maxDD `-5.6021`
- `news_risk_high->metal_1h` score `-0.432` n `30` status `ready` deltaP `1.0878` edge `-0.026` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5762` n `206` status `ready` deltaP `-0.141` edge `-0.0014` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6643` n `206` status `ready` deltaP `-1.5333` edge `-0.0005` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.9244` n `206` status `ready` deltaP `2.5678` edge `0.0177` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-0.9297` n `206` status `ready` deltaP `5.0956` edge `0.0073` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.9557` n `206` status `ready` deltaP `1.0799` edge `0.026` maxDD `-4.3608`
- `market_context_high->crypto_alt_1h` score `-0.9569` n `206` status `ready` deltaP `3.9562` edge `0.0262` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9914` n `206` status `ready` deltaP `3.6524` edge `0.0253` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
