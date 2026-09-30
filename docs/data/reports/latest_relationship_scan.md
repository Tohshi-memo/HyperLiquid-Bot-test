# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T20:22:46.525434+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6624`

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

- `market_context_high->unknown_1h` score `318.2679` n `50` status `ready` deltaP `7.4311` edge `26.4777` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.304` n `50` status `ready` deltaP `7.1646` edge `23.3109` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.0788` n `135` status `ready` deltaP `28.0324` edge `1.2573` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9029` n `50` status `ready` deltaP `18.7622` edge `0.5205` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.3076` n `135` status `ready` deltaP `24.213` edge `0.5991` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.2911` n `135` status `ready` deltaP `23.6459` edge `0.682` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.5257` n `50` status `ready` deltaP `13.4451` edge `0.3335` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9986` n `50` status `ready` deltaP `15.497` edge `0.1916` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8825` n `50` status `ready` deltaP `32.3841` edge `0.0378` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8505` n `135` status `ready` deltaP `26.9329` edge `0.1058` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7299` n `135` status `ready` deltaP `21.5393` edge `0.2113` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6362` n `50` status `ready` deltaP `13.4551` edge `0.1963` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3295` n `135` status `ready` deltaP `26.1224` edge `0.1801` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.41` n `50` status `ready` deltaP `19.8922` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7773` n `135` status `ready` deltaP `8.8024` edge `0.0684` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5381` n `135` status `ready` deltaP `7.4551` edge `0.0862` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4658` n `135` status `ready` deltaP `8.6682` edge `0.0098` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.006` n `50` status `ready` deltaP `9.3473` edge `-0.0069` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0094` n `50` status `ready` deltaP `0.8024` edge `0.0585` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `-0.102` n `135` status `ready` deltaP `7.1488` edge `0.2098` maxDD `-15.9436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
