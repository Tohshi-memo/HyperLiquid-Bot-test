# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T02:52:24.526677+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10425`

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

- `risk_on_high->unknown_24h` score `492.8681` n `96` status `ready` deltaP `26.7361` edge `40.8941` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `492.8681` n `96` status `ready` deltaP `26.7361` edge `40.8941` maxDD `0.0`
- `market_context_high->unknown_1h` score `22.3282` n `244` status `ready` deltaP `-2.9646` edge `1.9529` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `20.4454` n `96` status `ready` deltaP `33.5069` edge `1.5321` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.4454` n `96` status `ready` deltaP `33.5069` edge `1.5321` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.0868` n `96` status `ready` deltaP `30.5556` edge `0.9702` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.0868` n `96` status `ready` deltaP `30.5556` edge `0.9702` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.9324` n `185` status `ready` deltaP `24.0691` edge `0.6414` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.5824` n `185` status `ready` deltaP `23.0903` edge `0.3946` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.3944` n `96` status `ready` deltaP `23.0903` edge `0.2956` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.3944` n `96` status `ready` deltaP `23.0903` edge `0.2956` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.3842` n `120` status `ready` deltaP `28.9126` edge `0.2931` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3842` n `120` status `ready` deltaP `28.9126` edge `0.2931` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `3.8675` n `120` status `ready` deltaP `22.0732` edge `0.261` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.8675` n `120` status `ready` deltaP `22.0732` edge `0.261` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7151` n `96` status `ready` deltaP `23.2639` edge `0.0754` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7151` n `96` status `ready` deltaP `23.2639` edge `0.0754` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6031` n `185` status `ready` deltaP `21.524` edge `0.0949` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `0.9048` n `96` status `ready` deltaP `15.9722` edge `0.1251` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.9048` n `96` status `ready` deltaP `15.9722` edge `0.1251` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
