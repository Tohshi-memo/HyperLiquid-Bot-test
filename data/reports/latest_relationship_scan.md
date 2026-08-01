# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T17:22:27.388465+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.4314` n `60` status `ready` deltaP `34.2345` edge `432.3498` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.9073` n `53` status `ready` deltaP `54.6712` edge `1.0842` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.5028` n `60` status `ready` deltaP `23.7601` edge `0.4432` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.652` n `60` status `ready` deltaP `23.3028` edge `0.0847` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.0924` n `53` status `ready` deltaP `30.2573` edge `0.2524` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.3314` n `60` status `ready` deltaP `8.0488` edge `0.1946` maxDD `-3.5385`
- `news_risk_high->equity_1h` score `0.8306` n `66` status `ready` deltaP `9.6126` edge `0.0777` maxDD `-2.8051`
- `news_risk_high->crypto_alt_4h` score `0.564` n `60` status `ready` deltaP `12.1341` edge `0.1306` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5495` n `53` status `ready` deltaP `8.7379` edge `0.1079` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.4328` n `66` status `ready` deltaP `8.474` edge `0.0542` maxDD `-2.0834`
- `news_risk_high->fx_4h` score `0.2523` n `60` status `ready` deltaP `13.8415` edge `0.0245` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.205` n `53` status `ready` deltaP `13.5585` edge `0.0155` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1535` n `60` status `ready` deltaP `4.8272` edge `0.0351` maxDD `-0.8085`
- `news_risk_high->crypto_major_1h` score `0.1199` n `66` status `ready` deltaP `3.6291` edge `0.0477` maxDD `-2.5218`
- `market_context_high->fx_1h` score `-0.0161` n `53` status `ready` deltaP `7.2026` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0264` n `66` status `ready` deltaP `3.0666` edge `0.0083` maxDD `-0.5702`
- `news_risk_high->fx_1h` score `-0.0286` n `66` status `ready` deltaP `3.6291` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0663` n `66` status `ready` deltaP `3.6654` edge `0.0074` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.0955` n `53` status `ready` deltaP `3.8781` edge `0.016` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `-0.2122` n `53` status `ready` deltaP `4.3344` edge `0.0314` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
