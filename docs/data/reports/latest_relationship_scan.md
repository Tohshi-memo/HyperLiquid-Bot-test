# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T04:37:31.100016+00:00`
- Price records: `672`
- Market context records: `7529`
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

- `risk_on_high->crypto_major_4h` score `7.6336` n `36` status `ready` deltaP `40.9045` edge `0.3827` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.6336` n `36` status `ready` deltaP `40.9045` edge `0.3827` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.428` n `32` status `ready` deltaP `17.6397` edge `0.5202` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.428` n `32` status `ready` deltaP `17.6397` edge `0.5202` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.1081` n `36` status `ready` deltaP `30.8605` edge `0.2443` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.1081` n `36` status `ready` deltaP `30.8605` edge `0.2443` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.5593` n `36` status `ready` deltaP `15.4979` edge `0.3196` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.5593` n `36` status `ready` deltaP `15.4979` edge `0.3196` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.0404` n `32` status `ready` deltaP `16.3995` edge `0.2451` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.0404` n `32` status `ready` deltaP `16.3995` edge `0.2451` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.6615` n `36` status `ready` deltaP `24.4012` edge `0.0748` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.6615` n `36` status `ready` deltaP `24.4012` edge `0.0748` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.5753` n `36` status `ready` deltaP `9.4595` edge `0.0484` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.5753` n `36` status `ready` deltaP `9.4595` edge `0.0484` maxDD `-1.3497`
- `risk_on_high->fx_24h` score `0.5734` n `31` status `ready` deltaP `16.3254` edge `0.0103` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.5734` n `31` status `ready` deltaP `16.3254` edge `0.0103` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.5141` n `36` status `ready` deltaP `6.3813` edge `0.0284` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.5141` n `36` status `ready` deltaP `6.3813` edge `0.0284` maxDD `-0.2479`
- `risk_on_high->crypto_alt_1h` score `0.3085` n `36` status `ready` deltaP `3.2269` edge `0.0551` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.3085` n `36` status `ready` deltaP `3.2269` edge `0.0551` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
