# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T14:52:38.973876+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7438`

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

- `market_context_high->unknown_1h` score `308.3283` n `50` status `ready` deltaP `7.8802` edge `25.6464` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.5677` n `50` status `ready` deltaP `8.2317` edge `23.4091` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.8553` n `135` status `ready` deltaP `26.6435` edge `1.1646` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.7375` n `50` status `ready` deltaP `18.0` edge `0.5118` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.5465` n `135` status `ready` deltaP `24.5602` edge `0.6167` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.1154` n `135` status `ready` deltaP `23.8195` edge `0.6662` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.5259` n `50` status `ready` deltaP `13.5976` edge `0.3325` maxDD `-7.6792`
- `news_risk_high->index_24h` score `3.2001` n `135` status `ready` deltaP `30.0579` edge `0.1141` maxDD `-0.4916`
- `market_context_high->crypto_major_1h` score `3.1065` n `50` status `ready` deltaP `16.0958` edge `0.1966` maxDD `-2.2692`
- `market_context_high->fx_4h` score `3.0238` n `50` status `ready` deltaP `34.061` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.7824` n `135` status `ready` deltaP `22.0602` edge `0.2122` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.7118` n `50` status `ready` deltaP `13.7545` edge `0.2006` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3807` n `135` status `ready` deltaP `26.7321` edge `0.1803` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4376` n `50` status `ready` deltaP `20.1916` edge `0.0116` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8396` n `135` status `ready` deltaP `9.4012` edge `0.0696` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.6136` n `135` status `ready` deltaP `7.7545` edge `0.0905` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3999` n `135` status `ready` deltaP `7.9197` edge `0.0093` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0311` n `50` status `ready` deltaP `1.4012` edge `0.0597` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0508` n `50` status `ready` deltaP `8.4491` edge `-0.0082` maxDD `-2.3717`
- `news_risk_high->crypto_alt_4h` score `-0.1018` n `135` status `ready` deltaP `7.3013` edge `0.2088` maxDD `-15.9436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
