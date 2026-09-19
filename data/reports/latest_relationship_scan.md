# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T10:07:27.753871+00:00`
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

- `news_risk_high->crypto_major_24h` score `54.7497` n `72` status `ready` deltaP `34.375` edge `4.4225` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `47.9622` n `72` status `ready` deltaP `38.8889` edge `3.8755` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9529` n `144` status `ready` deltaP `-2.185` edge `3.1173` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.2451` n `72` status `ready` deltaP `43.9236` edge `0.6485` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.2328` n `52` status `ready` deltaP `44.9653` edge `0.3863` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2328` n `52` status `ready` deltaP `44.9653` edge `0.3863` maxDD `0.0`
- `risk_on_high->unknown_4h` score `8.2003` n `52` status `ready` deltaP `-9.076` edge `0.7664` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2003` n `52` status `ready` deltaP `-9.076` edge `0.7664` maxDD `-0.4694`
- `market_context_high->commodity_24h` score `7.0146` n `144` status `ready` deltaP `38.0209` edge `0.3836` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6857` n `81` status `ready` deltaP `23.0974` edge `0.5241` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6935` n `81` status `ready` deltaP `20.4456` edge `0.3806` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3108` n `85` status `ready` deltaP `18.2793` edge `0.2006` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6867` n `52` status `ready` deltaP `31.9301` edge `0.046` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6867` n `52` status `ready` deltaP `31.9301` edge `0.046` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5346` n `144` status `ready` deltaP `27.71` edge `0.0683` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3749` n `85` status `ready` deltaP `19.049` edge `0.1232` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.8957` n `72` status `ready` deltaP `24.4792` edge `0.0792` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.2205` n `81` status `ready` deltaP `13.6932` edge `0.0323` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0776` n `144` status `ready` deltaP `15.8101` edge `0.0221` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.647` n `85` status `ready` deltaP `8.3956` edge `0.0385` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
