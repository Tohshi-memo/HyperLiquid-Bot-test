# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T17:37:36.557739+00:00`
- Price records: `672`
- Market context records: `7479`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14775`

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

- `risk_on_high->crypto_major_4h` score `7.1999` n `36` status `ready` deltaP `38.6179` edge `0.3618` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1999` n `36` status `ready` deltaP `38.6179` edge `0.3618` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.2459` n `32` status `ready` deltaP `16.7732` edge `0.5108` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.2459` n `32` status `ready` deltaP `16.7732` edge `0.5108` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `4.9983` n `36` status `ready` deltaP `30.4032` edge `0.2382` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.9983` n `36` status `ready` deltaP `30.4032` edge `0.2382` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.5563` n `36` status `ready` deltaP `15.0406` edge `0.3224` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.5563` n `36` status `ready` deltaP `15.0406` edge `0.3224` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.2687` n `32` status `ready` deltaP `16.9194` edge `0.2709` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.2687` n `32` status `ready` deltaP `16.9194` edge `0.2709` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.5384` n `36` status `ready` deltaP `22.7545` edge `0.07` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.5384` n `36` status `ready` deltaP `22.7545` edge `0.07` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.5261` n `36` status `ready` deltaP `6.5315` edge `0.0284` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.5261` n `36` status `ready` deltaP `6.5315` edge `0.0284` maxDD `-0.2479`
- `risk_on_high->fx_24h` score `0.4982` n `31` status `ready` deltaP `16.4993` edge `-0.0005` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.4982` n `31` status `ready` deltaP `16.4993` edge `-0.0005` maxDD `-1.3162`
- `risk_on_high->metal_4h` score `0.4226` n `36` status `ready` deltaP `5.3354` edge `0.082` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.4226` n `36` status `ready` deltaP `5.3354` edge `0.082` maxDD `-0.5882`
- `risk_on_high->equity_1h` score `0.3771` n `36` status `ready` deltaP `7.2073` edge `0.038` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.3771` n `36` status `ready` deltaP `7.2073` edge `0.038` maxDD `-1.3497`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
