# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T17:37:27.320222+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10461`

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

- `risk_on_high->unknown_24h` score `245.2792` n `102` status `ready` deltaP `23.0903` edge `20.286` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `245.2792` n `102` status `ready` deltaP `23.0903` edge `20.286` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `17.4325` n `102` status `ready` deltaP `31.6585` edge `1.3859` maxDD `-8.5397`
- `risk_on_and_context->crypto_major_24h` score `17.4325` n `102` status `ready` deltaP `31.6585` edge `1.3859` maxDD `-8.5397`
- `risk_on_high->crypto_alt_24h` score `13.2692` n `102` status `ready` deltaP `31.4849` edge `0.902` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `13.2692` n `102` status `ready` deltaP `31.4849` edge `0.902` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `7.6509` n `214` status `ready` deltaP `24.5214` edge `0.5316` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.6738` n `117` status `ready` deltaP `30.1777` edge `0.3088` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.6738` n `117` status `ready` deltaP `30.1777` edge `0.3088` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.0053` n `117` status `ready` deltaP `26.5909` edge `0.3257` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0053` n `117` status `ready` deltaP `26.5909` edge `0.3257` maxDD `-3.8693`
- `market_context_high->equity_24h` score `4.2912` n `214` status `ready` deltaP `16.3194` edge `0.2488` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.5436` n `102` status `ready` deltaP `16.3194` edge `0.1865` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.5436` n `102` status `ready` deltaP `16.3194` edge `0.1865` maxDD `0.0`
- `risk_on_high->index_24h` score `2.0334` n `102` status `ready` deltaP `17.8921` edge `0.0544` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.0334` n `102` status `ready` deltaP `17.8921` edge `0.0544` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.2811` n `214` status `ready` deltaP `12.4221` edge `0.0633` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.0028` n `117` status `ready` deltaP `4.6958` edge `0.0875` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0028` n `117` status `ready` deltaP `4.6958` edge `0.0875` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6407` n `102` status `ready` deltaP `17.2386` edge `0.0828` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
