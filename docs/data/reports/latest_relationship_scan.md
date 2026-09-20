# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T08:22:27.883638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9292`

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

- `news_risk_high->crypto_major_24h` score `39.9227` n `82` status `ready` deltaP `17.1282` edge `3.4103` maxDD `-12.4744`
- `news_risk_high->crypto_alt_24h` score `36.5039` n `82` status `ready` deltaP `27.5703` edge `2.9961` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `6.7688` n `69` status `ready` deltaP `34.8128` edge `0.3845` maxDD `-0.8682`
- `market_context_high->unknown_4h` score `6.3686` n `72` status `ready` deltaP `2.2357` edge `0.5308` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `6.211` n `98` status `ready` deltaP `23.4476` edge `0.4822` maxDD `-7.675`
- `news_risk_high->equity_24h` score `5.7146` n `82` status `ready` deltaP `32.1012` edge `0.283` maxDD `-0.6636`
- `news_risk_high->crypto_major_4h` score `4.7036` n `98` status `ready` deltaP `22.8378` edge `0.3655` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1673` n `72` status `ready` deltaP `36.5854` edge `0.1167` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0761` n `101` status `ready` deltaP `16.6805` edge `0.1917` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.3231` n `101` status `ready` deltaP `18.7763` edge `0.1207` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3209` n `72` status `ready` deltaP `30.4878` edge `0.0075` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `2.1337` n `72` status `ready` deltaP `23.2452` edge `0.0397` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.1697` n `69` status `ready` deltaP `15.9118` edge `-0.0044` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.8606` n `72` status `ready` deltaP `13.9055` edge `0.0048` maxDD `-0.063`
- `news_risk_high->metal_24h` score `0.8596` n `82` status `ready` deltaP `21.2737` edge `0.0528` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.8272` n `98` status `ready` deltaP `19.2819` edge `0.0458` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6916` n `101` status `ready` deltaP `15.3465` edge `0.0155` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.4153` n `82` status `ready` deltaP `17.5983` edge `0.0665` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3515` n `101` status `ready` deltaP `6.2622` edge `0.0281` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
