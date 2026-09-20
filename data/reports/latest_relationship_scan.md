# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T11:52:29.770708+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `news_risk_high->crypto_major_24h` score `23.4886` n `96` status `ready` deltaP `7.4652` edge `2.5316` maxDD `-41.9187`
- `news_risk_high->crypto_alt_24h` score `21.9361` n `96` status `ready` deltaP `15.9722` edge `2.1461` maxDD `-28.2994`
- `market_context_high->unknown_4h` score `20.1031` n `60` status `ready` deltaP `1.4024` edge `1.6809` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.8376` n `101` status `ready` deltaP `22.4251` edge `0.4579` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.7669` n `55` status `ready` deltaP `31.1238` edge `0.3256` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.3501` n `101` status `ready` deltaP `21.358` edge `0.3459` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8656` n `60` status `ready` deltaP `32.7235` edge `0.1173` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0498` n `101` status `ready` deltaP `16.5308` edge `0.1905` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2914` n `60` status `ready` deltaP `29.6545` edge `0.0106` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2248` n `101` status `ready` deltaP `18.3272` edge `0.1155` maxDD `-2.8494`
- `market_context_high->fx_24h` score `1.5027` n `55` status `ready` deltaP `17.9735` edge `0.0096` maxDD `-0.0027`
- `news_risk_high->equity_24h` score `1.3307` n `96` status `ready` deltaP `18.2292` edge `0.1156` maxDD `-4.4325`
- `market_context_high->commodity_1h` score `1.3017` n `66` status `ready` deltaP `15.9363` edge `0.0316` maxDD `-0.3491`
- `news_risk_high->commodity_24h` score `0.9521` n `96` status `ready` deltaP `22.2223` edge `0.1045` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.5791` n `66` status `ready` deltaP `9.7623` edge `0.0048` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.5726` n `101` status `ready` deltaP `16.489` edge `0.0432` maxDD `-2.0994`
- `news_risk_high->metal_24h` score `0.4189` n `96` status `ready` deltaP `17.0139` edge `0.0247` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.234` n `101` status `ready` deltaP `5.5137` edge `0.0233` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.2164` n `66` status `ready` deltaP `6.6776` edge `0.0056` maxDD `-0.4568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
