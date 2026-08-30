# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T22:52:42.204860+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `risk_on_high->crypto_alt_24h` score `23.5559` n `51` status `ready` deltaP `48.9583` edge `1.6366` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `23.5559` n `51` status `ready` deltaP `48.9583` edge `1.6366` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `11.4269` n `51` status `ready` deltaP `32.1589` edge `0.781` maxDD `-2.4524`
- `risk_on_and_context->crypto_major_24h` score `11.4269` n `51` status `ready` deltaP `32.1589` edge `0.781` maxDD `-2.4524`
- `risk_on_high->unknown_4h` score `8.8126` n `81` status `ready` deltaP `30.1848` edge `0.576` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.8126` n `81` status `ready` deltaP `30.1848` edge `0.576` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.1928` n `51` status `ready` deltaP `69.4444` edge `0.0531` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1928` n `51` status `ready` deltaP `69.4444` edge `0.0531` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.0753` n `149` status `ready` deltaP `21.054` edge `0.3296` maxDD `-1.0945`
- `risk_on_high->metal_24h` score `4.8983` n `51` status `ready` deltaP `44.3628` edge `0.1386` maxDD `-0.4264`
- `risk_on_and_context->metal_24h` score `4.8983` n `51` status `ready` deltaP `44.3628` edge `0.1386` maxDD `-0.4264`
- `risk_on_high->unknown_1h` score `4.3492` n `91` status `ready` deltaP `11.3954` edge `0.3109` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.3492` n `91` status `ready` deltaP `11.3954` edge `0.3109` maxDD `-0.2885`
- `market_context_high->crypto_major_24h` score `4.3311` n `117` status `ready` deltaP `17.4279` edge `0.498` maxDD `-17.2607`
- `market_context_high->metal_24h` score `4.2053` n `117` status `ready` deltaP `33.6539` edge `0.228` maxDD `-3.1535`
- `market_context_high->crypto_alt_24h` score `3.5927` n `117` status `ready` deltaP `17.3344` edge `0.764` maxDD `-27.517`
- `risk_on_high->equity_24h` score `3.3049` n `51` status `ready` deltaP `24.9898` edge `0.1352` maxDD `-0.7778`
- `risk_on_and_context->equity_24h` score `3.3049` n `51` status `ready` deltaP `24.9898` edge `0.1352` maxDD `-0.7778`
- `market_context_high->unknown_1h` score `2.9374` n `161` status `ready` deltaP `10.3442` edge `0.2167` maxDD `-0.9372`
- `risk_on_high->index_24h` score `1.7601` n `51` status `ready` deltaP `23.7541` edge `0.0081` maxDD `-0.2492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
