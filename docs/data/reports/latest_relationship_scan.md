# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T23:37:27.110198+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.6625` n `113` status `ready` deltaP `-0.7487` edge `2.5104` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.606` n `85` status `ready` deltaP `7.3571` edge `0.104` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0824` n `113` status `ready` deltaP `3.2603` edge `0.0026` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1108` n `113` status `ready` deltaP `6.3917` edge `0.008` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.2274` n `85` status `ready` deltaP `16.0008` edge `0.0214` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4499` n `113` status `ready` deltaP `0.2663` edge `0.0108` maxDD `-1.0053`
- `market_context_high->metal_24h` score `-0.5507` n `85` status `ready` deltaP `12.9943` edge `0.1098` maxDD `-7.3625`
- `market_context_high->index_1h` score `-0.662` n `113` status `ready` deltaP `-2.0362` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6838` n `113` status `ready` deltaP `4.185` edge `-0.0057` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.7252` n `113` status `ready` deltaP `-0.8661` edge `0.0357` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.8966` n `85` status `ready` deltaP `10.288` edge `-0.0553` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3106` n `113` status `ready` deltaP `3.5464` edge `-0.0336` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.029` n `113` status `ready` deltaP `3.3941` edge `-0.0207` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1704` n `113` status `ready` deltaP `-8.0725` edge `-0.037` maxDD `-4.3282`
- `market_context_high->commodity_24h` score `-2.6653` n `85` status `ready` deltaP `-8.2067` edge `-0.0457` maxDD `-7.97`
- `market_context_high->crypto_alt_1h` score `-3.1859` n `113` status `ready` deltaP `-1.5606` edge `-0.0677` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8787` n `113` status `ready` deltaP `-0.5392` edge `-0.0923` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.1464` n `85` status `ready` deltaP `-4.5997` edge `-0.2399` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-7.6253` n `85` status `ready` deltaP `-0.531` edge `-0.4457` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.0212` n `113` status `ready` deltaP `-13.0477` edge `-0.2483` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
