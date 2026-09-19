# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T13:07:28.236786+00:00`
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

- `news_risk_high->crypto_major_24h` score `53.1802` n `72` status `ready` deltaP `32.2916` edge `4.3056` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.6483` n `72` status `ready` deltaP `36.8056` edge `3.7799` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.0717` n `144` status `ready` deltaP `-2.185` edge `3.1272` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.5324` n `72` status `ready` deltaP `41.8403` edge `0.603` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.3191` n `52` status `ready` deltaP `-9.076` edge `0.7763` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.3191` n `52` status `ready` deltaP `-9.076` edge `0.7763` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2563` n `52` status `ready` deltaP `45.1389` edge `0.3871` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2563` n `52` status `ready` deltaP `45.1389` edge `0.3871` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0381` n `144` status `ready` deltaP `38.1945` edge `0.3844` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6259` n `85` status `ready` deltaP `23.9688` edge `0.5133` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5484` n `85` status `ready` deltaP `21.0922` edge `0.3642` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.4174` n `97` status `ready` deltaP `20.0013` edge `0.198` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6489` n `52` status `ready` deltaP `31.4728` edge `0.0459` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6489` n `52` status `ready` deltaP `31.4728` edge `0.0459` maxDD `-0.1313`
- `news_risk_high->crypto_major_1h` score `2.5027` n `97` status `ready` deltaP `21.0661` edge `0.1204` maxDD `-2.8494`
- `market_context_high->commodity_4h` score `2.4969` n `144` status `ready` deltaP `27.2527` edge `0.0682` maxDD `-0.345`
- `news_risk_high->metal_24h` score `1.9173` n `72` status `ready` deltaP `24.4792` edge `0.081` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.0776` n `144` status `ready` deltaP `15.8101` edge `0.0221` maxDD `-0.3491`
- `news_risk_high->fx_4h` score `1.0748` n `85` status `ready` deltaP `12.3135` edge `0.0296` maxDD `-0.1034`
- `news_risk_high->metal_1h` score `0.7518` n `97` status `ready` deltaP `15.9794` edge `0.0163` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
