# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T17:37:34.388287+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6942`

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

- `market_context_high->unknown_1h` score `308.3031` n `50` status `ready` deltaP `7.5808` edge `25.6463` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.6529` n `50` status `ready` deltaP `8.2317` edge `23.4162` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.2491` n `135` status `ready` deltaP `26.9907` edge `1.1951` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.7737` n `50` status `ready` deltaP `18.1524` edge `0.5138` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.3694` n `135` status `ready` deltaP `24.3866` edge `0.6031` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.1027` n `135` status `ready` deltaP `23.6459` edge `0.6663` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.3559` n `50` status `ready` deltaP `12.9878` edge `0.3224` maxDD `-7.6792`
- `news_risk_high->index_24h` score `2.9916` n `135` status `ready` deltaP `28.3218` edge `0.1083` maxDD `-0.4916`
- `market_context_high->fx_4h` score `2.958` n `50` status `ready` deltaP `33.2988` edge `0.038` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9314` n `50` status `ready` deltaP `15.1976` edge `0.188` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.7107` n `135` status `ready` deltaP `21.5393` edge `0.2097` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6026` n `50` status `ready` deltaP `13.4551` edge `0.1935` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.2945` n `135` status `ready` deltaP `25.9699` edge `0.1782` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8252` n `135` status `ready` deltaP `9.2515` edge `0.0694` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5045` n `135` status `ready` deltaP `7.4551` edge `0.0834` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4131` n `135` status `ready` deltaP `8.0694` edge `0.0094` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0218` n `50` status `ready` deltaP `1.2515` edge `0.0595` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0438` n `50` status `ready` deltaP `8.5988` edge `-0.0083` maxDD `-2.3717`
- `market_context_high->metal_1h` score `-0.1754` n `50` status `ready` deltaP `2.6946` edge `0.0097` maxDD `-0.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
