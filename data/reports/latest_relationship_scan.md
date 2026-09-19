# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T09:52:25.666843+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8512`

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

- `news_risk_high->crypto_major_24h` score `54.8668` n `72` status `ready` deltaP `34.5486` edge `4.4311` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `48.0493` n `72` status `ready` deltaP `39.0625` edge `3.8816` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9541` n `144` status `ready` deltaP `-2.185` edge `3.1174` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.2974` n `72` status `ready` deltaP `44.0972` edge `0.6517` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.2328` n `52` status `ready` deltaP `44.9653` edge `0.3863` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2328` n `52` status `ready` deltaP `44.9653` edge `0.3863` maxDD `0.0`
- `risk_on_high->unknown_4h` score `8.2015` n `52` status `ready` deltaP `-9.076` edge `0.7665` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2015` n `52` status `ready` deltaP `-9.076` edge `0.7665` maxDD `-0.4694`
- `market_context_high->commodity_24h` score `7.0146` n `144` status `ready` deltaP `38.0209` edge `0.3836` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.7037` n `81` status `ready` deltaP `23.0974` edge `0.5256` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6741` n `81` status `ready` deltaP `20.2932` edge `0.38` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3114` n `84` status `ready` deltaP `17.9712` edge `0.2027` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6855` n `52` status `ready` deltaP `31.9301` edge `0.0459` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6855` n `52` status `ready` deltaP `31.9301` edge `0.0459` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5334` n `144` status `ready` deltaP `27.71` edge `0.0682` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4828` n `84` status `ready` deltaP `19.7676` edge `0.1274` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.8921` n `72` status `ready` deltaP `24.4792` edge `0.0789` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.2326` n `81` status `ready` deltaP `13.8456` edge `0.0323` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0645` n `144` status `ready` deltaP `15.6604` edge `0.022` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.6971` n `84` status `ready` deltaP `8.9321` edge `0.0391` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
