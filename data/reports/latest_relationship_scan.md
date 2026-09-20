# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T23:37:26.118195+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9028`

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

- `news_risk_high->crypto_major_24h` score `24.7493` n `98` status `ready` deltaP `12.7906` edge `2.663` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3043` n `98` status `ready` deltaP `15.0935` edge `2.0795` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6448` n `101` status `ready` deltaP `20.5958` edge `0.3707` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8125` n `101` status `ready` deltaP `20.4434` edge `0.3072` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7629` n `101` status `ready` deltaP `16.6805` edge `0.1656` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0556` n `101` status `ready` deltaP `18.1775` edge `0.1024` maxDD `-2.8494`
- `market_context_high->fx_1h` score `1.2058` n `51` status `ready` deltaP `16.2469` edge `0.0101` maxDD `-0.1012`
- `news_risk_high->commodity_24h` score `0.9826` n `98` status `ready` deltaP `22.2541` edge `0.1082` maxDD `-3.4467`
- `market_context_high->commodity_4h` score `0.9433` n `43` status `ready` deltaP `25.0284` edge `0.0095` maxDD `-1.7668`
- `news_risk_high->metal_1h` score `0.6448` n `101` status `ready` deltaP `14.8974` edge `0.0146` maxDD `-0.8144`
- `market_context_high->fx_4h` score `0.6119` n `43` status `ready` deltaP `10.848` edge `0.0069` maxDD `-0.2586`
- `news_risk_high->metal_4h` score `0.5972` n `101` status `ready` deltaP `16.9464` edge `0.0422` maxDD `-2.0994`
- `market_context_high->index_1h` score `0.4057` n `51` status `ready` deltaP `6.8774` edge `0.0135` maxDD `-0.0435`
- `news_risk_high->equity_24h` score `0.253` n `98` status `ready` deltaP `15.1821` edge `0.0608` maxDD `-4.941`
- `news_risk_high->fx_4h` score `0.2371` n `101` status `ready` deltaP `9.098` edge `0.0227` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.146` n `51` status `ready` deltaP `4.4529` edge `0.0148` maxDD `-0.2519`
- `market_context_high->equity_1h` score `0.136` n `51` status `ready` deltaP `3.584` edge `0.0241` maxDD `-0.7775`
- `news_risk_high->equity_1h` score `0.0614` n `101` status `ready` deltaP `4.1664` edge `0.0179` maxDD `-0.9112`
- `market_context_high->index_4h` score `0.0012` n `43` status `ready` deltaP `10.9259` edge `-0.009` maxDD `-1.0949`
- `news_risk_high->metal_24h` score `-0.0073` n `98` status `ready` deltaP `13.7684` edge `-0.0083` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
