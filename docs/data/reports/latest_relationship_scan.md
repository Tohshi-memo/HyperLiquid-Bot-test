# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T12:22:28.149494+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `28.4068` n `42` status `ready` deltaP `34.7966` edge `2.195` maxDD `-3.113`
- `market_context_high->crypto_major_24h` score `27.099` n `42` status `ready` deltaP `46.4285` edge `1.9971` maxDD `-2.2034`
- `risk_on_high->crypto_alt_4h` score `3.8976` n `48` status `ready` deltaP `18.1911` edge `0.2483` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.8976` n `48` status `ready` deltaP `18.1911` edge `0.2483` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4965` n `48` status `ready` deltaP `32.8252` edge `0.3147` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4965` n `48` status `ready` deltaP `32.8252` edge `0.3147` maxDD `-4.1548`
- `market_context_high->metal_24h` score `3.0759` n `42` status `ready` deltaP `27.9018` edge `0.0936` maxDD `-0.5294`
- `market_context_high->crypto_major_4h` score `2.5263` n `104` status `ready` deltaP `16.1585` edge `0.2806` maxDD `-8.5569`
- `market_context_high->crypto_alt_4h` score `2.3175` n `104` status `ready` deltaP `10.659` edge `0.2944` maxDD `-11.1201`
- `market_context_high->crypto_alt_1h` score `1.3943` n `104` status `ready` deltaP `11.0663` edge `0.1375` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.8627` n `48` status `ready` deltaP `5.9381` edge `0.092` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8627` n `48` status `ready` deltaP `5.9381` edge `0.092` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.5197` n `104` status `ready` deltaP `3.6331` edge `0.0954` maxDD `-3.4384`
- `market_context_high->index_24h` score `0.5032` n `42` status `ready` deltaP `12.5744` edge `0.0674` maxDD `-1.2711`
- `risk_on_high->crypto_major_1h` score `0.3571` n `48` status `ready` deltaP `4.9152` edge `0.0783` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3571` n `48` status `ready` deltaP `4.9152` edge `0.0783` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `0.1837` n `104` status `ready` deltaP `-4.6435` edge `0.1109` maxDD `-1.8373`
- `market_context_high->index_1h` score `0.0102` n `104` status `ready` deltaP `4.7213` edge `0.0029` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.0273` n `104` status `ready` deltaP `7.3065` edge `0.0051` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.3555` n `48` status `ready` deltaP `2.8194` edge `0.0035` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
