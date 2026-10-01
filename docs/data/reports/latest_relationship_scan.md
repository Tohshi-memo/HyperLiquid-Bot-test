# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T00:12:43.899225+00:00`
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

- `market_context_high->unknown_1h` score `317.9573` n `50` status `ready` deltaP `6.5329` edge `26.4578` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.007` n `50` status `ready` deltaP `6.7073` edge `23.2892` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.269` n `135` status `ready` deltaP `28.9004` edge `1.3507` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8533` n `50` status `ready` deltaP `18.4573` edge `0.5184` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3811` n `135` status `ready` deltaP `23.6459` edge `0.6895` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3352` n `135` status `ready` deltaP `24.213` edge `0.6014` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.8103` n `50` status `ready` deltaP `14.5122` edge `0.3501` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0142` n `50` status `ready` deltaP `15.497` edge `0.1929` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8715` n `50` status `ready` deltaP `32.2317` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8265` n `135` status `ready` deltaP `26.9329` edge `0.1038` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7671` n `135` status `ready` deltaP `21.5393` edge `0.2144` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6194` n `50` status `ready` deltaP `13.3054` edge `0.1959` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.228` n `135` status `ready` deltaP `25.5126` edge `0.1757` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3729` n `50` status `ready` deltaP `19.4431` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7042` n `135` status `ready` deltaP `8.0539` edge `0.0673` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5213` n `135` status `ready` deltaP `7.3054` edge `0.0858` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3999` n `135` status `ready` deltaP `7.9197` edge `0.0093` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.1825` n `135` status `ready` deltaP `8.2159` edge `0.2264` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `-0.0057` n `50` status `ready` deltaP `9.1976` edge `-0.0074` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0569` n `50` status `ready` deltaP `0.0539` edge `0.0574` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
