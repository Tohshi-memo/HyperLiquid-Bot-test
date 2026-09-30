# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T21:07:41.421001+00:00`
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

- `market_context_high->unknown_1h` score `318.2548` n `50` status `ready` deltaP `7.2814` edge `26.4776` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.1138` n `50` status `ready` deltaP `6.7073` edge `23.2981` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.3694` n `135` status `ready` deltaP `28.3796` edge `1.2792` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0055` n `50` status `ready` deltaP `19.2195` edge `0.526` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3475` n `135` status `ready` deltaP `23.6459` edge `0.6867` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.31` n `135` status `ready` deltaP `24.213` edge `0.5993` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.6607` n `50` status `ready` deltaP `13.9024` edge `0.3417` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0094` n `50` status `ready` deltaP `15.497` edge `0.1925` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8715` n `50` status `ready` deltaP `32.2317` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8457` n `135` status `ready` deltaP `26.9329` edge `0.1054` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7359` n `135` status `ready` deltaP `21.5393` edge `0.2118` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6554` n `50` status `ready` deltaP `13.4551` edge `0.1979` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3489` n `135` status `ready` deltaP `26.2748` edge `0.1807` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3849` n `50` status `ready` deltaP `19.5928` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7929` n `135` status `ready` deltaP `8.9521` edge `0.0687` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5573` n `135` status `ready` deltaP `7.4551` edge `0.0878` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.467` n `135` status `ready` deltaP `8.6682` edge `0.0099` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.0329` n `135` status `ready` deltaP `7.6061` edge `0.218` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `0.0068` n `50` status `ready` deltaP `9.3473` edge `-0.0068` maxDD `-2.3717`
- `market_context_high->equity_1h` score `0.0007` n `50` status `ready` deltaP `0.9521` edge `0.0588` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
