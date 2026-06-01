# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T09:52:21.235092+00:00`
- Price records: `672`
- Market context records: `2550`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->unknown_24h` score `5.6246` n `118` status `ready` deltaP `19.4768` edge `0.3717` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.5771` n `149` status `ready` deltaP `24.0987` edge `0.572` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.0233` n `118` status `ready` deltaP `12.1704` edge `0.6028` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.8975` n `149` status `ready` deltaP `17.1438` edge `0.3915` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9299` n `149` status `ready` deltaP `10.9193` edge `0.193` maxDD `-3.7312`
- `market_context_high->equity_24h` score `1.2588` n `118` status `ready` deltaP `18.9972` edge `0.0366` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.1593` n `149` status `ready` deltaP `9.4271` edge `0.1525` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.8912` n `118` status `ready` deltaP `8.0008` edge `0.119` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.6322` n `149` status `ready` deltaP `7.7854` edge `0.1202` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1986` n `118` status `ready` deltaP `-0.9592` edge `0.6723` maxDD `-39.2351`
- `market_context_high->index_4h` score `-0.1136` n `149` status `ready` deltaP `5.9226` edge `0.0352` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1849` n `149` status `ready` deltaP `2.8654` edge `0.0345` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.2148` n `149` status `ready` deltaP `3.1498` edge `0.0105` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4605` n `149` status `ready` deltaP `0.862` edge `0.01` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.5537` n `149` status `ready` deltaP `0.4853` edge `0.0041` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.5841` n `149` status `ready` deltaP `3.7586` edge `0.0141` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.7181` n `118` status `ready` deltaP `1.6037` edge `0.0049` maxDD `-1.946`
- `market_context_high->equity_1h` score `-0.8501` n `149` status `ready` deltaP `-0.7475` edge `0.018` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8734` n `149` status `ready` deltaP `3.5348` edge `0.0424` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.9073` n `149` status `ready` deltaP `-0.3059` edge `0.0124` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
