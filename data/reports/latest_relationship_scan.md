# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T09:07:18.975323+00:00`
- Price records: `672`
- Market context records: `1615`
- Flow alert records: `6559`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `11.7766` n `188` status `ready` deltaP `27.3493` edge `0.9719` maxDD `-8.8275`
- `market_context_high->index_24h` score `3.5431` n `188` status `ready` deltaP `19.5035` edge `0.2822` maxDD `-5.3574`
- `market_context_high->crypto_major_24h` score `2.7122` n `188` status `ready` deltaP `23.5187` edge `0.6588` maxDD `-42.4994`
- `market_context_high->crypto_alt_24h` score `2.3123` n `188` status `ready` deltaP `23.6185` edge `0.8458` maxDD `-60.8455`
- `market_context_high->equity_24h` score `2.207` n `188` status `ready` deltaP `18.0704` edge `0.4279` maxDD `-24.8226`
- `market_context_high->equity_4h` score `1.3513` n `193` status `ready` deltaP `11.2284` edge `0.1472` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.363` n `193` status `ready` deltaP `13.3648` edge `0.2894` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.2083` n `193` status `ready` deltaP `9.4331` edge `0.2347` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.2441` n `188` status `ready` deltaP `7.7201` edge `0.0331` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3078` n `193` status `ready` deltaP `0.4662` edge `0.0598` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5059` n `193` status `ready` deltaP `1.0642` edge `0.0316` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.7001` n `193` status `ready` deltaP `0.1544` edge `0.0038` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8317` n `193` status `ready` deltaP `-0.432` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8734` n `193` status `ready` deltaP `0.2867` edge `0.0342` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.8936` n `193` status `ready` deltaP `-1.2263` edge `0.0293` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.1033` n `193` status `ready` deltaP `-0.121` edge `0.001` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.1659` n `193` status `ready` deltaP `4.6687` edge `0.0053` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.3998` n `193` status `ready` deltaP `8.9457` edge `0.0929` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4083` n `193` status `ready` deltaP `-10.989` edge `-0.0144` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2001` n `193` status `ready` deltaP `-14.1563` edge `-0.1096` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
