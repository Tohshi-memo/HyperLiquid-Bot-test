# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T22:22:31.505575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6836`

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

- `market_context_high->unknown_1h` score `318.1168` n `50` status `ready` deltaP `7.2814` edge `26.4661` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.0274` n `50` status `ready` deltaP `6.7073` edge `23.2909` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.8238` n `135` status `ready` deltaP `28.9004` edge `1.3136` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9923` n `50` status `ready` deltaP `19.2195` edge `0.5249` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3787` n `135` status `ready` deltaP `23.6459` edge `0.6893` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3316` n `135` status `ready` deltaP `24.213` edge `0.6011` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.7839` n `50` status `ready` deltaP `14.5122` edge `0.3479` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0178` n `50` status `ready` deltaP `15.497` edge `0.1932` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8715` n `50` status `ready` deltaP `32.2317` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8397` n `135` status `ready` deltaP `26.9329` edge `0.1049` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7455` n `135` status `ready` deltaP `21.5393` edge `0.2126` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6842` n `50` status `ready` deltaP `13.6048` edge `0.1993` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3405` n `135` status `ready` deltaP `26.2748` edge `0.18` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3609` n `50` status `ready` deltaP `19.2934` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.818` n `135` status `ready` deltaP `9.1018` edge `0.0698` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.586` n `135` status `ready` deltaP `7.6048` edge `0.0892` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4801` n `135` status `ready` deltaP `8.8179` edge `0.01` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.1561` n `135` status `ready` deltaP `8.2159` edge `0.2242` maxDD `-15.9436`
- `market_context_high->equity_1h` score `0.0171` n `50` status `ready` deltaP `1.1018` edge `0.0599` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `0.0052` n `50` status `ready` deltaP `9.3473` edge `-0.007` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
