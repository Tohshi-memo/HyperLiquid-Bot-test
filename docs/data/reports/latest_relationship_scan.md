# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T19:22:43.109840+00:00`
- Price records: `672`
- Market context records: `5174`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `26.2651` n `72` status `ready` deltaP `32.4652` edge `1.9913` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `9.5607` n `72` status `ready` deltaP `22.0486` edge `1.0159` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.6418` n `72` status `ready` deltaP `23.4375` edge `0.9026` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `6.1202` n `148` status `ready` deltaP `20.6452` edge `0.4746` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0779` n `148` status `ready` deltaP `15.5817` edge `0.4792` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.7466` n `148` status `ready` deltaP `14.5353` edge `0.5279` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.7282` n `155` status `ready` deltaP `10.1854` edge `0.2236` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.4021` n `148` status `ready` deltaP `9.2864` edge `0.2188` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.61` n `155` status `ready` deltaP `7.0021` edge `0.1287` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.5541` n `155` status `ready` deltaP `4.3539` edge `0.1133` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.3723` n `155` status `ready` deltaP `8.6633` edge `0.0698` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0502` n `155` status `ready` deltaP `6.0827` edge `0.014` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0608` n `155` status `ready` deltaP `5.0096` edge `0.018` maxDD `-2.0682`
- `market_context_high->fx_24h` score `-0.1849` n `72` status `ready` deltaP `8.8542` edge `0.0151` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.2409` n `155` status `ready` deltaP `2.1084` edge `0.0003` maxDD `-0.6194`
- `market_context_high->commodity_24h` score `-0.3934` n `72` status `ready` deltaP `12.5` edge `0.0881` maxDD `-10.0829`
- `market_context_high->index_4h` score `-0.3942` n `148` status `ready` deltaP `6.2088` edge `0.0375` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5738` n `148` status `ready` deltaP `3.469` edge `0.0067` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6039` n `155` status `ready` deltaP `0.5756` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->metal_24h` score `-0.6089` n `72` status `ready` deltaP `-3.8195` edge `0.1724` maxDD `-9.9998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
