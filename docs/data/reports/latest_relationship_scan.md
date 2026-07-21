# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T16:52:27.234817+00:00`
- Price records: `672`
- Market context records: `7476`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14727`

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

- `risk_on_high->crypto_major_4h` score `7.1673` n `36` status `ready` deltaP `38.4655` edge `0.3601` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1673` n `36` status `ready` deltaP `38.4655` edge `0.3601` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.2255` n `32` status `ready` deltaP `16.7732` edge `0.5091` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.2255` n `32` status `ready` deltaP `16.7732` edge `0.5091` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.0103` n `36` status `ready` deltaP `30.4032` edge `0.2392` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.0103` n `36` status `ready` deltaP `30.4032` edge `0.2392` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.5745` n `36` status `ready` deltaP `15.1931` edge `0.3229` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.5745` n `36` status `ready` deltaP `15.1931` edge `0.3229` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.3003` n `32` status `ready` deltaP `17.0927` edge `0.2738` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.3003` n `32` status `ready` deltaP `17.0927` edge `0.2738` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.533` n `36` status `ready` deltaP `22.6048` edge `0.0703` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.533` n `36` status `ready` deltaP `22.6048` edge `0.0703` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.5429` n `36` status `ready` deltaP `6.6816` edge `0.0288` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.5429` n `36` status `ready` deltaP `6.6816` edge `0.0288` maxDD `-0.2479`
- `risk_on_high->fx_24h` score `0.4936` n `31` status `ready` deltaP `16.4993` edge `-0.0011` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.4936` n `31` status `ready` deltaP `16.4993` edge `-0.0011` maxDD `-1.3162`
- `risk_on_high->metal_4h` score `0.4554` n `36` status `ready` deltaP `5.6402` edge `0.0827` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.4554` n `36` status `ready` deltaP `5.6402` edge `0.0827` maxDD `-0.5882`
- `risk_on_high->equity_1h` score `0.3888` n `36` status `ready` deltaP `7.3574` edge `0.0385` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.3888` n `36` status `ready` deltaP `7.3574` edge `0.0385` maxDD `-1.3497`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
