# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T02:07:33.318264+00:00`
- Price records: `672`
- Market context records: `7519`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14782`

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

- `risk_on_high->crypto_major_4h` score `8.0879` n `36` status `ready` deltaP `40.1423` edge `0.4272` maxDD `-0.9991`
- `risk_on_and_context->crypto_major_4h` score `8.0879` n `36` status `ready` deltaP `40.1423` edge `0.4272` maxDD `-0.9991`
- `risk_on_high->crypto_major_24h` score `6.9716` n `32` status `ready` deltaP `16.7732` edge `0.5817` maxDD `-6.671`
- `risk_on_and_context->crypto_major_24h` score `6.9716` n `32` status `ready` deltaP `16.7732` edge `0.5817` maxDD `-6.671`
- `risk_on_high->crypto_alt_4h` score `5.0951` n `36` status `ready` deltaP `30.8605` edge `0.2434` maxDD `-0.9638`
- `risk_on_and_context->crypto_alt_4h` score `5.0951` n `36` status `ready` deltaP `30.8605` edge `0.2434` maxDD `-0.9638`
- `risk_on_high->unknown_4h` score `4.2634` n `36` status `ready` deltaP `18.4282` edge `0.2751` maxDD `-0.4136`
- `risk_on_and_context->unknown_4h` score `4.2634` n `36` status `ready` deltaP `18.4282` edge `0.2751` maxDD `-0.4136`
- `risk_on_high->crypto_alt_24h` score `2.0694` n `32` status `ready` deltaP `16.3995` edge `0.2497` maxDD `-5.1642`
- `risk_on_and_context->crypto_alt_24h` score `2.0694` n `32` status `ready` deltaP `16.3995` edge `0.2497` maxDD `-5.1642`
- `risk_on_high->crypto_major_1h` score `1.6662` n `36` status `ready` deltaP `23.8024` edge `0.0811` maxDD `-1.0937`
- `risk_on_and_context->crypto_major_1h` score `1.6662` n `36` status `ready` deltaP `23.8024` edge `0.0811` maxDD `-1.0937`
- `risk_on_high->crypto_alt_1h` score `0.2916` n `36` status `ready` deltaP `3.0772` edge `0.0542` maxDD `-0.9866`
- `risk_on_and_context->crypto_alt_1h` score `0.2916` n `36` status `ready` deltaP `3.0772` edge `0.0542` maxDD `-0.9866`
- `risk_on_high->metal_4h` score `0.2237` n `36` status `ready` deltaP `3.6585` edge `0.0766` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.2237` n `36` status `ready` deltaP `3.6585` edge `0.0766` maxDD `-0.5882`
- `risk_on_high->unknown_24h` score `0.0921` n `32` status `ready` deltaP `8.9526` edge `0.0142` maxDD `-2.6323`
- `risk_on_and_context->unknown_24h` score `0.0921` n `32` status `ready` deltaP `8.9526` edge `0.0142` maxDD `-2.6323`
- `risk_on_high->equity_1h` score `-0.2801` n `36` status `ready` deltaP `-5.405` edge `0.0774` maxDD `-1.5154`
- `risk_on_and_context->equity_1h` score `-0.2801` n `36` status `ready` deltaP `-5.405` edge `0.0774` maxDD `-1.5154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
