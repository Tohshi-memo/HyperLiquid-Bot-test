# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T20:46:15.918286+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6840`

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

- `market_context_high->unknown_1h` score `318.238` n `50` status `ready` deltaP `7.1317` edge `26.4772` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.1644` n `50` status `ready` deltaP `6.8598` edge `23.3013` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.2643` n `135` status `ready` deltaP `28.206` edge `1.2716` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9669` n `50` status `ready` deltaP `19.0671` edge `0.5238` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3307` n `135` status `ready` deltaP `23.6459` edge `0.6853` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3052` n `135` status `ready` deltaP `24.213` edge `0.5989` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.6113` n `50` status `ready` deltaP `13.75` edge `0.3386` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.001` n `50` status `ready` deltaP `15.497` edge `0.1918` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8715` n `50` status `ready` deltaP `32.2317` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8469` n `135` status `ready` deltaP `26.9329` edge `0.1055` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7335` n `135` status `ready` deltaP `21.5393` edge `0.2116` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6398` n `50` status `ready` deltaP `13.4551` edge `0.1966` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3429` n `135` status `ready` deltaP `26.2748` edge `0.1802` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3849` n `50` status `ready` deltaP `19.5928` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7785` n `135` status `ready` deltaP `8.8024` edge `0.0685` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5417` n `135` status `ready` deltaP `7.4551` edge `0.0865` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4658` n `135` status `ready` deltaP `8.6682` edge `0.0098` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0068` n `50` status `ready` deltaP `9.3473` edge `-0.0068` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0086` n `50` status `ready` deltaP `0.8024` edge `0.0586` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `-0.0164` n `135` status `ready` deltaP `7.4537` edge `0.2149` maxDD `-15.9436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
