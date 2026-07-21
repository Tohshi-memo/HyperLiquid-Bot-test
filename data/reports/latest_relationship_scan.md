# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T12:22:30.243838+00:00`
- Price records: `672`
- Market context records: `7456`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14679`

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

- `risk_on_high->crypto_major_4h` score `6.6818` n `36` status `ready` deltaP `36.9411` edge `0.3298` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.6818` n `36` status `ready` deltaP `36.9411` edge `0.3298` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.0587` n `32` status `ready` deltaP `16.7732` edge `0.4952` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.0587` n `32` status `ready` deltaP `16.7732` edge `0.4952` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `4.7597` n `36` status `ready` deltaP `29.641` edge `0.2234` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.7597` n `36` status `ready` deltaP `29.641` edge `0.2234` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.7534` n `36` status `ready` deltaP `17.1748` edge `0.3246` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.7534` n `36` status `ready` deltaP `17.1748` edge `0.3246` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.4087` n `32` status `ready` deltaP `17.0927` edge `0.2877` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.4087` n `32` status `ready` deltaP `17.0927` edge `0.2877` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.342` n `36` status `ready` deltaP `21.4072` edge `0.0538` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.342` n `36` status `ready` deltaP `21.4072` edge `0.0538` maxDD `-0.957`
- `risk_on_high->equity_24h` score `0.9657` n `31` status `ready` deltaP `13.0996` edge `0.2645` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.9657` n `31` status `ready` deltaP `13.0996` edge `0.2645` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.591` n `36` status `ready` deltaP `7.1321` edge `0.0298` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.591` n `36` status `ready` deltaP `7.1321` edge `0.0298` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.4942` n `36` status `ready` deltaP `8.5586` edge `0.044` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.4942` n `36` status `ready` deltaP `8.5586` edge `0.044` maxDD `-1.3497`
- `risk_on_high->metal_4h` score `0.446` n `36` status `ready` deltaP `5.7927` edge `0.0809` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.446` n `36` status `ready` deltaP `5.7927` edge `0.0809` maxDD `-0.5882`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
