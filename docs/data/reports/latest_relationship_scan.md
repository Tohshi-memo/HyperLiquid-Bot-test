# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T20:37:34.691472+00:00`
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

- `market_context_high->unknown_1h` score `318.2524` n `50` status `ready` deltaP `7.2814` edge `26.4774` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.2294` n `50` status `ready` deltaP `7.0122` edge `23.3057` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.1592` n `135` status `ready` deltaP `28.0324` edge `1.264` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9331` n `50` status `ready` deltaP `18.9146` edge `0.522` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3079` n `135` status `ready` deltaP `23.6459` edge `0.6834` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.304` n `135` status `ready` deltaP `24.213` edge `0.5988` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.5655` n `50` status `ready` deltaP `13.5976` edge `0.3358` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0034` n `50` status `ready` deltaP `15.497` edge `0.192` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8703` n `50` status `ready` deltaP `32.2317` edge `0.0378` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8481` n `135` status `ready` deltaP `26.9329` edge `0.1056` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7323` n `135` status `ready` deltaP `21.5393` edge `0.2115` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.641` n `50` status `ready` deltaP `13.4551` edge `0.1967` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3429` n `135` status `ready` deltaP `26.2748` edge `0.1802` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.398` n `50` status `ready` deltaP `19.7425` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7773` n `135` status `ready` deltaP `8.8024` edge `0.0684` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5429` n `135` status `ready` deltaP `7.4551` edge `0.0866` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4658` n `135` status `ready` deltaP `8.6682` edge `0.0098` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0068` n `50` status `ready` deltaP `9.3473` edge `-0.0068` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0094` n `50` status `ready` deltaP `0.8024` edge `0.0585` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `-0.0622` n `135` status `ready` deltaP `7.3013` edge `0.2121` maxDD `-15.9436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
