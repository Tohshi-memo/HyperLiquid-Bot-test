# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T11:52:28.667550+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8522`

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

- `news_risk_high->crypto_major_24h` score `53.8701` n `72` status `ready` deltaP `33.1597` edge `4.3573` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `47.2266` n `72` status `ready` deltaP `37.6737` edge `3.8223` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9793` n `144` status `ready` deltaP `-2.185` edge `3.1195` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.8635` n `72` status `ready` deltaP `42.7083` edge `0.6248` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.2267` n `52` status `ready` deltaP `-9.076` edge `0.7686` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2267` n `52` status `ready` deltaP `-9.076` edge `0.7686` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2208` n `52` status `ready` deltaP `44.9653` edge `0.3853` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2208` n `52` status `ready` deltaP `44.9653` edge `0.3853` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0026` n `144` status `ready` deltaP `38.0209` edge `0.3826` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.5117` n `81` status `ready` deltaP `23.0974` edge `0.5096` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6779` n `81` status `ready` deltaP `20.4456` edge `0.3793` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.5284` n `92` status `ready` deltaP `19.9493` edge `0.2076` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6745` n `52` status `ready` deltaP `31.7777` edge `0.046` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6745` n `52` status `ready` deltaP `31.7777` edge `0.046` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5225` n `144` status `ready` deltaP `27.5576` edge `0.0683` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4467` n `92` status `ready` deltaP `19.8711` edge `0.1237` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.9173` n `72` status `ready` deltaP `24.4792` edge `0.081` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.1693` n `81` status `ready` deltaP `13.0834` edge `0.0321` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0645` n `144` status `ready` deltaP `15.6604` edge `0.022` maxDD `-0.3491`
- `news_risk_high->metal_1h` score `0.635` n `92` status `ready` deltaP `14.4298` edge `0.0169` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
