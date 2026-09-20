# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T02:22:27.913156+00:00`
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

- `news_risk_high->crypto_major_24h` score `44.467` n `78` status `ready` deltaP `19.4712` edge `3.6733` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `40.0959` n `78` status `ready` deltaP `31.6105` edge `3.2685` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `23.0544` n `95` status `ready` deltaP `-3.9569` edge `1.9709` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.728` n `93` status `ready` deltaP `38.5529` edge `0.4395` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.3573` n `78` status `ready` deltaP `35.8707` edge `0.3782` maxDD `-0.0053`
- `news_risk_high->crypto_alt_4h` score `5.9354` n `98` status `ready` deltaP `22.8378` edge `0.4633` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.645` n `98` status `ready` deltaP `22.9902` edge `0.3596` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.9584` n `95` status `ready` deltaP `36.1489` edge `0.1022` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2796` n `98` status `ready` deltaP `18.624` edge `0.1957` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.5373` n `98` status `ready` deltaP `20.8695` edge `0.1246` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.9539` n `96` status `ready` deltaP `22.5986` edge `0.0332` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.6105` n `78` status `ready` deltaP `23.1037` edge `0.0646` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1413` n `95` status `ready` deltaP `20.8825` edge `0.0027` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8199` n `98` status `ready` deltaP `19.1295` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7303` n `98` status `ready` deltaP `15.7552` edge `0.016` maxDD `-0.8144`
- `market_context_high->fx_24h` score `0.7031` n `93` status `ready` deltaP `12.1191` edge `-0.018` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.4585` n `96` status `ready` deltaP `9.1941` edge `0.0027` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3743` n `98` status `ready` deltaP `6.2172` edge `0.0303` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.1287` n `78` status `ready` deltaP `15.9723` edge `0.0406` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
