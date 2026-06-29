# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T19:18:09.060083+00:00`
- Price records: `672`
- Market context records: `5173`
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

- `market_context_high->unknown_24h` score `26.2807` n `72` status `ready` deltaP `32.4652` edge `1.9926` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `9.5187` n `72` status `ready` deltaP `22.0486` edge `1.0124` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.6214` n `72` status `ready` deltaP `23.4375` edge `0.9009` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `6.1226` n `148` status `ready` deltaP `20.6452` edge `0.4748` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0695` n `148` status `ready` deltaP `15.5817` edge `0.4785` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.7298` n `148` status `ready` deltaP `14.5353` edge `0.5265` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.7787` n `155` status `ready` deltaP `10.6809` edge `0.2245` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.3961` n `148` status `ready` deltaP `9.2864` edge `0.2183` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.5944` n `155` status `ready` deltaP `7.0021` edge `0.1274` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.5469` n `155` status `ready` deltaP `4.3539` edge `0.1127` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.3675` n `155` status `ready` deltaP `8.6633` edge `0.0694` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0081` n `155` status `ready` deltaP `5.5872` edge `0.0138` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0623` n `155` status `ready` deltaP `5.0096` edge `0.0178` maxDD `-2.0682`
- `market_context_high->fx_24h` score `-0.1849` n `72` status `ready` deltaP `8.8542` edge `0.0151` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.2409` n `155` status `ready` deltaP `2.1084` edge `0.0003` maxDD `-0.6194`
- `market_context_high->commodity_24h` score `-0.3903` n `72` status `ready` deltaP `12.5` edge `0.0883` maxDD `-10.0668`
- `market_context_high->index_4h` score `-0.3942` n `148` status `ready` deltaP `6.2088` edge `0.0375` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5738` n `148` status `ready` deltaP `3.469` edge `0.0067` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5774` n `155` status `ready` deltaP `1.0711` edge `-0.0003` maxDD `-2.4692`
- `market_context_high->metal_24h` score `-0.6188` n `72` status `ready` deltaP `-3.8195` edge `0.1718` maxDD `-10.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
