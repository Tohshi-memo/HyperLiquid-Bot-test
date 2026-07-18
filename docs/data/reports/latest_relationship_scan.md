# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T19:37:23.863068+00:00`
- Price records: `672`
- Market context records: `7173`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `risk_on_high->commodity_1h` score `1.9969` n `34` status `ready` deltaP `21.6802` edge `0.0369` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `1.9969` n `34` status `ready` deltaP `21.6802` edge `0.0369` maxDD `-0.2021`
- `risk_on_high->crypto_major_1h` score `0.4414` n `34` status `ready` deltaP `9.1229` edge `0.0248` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.4414` n `34` status `ready` deltaP `9.1229` edge `0.0248` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.3634` n `34` status `ready` deltaP `3.945` edge `0.034` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3634` n `34` status `ready` deltaP `3.945` edge `0.034` maxDD `-0.7345`
- `market_context_high->fx_1h` score `-0.2831` n `172` status `ready` deltaP `1.7616` edge `0.0009` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.5307` n `172` status `ready` deltaP `4.9506` edge `0.04` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.5326` n `160` status `ready` deltaP `9.3293` edge `0.0093` maxDD `-1.2705`
- `market_context_high->commodity_1h` score `-0.5541` n `172` status `ready` deltaP `0.4422` edge `-0.0119` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.6194` n `172` status `ready` deltaP `-0.3795` edge `0.027` maxDD `-5.9775`
- `market_context_high->unknown_1h` score `-0.6579` n `172` status `ready` deltaP `-1.4901` edge `0.0193` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.8567` n `172` status `ready` deltaP `-0.1079` edge `-0.0042` maxDD `-2.3175`
- `risk_on_high->fx_1h` score `-1.0183` n `34` status `ready` deltaP `-8.2247` edge `-0.0022` maxDD `-0.2261`
- `risk_on_and_context->fx_1h` score `-1.0183` n `34` status `ready` deltaP `-8.2247` edge `-0.0022` maxDD `-0.2261`
- `market_context_high->metal_1h` score `-1.3717` n `172` status `ready` deltaP `-7.9481` edge `-0.0051` maxDD `-2.0882`
- `risk_on_high->crypto_alt_1h` score `-1.5331` n `34` status `ready` deltaP `-12.7598` edge `-0.0005` maxDD `-1.3755`
- `risk_on_and_context->crypto_alt_1h` score `-1.5331` n `34` status `ready` deltaP `-12.7598` edge `-0.0005` maxDD `-1.3755`
- `risk_on_high->index_1h` score `-1.5454` n `34` status `ready` deltaP `-14.3008` edge `-0.0004` maxDD `-0.3101`
- `risk_on_and_context->index_1h` score `-1.5454` n `34` status `ready` deltaP `-14.3008` edge `-0.0004` maxDD `-0.3101`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
