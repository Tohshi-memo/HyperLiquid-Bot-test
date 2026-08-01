# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T10:37:25.612813+00:00`
- Price records: `672`
- Market context records: `8612`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5076.9069` n `61` status `ready` deltaP `34.3438` edge `422.8887` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.6087` n `39` status `ready` deltaP `51.7887` edge `1.2452` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.9712` n `61` status `ready` deltaP `19.515` edge `0.4272` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4587` n `61` status `ready` deltaP `21.3065` edge `0.0819` maxDD `-0.191`
- `market_context_high->fx_24h` score `1.8565` n `39` status `ready` deltaP `29.0584` edge `0.08` maxDD `-0.523`
- `market_context_high->crypto_major_24h` score `1.7546` n `39` status `ready` deltaP `7.5368` edge `0.5277` maxDD `-22.5735`
- `market_context_high->crypto_alt_4h` score `1.7291` n `62` status `ready` deltaP `12.6749` edge `0.1553` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7083` n `61` status `ready` deltaP `15.3946` edge `0.0874` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0309` n `61` status `ready` deltaP `6.5748` edge `0.1659` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4955` n `61` status `ready` deltaP `9.1661` edge `0.0551` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.371` n `61` status `ready` deltaP `7.0776` edge `0.0516` maxDD `-2.0972`
- `news_risk_high->crypto_alt_4h` score `0.3466` n `61` status `ready` deltaP `10.4274` edge `0.1141` maxDD `-5.8012`
- `news_risk_high->fx_4h` score `0.2292` n `61` status `ready` deltaP `13.7635` edge `0.0231` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `0.1094` n `61` status `ready` deltaP `6.1721` edge `0.0083` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `0.0889` n `61` status `ready` deltaP `3.7653` edge `0.0339` maxDD `-0.8085`
- `news_risk_high->fx_1h` score `0.0758` n `61` status `ready` deltaP `4.9966` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0207` n `61` status `ready` deltaP `3.7842` edge `0.0091` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.1563` n `62` status `ready` deltaP `8.0522` edge `0.0129` maxDD `-1.3685`
- `market_context_high->metal_24h` score `-0.2383` n `39` status `ready` deltaP `0.6044` edge `0.0626` maxDD `-2.1075`
- `market_context_high->fx_1h` score `-0.2599` n `62` status `ready` deltaP `2.5111` edge `0.0002` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
