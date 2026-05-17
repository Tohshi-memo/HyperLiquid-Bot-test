# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T10:07:12.343417+00:00`
- Price records: `672`
- Market context records: `1002`
- Flow alert records: `4791`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `12.9662` n `210` status `ready` deltaP `31.8399` edge `0.9271` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1806` n `210` status `ready` deltaP `10.8874` edge `0.3992` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.362` n `210` status `ready` deltaP `1.795` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.533` n `210` status `ready` deltaP `2.5449` edge `0.0194` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6533` n `210` status `ready` deltaP `0.9481` edge `0.0161` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.7198` n `210` status `ready` deltaP `3.052` edge `0.1184` maxDD `-5.8987`
- `market_context_high->index_1h` score `-0.7293` n `210` status `ready` deltaP `2.9213` edge `0.0051` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7549` n `210` status `ready` deltaP `0.3247` edge `0.0007` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2142` n `210` status `ready` deltaP `4.9244` edge `-0.0162` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.2426` n `210` status `ready` deltaP `4.6537` edge `0.1259` maxDD `-10.5047`
- `market_context_high->crypto_alt_1h` score `-1.3334` n `210` status `ready` deltaP `-0.6415` edge `-0.0227` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5032` n `210` status `ready` deltaP `1.9264` edge `0.0771` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7442` n `210` status `ready` deltaP `-1.6017` edge `0.0176` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8503` n `210` status `ready` deltaP `-0.4776` edge `-0.0381` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.9158` n `210` status `ready` deltaP `7.1429` edge `0.08` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.219` n `210` status `ready` deltaP `-1.5584` edge `0.0589` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3085` n `210` status `ready` deltaP `-1.9048` edge `0.0148` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5754` n `210` status `ready` deltaP `-1.9264` edge `-0.0229` maxDD `-20.1443`
- `market_context_high->metal_4h` score `-4.6041` n `210` status `ready` deltaP `-4.6753` edge `-0.1634` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.1361` n `210` status `ready` deltaP `2.8788` edge `0.4025` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
