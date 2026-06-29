# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T21:37:32.177414+00:00`
- Price records: `672`
- Market context records: `5184`
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

- `market_context_high->unknown_24h` score `22.2806` n `81` status `ready` deltaP `32.9089` edge `1.6563` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.1822` n `81` status `ready` deltaP `25.733` edge `1.2098` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.8487` n `81` status `ready` deltaP `26.659` edge `0.9817` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.7372` n `152` status `ready` deltaP `19.7128` edge `0.4489` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.5975` n `152` status `ready` deltaP `13.6714` edge `0.4519` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4387` n `152` status `ready` deltaP `13.6714` edge `0.508` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.5904` n `155` status `ready` deltaP `9.4369` edge `0.2171` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.2849` n `152` status `ready` deltaP `8.9458` edge `0.2113` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5421` n `155` status `ready` deltaP `4.3539` edge `0.1123` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5225` n `155` status `ready` deltaP `6.4033` edge `0.1254` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.3052` n `155` status `ready` deltaP `8.0645` edge `0.0682` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.11` n `81` status `ready` deltaP `10.9954` edge `0.0254` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0226` n `155` status `ready` deltaP `5.7833` edge `0.0137` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0444` n `155` status `ready` deltaP `5.309` edge `0.0181` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2736` n `155` status `ready` deltaP `1.5096` edge `0.0001` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4175` n `152` status `ready` deltaP `6.0815` edge `0.0364` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5285` n `152` status `ready` deltaP `4.3405` edge `0.0067` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5969` n `155` status `ready` deltaP `0.7253` edge `-0.0005` maxDD `-2.4692`
- `market_context_high->index_24h` score `-1.0669` n `81` status `ready` deltaP `6.2114` edge `-0.0147` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2201` n `152` status `ready` deltaP `0.8425` edge `0.0383` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
