# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T15:37:32.932797+00:00`
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

- `market_context_high->unknown_1h` score `308.2419` n `50` status `ready` deltaP `7.5808` edge `25.6412` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.7297` n `50` status `ready` deltaP `8.2317` edge `23.4226` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.9659` n `135` status `ready` deltaP `26.9907` edge `1.1715` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.7171` n `50` status `ready` deltaP `18.0` edge `0.5101` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.4625` n `135` status `ready` deltaP `24.5602` edge `0.6097` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.0931` n `135` status `ready` deltaP `23.6459` edge `0.6655` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.4441` n `50` status `ready` deltaP `13.4451` edge `0.3267` maxDD `-7.6792`
- `news_risk_high->index_24h` score `3.1308` n `135` status `ready` deltaP `29.537` edge `0.1118` maxDD `-0.4916`
- `market_context_high->crypto_major_1h` score `3.0717` n `50` status `ready` deltaP `15.9461` edge `0.1947` maxDD `-2.2692`
- `market_context_high->fx_4h` score `3.0104` n `50` status `ready` deltaP `33.9085` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.7517` n `135` status `ready` deltaP `21.8866` edge `0.2108` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.671` n `50` status `ready` deltaP `13.6048` edge `0.1982` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3141` n `135` status `ready` deltaP `26.2748` edge `0.1778` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4112` n `50` status `ready` deltaP `19.8922` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8228` n `135` status `ready` deltaP `9.2515` edge `0.0692` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5728` n `135` status `ready` deltaP `7.6048` edge `0.0881` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3867` n `135` status `ready` deltaP `7.77` edge `0.0092` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0202` n `50` status `ready` deltaP `1.2515` edge `0.0593` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0618` n `50` status `ready` deltaP `8.2994` edge `-0.0086` maxDD `-2.3717`
- `market_context_high->metal_1h` score `-0.1802` n `50` status `ready` deltaP `2.6946` edge `0.0093` maxDD `-0.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
