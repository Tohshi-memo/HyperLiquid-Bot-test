# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T12:07:30.795190+00:00`
- Price records: `672`
- Market context records: `7455`
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

- `risk_on_high->crypto_major_4h` score `6.6264` n `36` status `ready` deltaP `36.7887` edge `0.3262` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.6264` n `36` status `ready` deltaP `36.7887` edge `0.3262` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.0395` n `32` status `ready` deltaP `16.7732` edge `0.4936` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.0395` n `32` status `ready` deltaP `16.7732` edge `0.4936` maxDD `-5.8371`
- `risk_on_high->unknown_4h` score `4.7402` n `36` status `ready` deltaP `17.1748` edge `0.3235` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.7402` n `36` status `ready` deltaP `17.1748` edge `0.3235` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.7285` n `36` status `ready` deltaP `29.641` edge `0.2208` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.7285` n `36` status `ready` deltaP `29.641` edge `0.2208` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `2.4103` n `32` status `ready` deltaP `17.0927` edge `0.2879` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.4103` n `32` status `ready` deltaP `17.0927` edge `0.2879` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.3537` n `36` status `ready` deltaP `21.5569` edge `0.0543` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3537` n `36` status `ready` deltaP `21.5569` edge `0.0543` maxDD `-0.957`
- `risk_on_high->equity_24h` score `0.9621` n `31` status `ready` deltaP `13.0996` edge `0.2642` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.9621` n `31` status `ready` deltaP `13.0996` edge `0.2642` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.6054` n `36` status `ready` deltaP `7.2822` edge `0.03` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.6054` n `36` status `ready` deltaP `7.2822` edge `0.03` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.5035` n `36` status `ready` deltaP `8.7088` edge `0.0442` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.5035` n `36` status `ready` deltaP `8.7088` edge `0.0442` maxDD `-1.3497`
- `risk_on_high->metal_4h` score `0.4194` n `36` status `ready` deltaP `5.6402` edge `0.0797` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.4194` n `36` status `ready` deltaP `5.6402` edge `0.0797` maxDD `-0.5882`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
