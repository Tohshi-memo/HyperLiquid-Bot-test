# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T02:07:29.857141+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7535`

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

- `market_context_high->unknown_24h` score `7598.2183` n `52` status `ready` deltaP `1.3889` edge `633.1756` maxDD `0.0`
- `market_context_high->unknown_4h` score `373.6662` n `52` status `ready` deltaP `7.3757` edge `31.094` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `37.9561` n `55` status `ready` deltaP `4.5101` edge `3.144` maxDD `-0.2178`
- `market_context_high->equity_24h` score `20.8936` n `52` status `ready` deltaP `42.695` edge `1.4801` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.6179` n `94` status `ready` deltaP `32.8716` edge `1.0513` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.2798` n `52` status `ready` deltaP `43.8302` edge `0.2622` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.1998` n `52` status `ready` deltaP `49.1319` edge `0.1891` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.0074` n `52` status `ready` deltaP `24.3668` edge `0.3676` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4246` n `52` status `ready` deltaP `30.9569` edge `0.2793` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.5389` n `52` status `ready` deltaP `33.3959` edge `0.089` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.8888` n `52` status `ready` deltaP `2.7204` edge `0.2928` maxDD `-2.283`
- `news_risk_high->crypto_alt_4h` score `2.3124` n `126` status `ready` deltaP `9.4706` edge `0.2682` maxDD `-7.4246`
- `market_context_high->equity_1h` score `2.205` n `55` status `ready` deltaP `7.7327` edge `0.1847` maxDD `-1.5336`
- `market_context_high->crypto_major_24h` score `2.1274` n `52` status `ready` deltaP `8.7607` edge `0.282` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.8198` n `52` status `ready` deltaP `-5.2217` edge `0.4199` maxDD `-8.8096`
- `market_context_high->crypto_major_1h` score `1.6183` n `55` status `ready` deltaP `7.583` edge `0.1352` maxDD `-1.4048`
- `market_context_high->metal_4h` score `1.5349` n `52` status `ready` deltaP `18.6444` edge `0.0461` maxDD `-0.7323`
- `market_context_high->crypto_alt_1h` score `1.4274` n `55` status `ready` deltaP `3.0267` edge `0.16` maxDD `-2.2314`
- `market_context_high->fx_1h` score `1.3308` n `55` status `ready` deltaP `18.3424` edge `0.0062` maxDD `-0.0736`
- `market_context_high->metal_1h` score `0.9702` n `55` status `ready` deltaP `11.9243` edge `0.0262` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
