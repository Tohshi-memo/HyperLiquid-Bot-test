# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T04:22:23.242450+00:00`
- Price records: `672`
- Market context records: `7528`
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

- `risk_on_high->crypto_major_4h` score `7.6142` n `36` status `ready` deltaP `40.7521` edge `0.3821` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.6142` n `36` status `ready` deltaP `40.7521` edge `0.3821` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.422` n `32` status `ready` deltaP `17.6397` edge `0.5197` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.422` n `32` status `ready` deltaP `17.6397` edge `0.5197` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.1057` n `36` status `ready` deltaP `30.8605` edge `0.2441` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.1057` n `36` status `ready` deltaP `30.8605` edge `0.2441` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.5375` n `36` status `ready` deltaP `15.3455` edge `0.3188` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.5375` n `36` status `ready` deltaP `15.3455` edge `0.3188` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.0373` n `32` status `ready` deltaP `16.3995` edge `0.2447` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.0373` n `32` status `ready` deltaP `16.3995` edge `0.2447` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.6623` n `36` status `ready` deltaP `24.4012` edge `0.0749` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.6623` n `36` status `ready` deltaP `24.4012` edge `0.0749` maxDD `-0.957`
- `risk_on_high->fx_24h` score `0.5727` n `31` status `ready` deltaP `16.3254` edge `0.0102` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.5727` n `31` status `ready` deltaP `16.3254` edge `0.0102` maxDD `-1.3162`
- `risk_on_high->equity_1h` score `0.5636` n `36` status `ready` deltaP `9.3094` edge `0.0479` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.5636` n `36` status `ready` deltaP `9.3094` edge `0.0479` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.5273` n `36` status `ready` deltaP `6.5315` edge `0.0285` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.5273` n `36` status `ready` deltaP `6.5315` edge `0.0285` maxDD `-0.2479`
- `risk_on_high->crypto_alt_1h` score `0.3085` n `36` status `ready` deltaP `3.2269` edge `0.0551` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.3085` n `36` status `ready` deltaP `3.2269` edge `0.0551` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
