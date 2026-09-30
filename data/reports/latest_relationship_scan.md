# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T20:07:34.051219+00:00`
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

- `market_context_high->unknown_1h` score `318.5679` n `50` status `ready` deltaP `7.5808` edge `26.5017` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.4674` n `50` status `ready` deltaP `7.3171` edge `23.3235` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9996` n `135` status `ready` deltaP `28.0324` edge `1.2507` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8727` n `50` status `ready` deltaP `18.6098` edge `0.519` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.3112` n `135` status `ready` deltaP `24.213` edge `0.5994` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.2731` n `135` status `ready` deltaP `23.6459` edge `0.6805` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.4907` n `50` status `ready` deltaP `13.2927` edge `0.3316` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0166` n `50` status `ready` deltaP `15.6467` edge `0.1921` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8959` n `50` status `ready` deltaP `32.5366` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8529` n `135` status `ready` deltaP `26.9329` edge `0.106` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7287` n `135` status `ready` deltaP `21.5393` edge `0.2112` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6602` n `50` status `ready` deltaP `13.6048` edge `0.1973` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3271` n `135` status `ready` deltaP `26.1224` edge `0.1799` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7641` n `135` status `ready` deltaP `8.6527` edge `0.0683` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.562` n `135` status `ready` deltaP `7.6048` edge `0.0872` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4526` n `135` status `ready` deltaP `8.5185` edge `0.0097` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0146` n `50` status `ready` deltaP `9.497` edge `-0.0068` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.018` n `50` status `ready` deltaP `0.6527` edge `0.0584` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `-0.137` n `135` status `ready` deltaP `6.9964` edge `0.2079` maxDD `-15.9436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
