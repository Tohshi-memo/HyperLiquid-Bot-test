# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T15:22:35.211271+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6916`

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

- `market_context_high->unknown_1h` score `308.2587` n `50` status `ready` deltaP `7.7305` edge `25.6416` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.5533` n `50` status `ready` deltaP `8.2317` edge `23.4079` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.9227` n `135` status `ready` deltaP `26.9907` edge `1.1679` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.7159` n `50` status `ready` deltaP `18.0` edge `0.51` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.4913` n `135` status `ready` deltaP `24.5602` edge `0.6121` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.0847` n `135` status `ready` deltaP `23.6459` edge `0.6648` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.4537` n `50` status `ready` deltaP `13.4451` edge `0.3275` maxDD `-7.6792`
- `news_risk_high->index_24h` score `3.1531` n `135` status `ready` deltaP `29.7106` edge `0.1125` maxDD `-0.4916`
- `market_context_high->crypto_major_1h` score `3.0933` n `50` status `ready` deltaP `16.0958` edge `0.1955` maxDD `-2.2692`
- `market_context_high->fx_4h` score `3.0116` n `50` status `ready` deltaP `33.9085` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.7565` n `135` status `ready` deltaP `21.8866` edge `0.2112` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.689` n `50` status `ready` deltaP `13.7545` edge `0.1987` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3347` n `135` status `ready` deltaP `26.4272` edge `0.1785` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4244` n `50` status `ready` deltaP `20.0419` edge `0.0115` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8384` n `135` status `ready` deltaP `9.4012` edge `0.0695` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5908` n `135` status `ready` deltaP `7.7545` edge `0.0886` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3999` n `135` status `ready` deltaP `7.9197` edge `0.0093` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0303` n `50` status `ready` deltaP `1.4012` edge `0.0596` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0524` n `50` status `ready` deltaP `8.4491` edge `-0.0084` maxDD `-2.3717`
- `news_risk_high->crypto_alt_4h` score `-0.174` n `135` status `ready` deltaP `7.1488` edge `0.2038` maxDD `-15.9436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
