# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T20:52:33.925997+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5038`

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

- `market_context_high->unknown_4h` score `29.7201` n `113` status `ready` deltaP `-0.7487` edge `2.5152` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.2662` n `74` status `ready` deltaP `2.7637` edge `0.1063` maxDD `-4.5369`
- `market_context_high->fx_4h` score `-0.0573` n `113` status `ready` deltaP `7.0014` edge `0.0084` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0747` n `113` status `ready` deltaP `3.41` edge `0.0026` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.493` n `113` status `ready` deltaP `-0.0331` edge `0.0092` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.5532` n `74` status `ready` deltaP `10.7404` edge `0.0147` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.6419` n `113` status `ready` deltaP `4.6341` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.7017` n `113` status `ready` deltaP `-2.7847` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.7929` n `113` status `ready` deltaP `-1.6283` edge `0.0321` maxDD `-1.165`
- `market_context_high->commodity_24h` score `-1.2051` n `74` status `ready` deltaP `-1.7361` edge `0.002` maxDD `-3.9277`
- `market_context_high->metal_24h` score `-1.3291` n `74` status `ready` deltaP `3.7256` edge `0.0718` maxDD `-7.3625`
- `market_context_high->crypto_major_1h` score `-1.3457` n `113` status `ready` deltaP `3.0973` edge `-0.0351` maxDD `-9.3126`
- `market_context_high->index_24h` score `-1.3711` n `74` status `ready` deltaP `5.3914` edge `-0.0835` maxDD `-4.925`
- `market_context_high->metal_4h` score `-2.0206` n `113` status `ready` deltaP `3.3941` edge `-0.02` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.206` n `113` status `ready` deltaP `-8.6822` edge `-0.0375` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.2195` n `113` status `ready` deltaP `-1.7103` edge `-0.0695` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9698` n `113` status `ready` deltaP `-1.4374` edge `-0.0939` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.5297` n `74` status `ready` deltaP `0.1361` edge `-0.1924` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-9.1848` n `74` status `ready` deltaP `-7.5263` edge `-0.599` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.3161` n `113` status `ready` deltaP `-14.7245` edge `-0.2617` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
