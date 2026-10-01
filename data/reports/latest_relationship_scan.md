# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T03:07:40.609625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6730`

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

- `market_context_high->unknown_1h` score `318.4528` n `50` status `ready` deltaP `6.6826` edge `26.4981` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.5554` n `50` status `ready` deltaP `6.7073` edge `23.3349` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.006` n `135` status `ready` deltaP `29.2477` edge `1.4098` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9547` n `50` status `ready` deltaP `18.9146` edge `0.5238` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4831` n `135` status `ready` deltaP `23.6459` edge `0.698` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.4339` n `135` status `ready` deltaP `24.9074` edge `0.605` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.9929` n `50` status `ready` deltaP `14.6646` edge `0.3643` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.019` n `50` status `ready` deltaP `15.6467` edge `0.1923` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8309` n `135` status `ready` deltaP `21.8866` edge `0.2174` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.8279` n `50` status `ready` deltaP `31.9268` edge `0.0363` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.7192` n `135` status `ready` deltaP `25.8912` edge `0.1018` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.665` n `50` status `ready` deltaP `13.3054` edge `0.1997` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `1.9728` n `135` status `ready` deltaP `23.9882` edge `0.1646` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3801` n `50` status `ready` deltaP `19.5928` edge `0.0108` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.5927` n `135` status `ready` deltaP `7.1557` edge `0.064` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5669` n `135` status `ready` deltaP `7.3054` edge `0.0896` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.3651` n `135` status `ready` deltaP `8.3683` edge `0.2406` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.3304` n `135` status `ready` deltaP `7.1712` edge `0.0085` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0036` n `50` status `ready` deltaP `8.8982` edge `-0.0065` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1293` n `50` status `ready` deltaP `-0.8443` edge `0.0541` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
