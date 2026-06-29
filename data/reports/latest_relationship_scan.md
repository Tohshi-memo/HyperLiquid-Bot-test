# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T03:22:30.651662+00:00`
- Price records: `672`
- Market context records: `5105`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `18.8983` n `79` status `ready` deltaP `28.0678` edge `1.422` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2445` n `112` status `ready` deltaP `22.9747` edge `0.6361` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.3793` n `124` status `ready` deltaP `4.689` edge `0.5645` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `3.141` n `112` status `ready` deltaP `14.8519` edge `0.4636` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.4467` n `112` status `ready` deltaP `13.2186` edge `0.4548` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `1.0624` n `124` status `ready` deltaP `7.9486` edge `0.1317` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.5849` n `112` status `ready` deltaP `8.3624` edge `0.1584` maxDD `-6.4661`
- `market_context_high->crypto_major_1h` score `0.5731` n `124` status `ready` deltaP `8.8227` edge `0.1392` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.4738` n `124` status `ready` deltaP `8.813` edge `0.0613` maxDD `-2.745`
- `market_context_high->metal_1h` score `0.3784` n `124` status `ready` deltaP `9.8947` edge `0.0322` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.0438` n `124` status `ready` deltaP `4.9884` edge `0.0115` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2495` n `112` status `ready` deltaP `5.0305` edge `0.0281` maxDD `-2.49`
- `market_context_high->metal_4h` score `-0.3693` n `112` status `ready` deltaP `3.8981` edge `0.0677` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.8041` n `124` status `ready` deltaP `-5.6693` edge `-0.0012` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9544` n `124` status `ready` deltaP `-0.4733` edge `-0.0006` maxDD `-2.062`
- `market_context_high->fx_24h` score `-1.6547` n `79` status `ready` deltaP `-4.1842` edge `-0.0088` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.6815` n `79` status `ready` deltaP `7.7004` edge `0.0293` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-1.7497` n `112` status `ready` deltaP `-5.3571` edge `-0.0028` maxDD `-1.9169`
- `market_context_high->commodity_4h` score `-2.1558` n `112` status `ready` deltaP `1.9817` edge `-0.0219` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-4.5805` n `79` status `ready` deltaP `-6.7731` edge `0.0034` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
