# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T15:07:42.012348+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->unknown_1h` score `308.2863` n `50` status `ready` deltaP `7.8802` edge `25.6429` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.4837` n `50` status `ready` deltaP `8.2317` edge `23.4021` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.8884` n `135` status `ready` deltaP `26.8171` edge `1.1662` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.7255` n `50` status `ready` deltaP `18.0` edge `0.5108` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.5225` n `135` status `ready` deltaP `24.5602` edge `0.6147` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.1082` n `135` status `ready` deltaP `23.8195` edge `0.6656` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.4789` n `50` status `ready` deltaP `13.4451` edge `0.3296` maxDD `-7.6792`
- `news_risk_high->index_24h` score `3.1778` n `135` status `ready` deltaP `29.8843` edge `0.1134` maxDD `-0.4916`
- `market_context_high->crypto_major_1h` score `3.1077` n `50` status `ready` deltaP `16.0958` edge `0.1967` maxDD `-2.2692`
- `market_context_high->fx_4h` score `3.0238` n `50` status `ready` deltaP `34.061` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.7764` n `135` status `ready` deltaP `22.0602` edge `0.2117` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.7046` n `50` status `ready` deltaP `13.7545` edge `0.2` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3589` n `135` status `ready` deltaP `26.5797` edge `0.1795` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4244` n `50` status `ready` deltaP `20.0419` edge `0.0115` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8396` n `135` status `ready` deltaP `9.4012` edge `0.0696` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.6064` n `135` status `ready` deltaP `7.7545` edge `0.0899` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3999` n `135` status `ready` deltaP `7.9197` edge `0.0093` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0311` n `50` status `ready` deltaP `1.4012` edge `0.0597` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0508` n `50` status `ready` deltaP `8.4491` edge `-0.0082` maxDD `-2.3717`
- `news_risk_high->crypto_alt_4h` score `-0.1488` n `135` status `ready` deltaP `7.1488` edge `0.2059` maxDD `-15.9436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
