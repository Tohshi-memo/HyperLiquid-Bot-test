# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T23:22:29.711313+00:00`
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

- `market_context_high->unknown_1h` score `318.0724` n `50` status `ready` deltaP `6.982` edge `26.4644` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `279.9674` n `50` status `ready` deltaP `6.7073` edge `23.2859` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.089` n `135` status `ready` deltaP `28.9004` edge `1.3357` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9379` n `50` status `ready` deltaP `18.9146` edge `0.5224` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3751` n `135` status `ready` deltaP `23.6459` edge `0.689` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3316` n `135` status `ready` deltaP `24.213` edge `0.6011` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.8163` n `50` status `ready` deltaP `14.5122` edge `0.3506` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9938` n `50` status `ready` deltaP `15.3473` edge `0.1922` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8715` n `50` status `ready` deltaP `32.2317` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8313` n `135` status `ready` deltaP `26.9329` edge `0.1042` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7551` n `135` status `ready` deltaP `21.5393` edge `0.2134` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6182` n `50` status `ready` deltaP `13.3054` edge `0.1958` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.2969` n `135` status `ready` deltaP `25.9699` edge `0.1784` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3717` n `50` status `ready` deltaP `19.4431` edge `0.0111` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7497` n `135` status `ready` deltaP `8.503` edge `0.0681` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5201` n `135` status `ready` deltaP `7.3054` edge `0.0857` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.425` n `135` status `ready` deltaP `8.2191` edge `0.0094` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.1885` n `135` status `ready` deltaP `8.2159` edge `0.2269` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `0.0052` n `50` status `ready` deltaP `9.3473` edge `-0.007` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0273` n `50` status `ready` deltaP `0.503` edge `0.0582` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
