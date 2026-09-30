# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T15:52:34.310831+00:00`
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

- `market_context_high->unknown_1h` score `308.2599` n `50` status `ready` deltaP `7.7305` edge `25.6417` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.8617` n `50` status `ready` deltaP `8.2317` edge `23.4336` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0115` n `135` status `ready` deltaP `26.9907` edge `1.1753` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.7219` n `50` status `ready` deltaP `18.0` edge `0.5105` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.4421` n `135` status `ready` deltaP `24.5602` edge `0.608` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.0979` n `135` status `ready` deltaP `23.6459` edge `0.6659` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.4283` n `50` status `ready` deltaP `13.2927` edge `0.3264` maxDD `-7.6792`
- `news_risk_high->index_24h` score `3.1085` n `135` status `ready` deltaP `29.3634` edge `0.1111` maxDD `-0.4916`
- `market_context_high->crypto_major_1h` score `3.0429` n `50` status `ready` deltaP `15.7964` edge `0.1933` maxDD `-2.2692`
- `market_context_high->fx_4h` score `3.0104` n `50` status `ready` deltaP `33.9085` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.7493` n `135` status `ready` deltaP `21.8866` edge `0.2106` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6674` n `50` status `ready` deltaP `13.6048` edge `0.1979` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.2935` n `135` status `ready` deltaP `26.1224` edge `0.1771` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.398` n `50` status `ready` deltaP `19.7425` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8216` n `135` status `ready` deltaP `9.2515` edge `0.0691` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5692` n `135` status `ready` deltaP `7.6048` edge `0.0878` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3867` n `135` status `ready` deltaP `7.77` edge `0.0092` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0194` n `50` status `ready` deltaP `1.2515` edge `0.0592` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0719` n `50` status `ready` deltaP `8.1497` edge `-0.0089` maxDD `-2.3717`
- `market_context_high->metal_1h` score `-0.1778` n `50` status `ready` deltaP `2.6946` edge `0.0095` maxDD `-0.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
