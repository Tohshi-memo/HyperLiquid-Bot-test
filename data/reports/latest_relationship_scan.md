# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T16:52:41.526706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6926`

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

- `market_context_high->unknown_1h` score `308.2419` n `50` status `ready` deltaP `7.5808` edge `25.6412` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.8677` n `50` status `ready` deltaP `8.2317` edge `23.4341` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.1591` n `135` status `ready` deltaP `26.9907` edge `1.1876` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.7085` n `50` status `ready` deltaP `17.8476` edge `0.5104` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.3766` n `135` status `ready` deltaP `24.3866` edge `0.6037` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.1075` n `135` status `ready` deltaP `23.6459` edge `0.6667` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.3463` n `50` status `ready` deltaP `12.9878` edge `0.3216` maxDD `-7.6792`
- `news_risk_high->index_24h` score `3.0302` n `135` status `ready` deltaP `28.669` edge `0.1092` maxDD `-0.4916`
- `market_context_high->fx_4h` score `2.997` n `50` status `ready` deltaP `33.7561` edge `0.0382` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.947` n `50` status `ready` deltaP `15.3473` edge `0.1883` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.7143` n `135` status `ready` deltaP `21.5393` edge `0.21` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.5894` n `50` status `ready` deltaP `13.3054` edge `0.1934` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.256` n `135` status `ready` deltaP `25.8175` edge `0.176` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7845` n `135` status `ready` deltaP `8.9521` edge `0.068` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.4913` n `135` status `ready` deltaP `7.3054` edge `0.0833` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3723` n `135` status `ready` deltaP `7.6203` edge `0.009` maxDD `-0.302`
- `market_context_high->equity_1h` score `-0.0047` n `50` status `ready` deltaP `0.9521` edge `0.0581` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0734` n `50` status `ready` deltaP `8.1497` edge `-0.0091` maxDD `-2.3717`
- `market_context_high->metal_1h` score `-0.2054` n `50` status `ready` deltaP `2.3952` edge `0.0092` maxDD `-0.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
