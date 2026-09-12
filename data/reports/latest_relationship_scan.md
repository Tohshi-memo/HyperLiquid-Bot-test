# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T18:22:33.204271+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12881`

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

- `market_context_high->unknown_24h` score `8638.7455` n `82` status `ready` deltaP `13.0124` edge `719.8139` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `5773.6309` n `42` status `ready` deltaP `15.4514` edge `481.0329` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5773.6309` n `42` status `ready` deltaP `15.4514` edge `481.0329` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.0332` n `82` status `ready` deltaP `-5.4002` edge `31.9976` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.7392` n `69` status `ready` deltaP `46.4976` edge `1.5379` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.2` n `69` status `ready` deltaP `29.8837` edge `1.2829` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.4369` n `42` status `ready` deltaP `38.2688` edge `1.1376` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.4369` n `42` status `ready` deltaP `38.2688` edge `1.1376` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.3277` n `82` status `ready` deltaP `30.6614` edge `1.0723` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.77` n `42` status `ready` deltaP `41.3194` edge `0.5387` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.77` n `42` status `ready` deltaP `41.3194` edge `0.5387` maxDD `0.0`
- `market_context_high->equity_24h` score `9.4376` n `82` status `ready` deltaP `41.3194` edge `0.511` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.1726` n `69` status `ready` deltaP `23.9281` edge `0.6856` maxDD `-3.1258`
- `risk_on_high->crypto_alt_4h` score `8.3056` n `47` status `ready` deltaP `41.9402` edge `0.4497` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.3056` n `47` status `ready` deltaP `41.9402` edge `0.4497` maxDD `-1.9733`
- `news_risk_high->index_24h` score `6.6973` n `69` status `ready` deltaP `43.9009` edge `0.2831` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.46` n `69` status `ready` deltaP `41.2968` edge `0.3071` maxDD `-0.526`
- `risk_on_high->index_24h` score `4.9354` n `42` status `ready` deltaP `49.8015` edge `0.0835` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9354` n `42` status `ready` deltaP `49.8015` edge `0.0835` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `3.9334` n `47` status `ready` deltaP `34.6361` edge `0.1062` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
