# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T03:37:30.079997+00:00`
- Price records: `672`
- Market context records: `5841`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9268` n `30` status `ready` deltaP `23.3333` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8277` n `30` status `ready` deltaP `11.2375` edge `0.0779` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7204` n `263` status `ready` deltaP `7.7721` edge `0.154` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1803` n `30` status `ready` deltaP `4.5709` edge `0.0388` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3307` n `263` status `ready` deltaP `0.9506` edge `-0.0002` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.3689` n `263` status `ready` deltaP `4.4922` edge `0.04` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4242` n `30` status `ready` deltaP `1.3872` edge `-0.027` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5262` n `263` status `ready` deltaP `-0.8487` edge `-0.0017` maxDD `-2.1419`
- `market_context_high->index_1h` score `-0.5434` n `263` status `ready` deltaP `1.3667` edge `0.006` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.5517` n `263` status `ready` deltaP `2.8068` edge `0.0024` maxDD `-2.0339`
- `market_context_high->equity_24h` score `-0.624` n `235` status `ready` deltaP `16.2441` edge `0.3476` maxDD `-31.6316`
- `market_context_high->crypto_major_1h` score `-0.9114` n `263` status `ready` deltaP `3.0373` edge `0.0359` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1117` n `263` status `ready` deltaP `1.5164` edge `0.0307` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1748` n `263` status `ready` deltaP `0.5564` edge `0.0144` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2261` n `30` status `ready` deltaP `-12.2455` edge `-0.0241` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.6876` n `263` status `ready` deltaP `-2.9323` edge `-0.0019` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.7053` n `235` status `ready` deltaP `6.5647` edge `0.0194` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1298` n `263` status `ready` deltaP `-4.616` edge `-0.0419` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.4631` n `263` status `ready` deltaP `-0.469` edge `-0.014` maxDD `-7.7173`
- `market_context_high->index_24h` score `-2.9151` n `235` status `ready` deltaP `2.916` edge `0.0213` maxDD `-18.1572`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
