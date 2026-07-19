# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T19:22:29.054667+00:00`
- Price records: `672`
- Market context records: `7282`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13791`

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

- `market_context_high->fx_1h` score `-0.2058` n `133` status `ready` deltaP `3.2333` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.7874` n `133` status `ready` deltaP `-1.434` edge `0.0125` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-0.8766` n `130` status `ready` deltaP `5.1893` edge `0.013` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-0.9244` n `133` status `ready` deltaP `1.73` edge `0.011` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-1.098` n `133` status `ready` deltaP `-2.1767` edge `-0.0149` maxDD `-1.9668`
- `market_context_high->fx_24h` score `-1.1057` n `125` status `ready` deltaP `-2.4696` edge `-0.0025` maxDD `-2.1564`
- `market_context_high->unknown_4h` score `-1.1425` n `130` status `ready` deltaP `7.8987` edge `0.088` maxDD `-6.2026`
- `market_context_high->unknown_1h` score `-1.2186` n `133` status `ready` deltaP `0.063` edge `-0.0943` maxDD `-1.3212`
- `market_context_high->commodity_4h` score `-1.3719` n `130` status `ready` deltaP `0.1999` edge `-0.017` maxDD `-2.5593`
- `market_context_high->index_1h` score `-1.403` n `133` status `ready` deltaP `-5.9495` edge `-0.01` maxDD `-2.3805`
- `market_context_high->metal_1h` score `-2.2045` n `133` status `ready` deltaP `-9.116` edge `-0.0071` maxDD `-1.9332`
- `market_context_high->commodity_24h` score `-2.6326` n `125` status `ready` deltaP `-3.6174` edge `-0.1155` maxDD `-2.3815`
- `market_context_high->metal_4h` score `-2.6764` n `130` status `ready` deltaP `-12.0873` edge `-0.017` maxDD `-4.6441`
- `market_context_high->equity_1h` score `-4.6331` n `133` status `ready` deltaP `-9.5588` edge `-0.0697` maxDD `-15.5469`
- `market_context_high->crypto_alt_4h` score `-4.7297` n `130` status `ready` deltaP `-1.7613` edge `-0.0427` maxDD `-20.5092`
- `market_context_high->crypto_major_4h` score `-5.4019` n `130` status `ready` deltaP `-1.8645` edge `-0.0483` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.4821` n `130` status `ready` deltaP `-16.0574` edge `-0.0658` maxDD `-12.3859`
- `market_context_high->unknown_24h` score `-6.2018` n `126` status `ready` deltaP `-12.6984` edge `-0.0607` maxDD `-17.7166`
- `market_context_high->metal_24h` score `-12.3094` n `126` status `ready` deltaP `-31.6716` edge `-0.1489` maxDD `-26.5926`
- `market_context_high->index_24h` score `-14.7269` n `125` status `ready` deltaP `-29.6` edge `-0.1871` maxDD `-40.0916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
