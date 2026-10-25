# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T21:07:24.346414+00:00`
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

- `market_context_high->unknown_4h` score `29.6865` n `113` status `ready` deltaP `-0.7487` edge `2.5124` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.3495` n `75` status `ready` deltaP `3.3402` edge `0.1094` maxDD `-4.5369`
- `market_context_high->fx_4h` score `-0.0573` n `113` status `ready` deltaP `7.0014` edge `0.0084` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0824` n `113` status `ready` deltaP `3.2603` edge `0.0026` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.4918` n `113` status `ready` deltaP `-0.0331` edge `0.0093` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.5176` n `75` status `ready` deltaP `11.3055` edge `0.0155` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.6539` n `113` status `ready` deltaP `4.4844` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6931` n `113` status `ready` deltaP `-2.635` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.7921` n `113` status `ready` deltaP `-1.6283` edge `0.0322` maxDD `-1.165`
- `market_context_high->metal_24h` score `-1.2529` n `75` status `ready` deltaP `4.6805` edge `0.0752` maxDD `-7.3625`
- `market_context_high->commodity_24h` score `-1.3117` n `75` status `ready` deltaP `-2.4028` edge `-0.0007` maxDD `-4.1154`
- `market_context_high->index_24h` score `-1.3238` n `75` status `ready` deltaP `5.8959` edge `-0.0808` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3348` n `113` status `ready` deltaP `3.247` edge `-0.0347` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0206` n `113` status `ready` deltaP `3.3941` edge `-0.02` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1965` n `113` status `ready` deltaP `-8.5298` edge `-0.0373` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1931` n `113` status `ready` deltaP `-1.5606` edge `-0.0683` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9554` n `113` status `ready` deltaP `-1.2877` edge `-0.0937` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.5687` n `75` status `ready` deltaP `-0.375` edge `-0.194` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-9.0178` n `75` status `ready` deltaP `-6.8055` edge `-0.5824` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.2847` n `113` status `ready` deltaP `-14.5721` edge `-0.2601` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
