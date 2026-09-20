# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T01:52:31.356963+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9116`

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

- `news_risk_high->crypto_major_24h` score `46.6273` n `76` status `ready` deltaP `21.7654` edge `3.8297` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `41.3846` n `76` status `ready` deltaP `31.7892` edge `3.3747` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `20.7681` n `97` status `ready` deltaP `-5.4753` edge `1.7905` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.8097` n `95` status `ready` deltaP `38.7793` edge `0.4448` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.6703` n `76` status `ready` deltaP `36.1842` edge `0.4022` maxDD `-0.0053`
- `news_risk_high->crypto_alt_4h` score `5.9714` n `98` status `ready` deltaP `22.8378` edge `0.4663` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.679` n `98` status `ready` deltaP `23.2951` edge `0.3604` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8958` n `97` status `ready` deltaP `35.5308` edge `0.1011` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2952` n `98` status `ready` deltaP `18.7737` edge `0.196` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.5182` n `98` status `ready` deltaP `20.7198` edge `0.124` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.8405` n `98` status `ready` deltaP `21.3461` edge `0.0321` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.6328` n `76` status `ready` deltaP `22.8436` edge `0.0682` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.0917` n `97` status `ready` deltaP `20.3074` edge `0.0024` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8077` n `98` status `ready` deltaP `18.9771` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7183` n `98` status `ready` deltaP `15.6055` edge `0.016` maxDD `-0.8144`
- `market_context_high->fx_24h` score `0.67` n `95` status `ready` deltaP `11.7946` edge `-0.0186` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.4335` n `98` status `ready` deltaP `8.8965` edge `0.0026` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.4018` n `98` status `ready` deltaP `6.5166` edge `0.0306` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.0472` n `76` status `ready` deltaP `15.0951` edge `0.036` maxDD `-3.4467`
- `news_risk_high->fx_24h` score `0.0214` n `76` status `ready` deltaP `1.0051` edge `0.0326` maxDD `-0.3349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
