# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T01:22:29.747655+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6620`

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

- `market_context_high->unknown_1h` score `318.2789` n `50` status `ready` deltaP `6.5329` edge `26.4846` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.4402` n `50` status `ready` deltaP `6.7073` edge `23.3253` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.5894` n `135` status `ready` deltaP `28.9004` edge `1.3774` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8363` n `50` status `ready` deltaP `18.3049` edge `0.518` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4015` n `135` status `ready` deltaP `23.6459` edge `0.6912` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3778` n `135` status `ready` deltaP `24.3866` edge `0.6038` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.8799` n `50` status `ready` deltaP `14.5122` edge `0.3559` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9818` n `50` status `ready` deltaP `15.3473` edge `0.1912` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8387` n `50` status `ready` deltaP `31.9268` edge `0.0372` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.7887` n `135` status `ready` deltaP `21.5393` edge `0.2162` maxDD `-2.192`
- `news_risk_high->index_24h` score `2.7776` n `135` status `ready` deltaP `26.412` edge `0.1032` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6134` n `50` status `ready` deltaP `13.3054` edge `0.1954` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.1554` n `135` status `ready` deltaP `25.0553` edge `0.1727` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3417` n `50` status `ready` deltaP `19.1437` edge `0.0106` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.6886` n `135` status `ready` deltaP `7.9042` edge `0.067` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5153` n `135` status `ready` deltaP `7.3054` edge `0.0853` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3987` n `135` status `ready` deltaP `7.9197` edge `0.0092` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.2521` n `135` status `ready` deltaP `8.2159` edge `0.2322` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `0.03` n `50` status `ready` deltaP `9.3473` edge `-0.0061` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.067` n `50` status `ready` deltaP `-0.0958` edge `0.0571` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
