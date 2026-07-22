# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T02:22:24.478219+00:00`
- Price records: `672`
- Market context records: `7520`
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

- `risk_on_high->crypto_major_4h` score `7.4635` n `36` status `ready` deltaP `40.1423` edge `0.3736` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.4635` n `36` status `ready` deltaP `40.1423` edge `0.3736` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.2699` n `32` status `ready` deltaP `16.7732` edge `0.5128` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.2699` n `32` status `ready` deltaP `16.7732` edge `0.5128` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.0707` n `36` status `ready` deltaP `30.708` edge `0.2422` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.0707` n `36` status `ready` deltaP `30.708` edge `0.2422` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.4405` n `36` status `ready` deltaP `14.5833` edge `0.3158` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.4405` n `36` status `ready` deltaP `14.5833` edge `0.3158` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.0424` n `32` status `ready` deltaP `16.5728` edge `0.2442` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.0424` n `32` status `ready` deltaP `16.5728` edge `0.2442` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.589` n `36` status `ready` deltaP `23.6527` edge `0.0705` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.589` n `36` status `ready` deltaP `23.6527` edge `0.0705` maxDD `-0.957`
- `risk_on_high->fx_24h` score `0.5633` n `31` status `ready` deltaP `16.3254` edge `0.009` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.5633` n `31` status `ready` deltaP `16.3254` edge `0.009` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.4733` n `36` status `ready` deltaP `5.9309` edge `0.028` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.4733` n `36` status `ready` deltaP `5.9309` edge `0.028` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.4497` n `36` status `ready` deltaP `8.2583` edge `0.0403` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.4497` n `36` status `ready` deltaP `8.2583` edge `0.0403` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.2882` n `36` status `ready` deltaP `3.0772` edge `0.0535` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.2882` n `36` status `ready` deltaP `3.0772` edge `0.0535` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
