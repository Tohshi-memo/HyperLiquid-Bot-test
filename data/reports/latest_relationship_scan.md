# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T20:52:30.060240+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6818`

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

- `market_context_high->unknown_1h` score `337.7797` n `50` status `ready` deltaP `8.479` edge `28.0967` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.4584` n `50` status `ready` deltaP `6.8598` edge `23.8258` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.1672` n `99` status `ready` deltaP `35.827` edge `1.4627` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.3016` n `50` status `ready` deltaP `33.3889` edge `0.7775` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2257` n `50` status `ready` deltaP `18.7622` edge `0.5474` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.7147` n `50` status `ready` deltaP `11.8472` edge `0.5682` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0112` n `50` status `ready` deltaP `16.189` edge `0.439` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.6155` n `99` status `ready` deltaP `19.0657` edge `0.5729` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.8349` n `50` status `ready` deltaP `19.0417` edge `0.5509` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.2853` n `112` status `ready` deltaP `27.4608` edge `0.1603` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1306` n `50` status `ready` deltaP `34.9756` edge `0.0412` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0275` n `50` status `ready` deltaP `14.5988` edge `0.2` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.947` n `50` status `ready` deltaP `13.6048` edge `0.2212` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.7318` n `99` status `ready` deltaP `19.7286` edge `0.4536` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.1726` n `99` status `ready` deltaP `22.5695` edge `0.0784` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.0676` n `99` status `ready` deltaP `23.8163` edge `0.2337` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5142` n `50` status `ready` deltaP `21.0898` edge `0.012` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.2898` n `99` status `ready` deltaP `20.6755` edge `0.108` maxDD `-6.0683`
- `market_context_high->index_24h` score `0.9073` n `50` status `ready` deltaP `14.7917` edge `0.0748` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.4915` n `50` status `ready` deltaP `14.4306` edge `0.0686` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
