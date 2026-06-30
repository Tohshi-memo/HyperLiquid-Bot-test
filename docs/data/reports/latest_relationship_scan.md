# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T02:37:31.290452+00:00`
- Price records: `672`
- Market context records: `5207`
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

- `market_context_high->unknown_24h` score `16.1668` n `101` status `ready` deltaP `33.8868` edge `1.1403` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.865` n `101` status `ready` deltaP `30.5727` edge `1.4011` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.6056` n `101` status `ready` deltaP `30.7652` edge `1.0174` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.2513` n `155` status `ready` deltaP `18.9644` edge `0.4134` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.6067` n `155` status `ready` deltaP `13.8464` edge `0.4515` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4526` n `155` status `ready` deltaP `14.0696` edge `0.5065` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.5617` n `155` status `ready` deltaP `8.8381` edge `0.2187` maxDD `-2.7986`
- `market_context_high->crypto_alt_1h` score `0.6524` n `155` status `ready` deltaP `4.9527` edge `0.1175` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.646` n `155` status `ready` deltaP `7.0021` edge `0.1317` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.5906` n `155` status `ready` deltaP `8.0074` edge `0.1597` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.55` n `101` status `ready` deltaP `13.3904` edge `0.0461` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.0067` n `155` status `ready` deltaP `6.1184` edge `0.0563` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.0935` n `155` status `ready` deltaP `4.5605` edge `0.0168` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1235` n `155` status `ready` deltaP `4.2863` edge `0.0115` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.276` n `155` status `ready` deltaP `1.5096` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.5923` n `155` status `ready` deltaP `3.3389` edge `0.0052` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.5966` n `155` status `ready` deltaP `5.4485` edge `0.0257` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.6156` n `155` status `ready` deltaP `0.4259` edge `-0.0009` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.6724` n `101` status `ready` deltaP `12.029` edge `-0.0029` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3613` n `155` status `ready` deltaP `-0.1023` edge `0.0265` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
