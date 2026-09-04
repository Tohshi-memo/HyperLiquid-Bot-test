# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T17:22:27.193833+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10802`

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

- `risk_on_high->unknown_4h` score `19.5166` n `133` status `ready` deltaP `7.3216` edge `1.6394` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5166` n `133` status `ready` deltaP `7.3216` edge `1.6394` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.3998` n `133` status `ready` deltaP `-1.9518` edge `1.0207` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.3998` n `133` status `ready` deltaP `-1.9518` edge `1.0207` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.189` n `212` status `ready` deltaP `9.1233` edge `0.8578` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.919` n `215` status `ready` deltaP `-0.8537` edge `0.812` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.0141` n `49` status `ready` deltaP `18.7855` edge `0.1529` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `1.7799` n `49` status `ready` deltaP `11.9721` edge `0.0857` maxDD `-0.042`
- `news_risk_high->commodity_4h` score `1.6833` n `49` status `ready` deltaP `13.0445` edge `0.0734` maxDD `-0.2737`
- `news_risk_high->crypto_major_4h` score `0.929` n `49` status `ready` deltaP `7.4726` edge `0.1317` maxDD `-2.6594`
- `news_risk_high->metal_4h` score `0.7104` n `49` status `ready` deltaP `11.8591` edge `0.0383` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `0.7058` n `49` status `ready` deltaP `11.4537` edge `0.0532` maxDD `-0.7924`
- `news_risk_high->index_1h` score `0.5243` n `49` status `ready` deltaP `10.8701` edge `0.0085` maxDD `-0.1`
- `news_risk_high->fx_4h` score `0.2019` n `49` status `ready` deltaP `10.4716` edge `0.0013` maxDD `-0.9514`
- `news_risk_high->metal_1h` score `0.1904` n `49` status `ready` deltaP `5.7956` edge `0.0087` maxDD `-0.5011`
- `risk_on_high->metal_1h` score `0.1085` n `133` status `ready` deltaP `12.5625` edge `0.0014` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1085` n `133` status `ready` deltaP `12.5625` edge `0.0014` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.1609` n `49` status `ready` deltaP `4.6377` edge `0.0003` maxDD `-0.9036`
- `news_risk_high->equity_24h` score `-0.1868` n `49` status `ready` deltaP `2.5014` edge `0.0727` maxDD `-5.0655`
- `risk_on_high->index_1h` score `-0.2058` n `133` status `ready` deltaP `3.2439` edge `-0.0035` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
