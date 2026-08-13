# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T11:37:30.574215+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `32.7351` n `161` status `ready` deltaP `-23.6898` edge `3.1771` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `7.5241` n `32` status `ready` deltaP `-42.1875` edge `1.3209` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `7.5241` n `32` status `ready` deltaP `-42.1875` edge `1.3209` maxDD `-1.6689`
- `news_risk_high->equity_4h` score `7.0186` n `36` status `ready` deltaP `37.3476` edge `0.3359` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.4102` n `32` status `ready` deltaP `25.3472` edge `0.1152` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.4102` n `32` status `ready` deltaP `25.3472` edge `0.1152` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.4927` n `32` status `ready` deltaP `17.4543` edge `0.1096` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.4927` n `32` status `ready` deltaP `17.4543` edge `0.1096` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.0826` n `32` status `ready` deltaP `23.2639` edge `0.0369` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0826` n `32` status `ready` deltaP `23.2639` edge `0.0369` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.9116` n `36` status `ready` deltaP `21.7479` edge `0.0275` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.5895` n `36` status `ready` deltaP `7.8344` edge `0.1121` maxDD `-0.5496`
- `market_context_high->commodity_24h` score `1.4412` n `161` status `ready` deltaP `15.4093` edge `0.0977` maxDD `-2.4263`
- `risk_on_high->crypto_major_24h` score `1.3903` n `32` status `ready` deltaP `12.8472` edge `0.2082` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3903` n `32` status `ready` deltaP `12.8472` edge `0.2082` maxDD `-6.2481`
- `market_context_high->commodity_4h` score `1.3111` n `161` status `ready` deltaP `15.1057` edge `0.0724` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.1521` n `32` status `ready` deltaP `12.4626` edge `0.0362` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1521` n `32` status `ready` deltaP `12.4626` edge `0.0362` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9293` n `32` status `ready` deltaP `10.747` edge `0.0199` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9293` n `32` status `ready` deltaP `10.747` edge `0.0199` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
