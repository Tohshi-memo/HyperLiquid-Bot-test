# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T09:37:34.839975+00:00`
- Price records: `672`
- Market context records: `5235`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5602`

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

- `market_context_high->unknown_24h` score `23.0072` n `126` status `ready` deltaP `32.2421` edge `1.7213` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.2422` n `126` status `ready` deltaP `33.4326` edge `1.2468` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `7.0608` n `126` status `ready` deltaP `22.5694` edge `0.7808` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.0929` n `155` status `ready` deltaP `13.694` edge `0.4097` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9756` n `155` status `ready` deltaP `14.527` edge `0.4637` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.1888` n `155` status `ready` deltaP `16.9827` edge `0.1714` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8082` n `155` status `ready` deltaP `8.0896` edge `0.1609` maxDD `-2.7986`
- `market_context_high->equity_24h` score `1.071` n `126` status `ready` deltaP `17.5843` edge `0.5349` maxDD `-40.0306`
- `market_context_high->fx_24h` score `0.5707` n `126` status `ready` deltaP `13.2441` edge `0.0488` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4808` n `155` status `ready` deltaP `4.803` edge `0.1042` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4432` n `155` status `ready` deltaP `6.8524` edge `0.1158` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.0879` n `155` status `ready` deltaP `6.1782` edge `0.13` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.142` n `155` status `ready` deltaP `5.6693` edge `0.0469` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1574` n `155` status `ready` deltaP `4.1114` edge `0.0116` maxDD `-2.0682`
- `market_context_high->index_24h` score `-0.1641` n `126` status `ready` deltaP `17.0635` edge `0.0287` maxDD `-7.413`
- `market_context_high->index_1h` score `-0.205` n `155` status `ready` deltaP `3.6875` edge `0.0087` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3188` n `155` status `ready` deltaP `0.7611` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.6655` n `155` status `ready` deltaP `-0.3226` edge `-0.0023` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7386` n `155` status `ready` deltaP `0.8999` edge `0.0027` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8983` n `155` status `ready` deltaP `3.1619` edge `0.0158` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
