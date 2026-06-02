# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T01:52:20.143842+00:00`
- Price records: `672`
- Market context records: `2618`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.8258` n `146` status `ready` deltaP `18.2958` edge `0.563` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0825` n `146` status `ready` deltaP `24.8914` edge `0.5255` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.2875` n `146` status `ready` deltaP `14.1539` edge `0.3606` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.412` n `146` status `ready` deltaP `11.73` edge `0.1582` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0987` n `146` status `ready` deltaP `7.6846` edge `0.1453` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.8872` n `146` status `ready` deltaP `9.4963` edge `0.1087` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.7892` n `146` status `ready` deltaP `9.1625` edge `0.1241` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.5164` n `146` status `ready` deltaP `2.0643` edge `0.6671` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2192` n `146` status `ready` deltaP `8.8227` edge `0.0436` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0808` n `146` status `ready` deltaP `4.3905` edge `0.0134` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3308` n `146` status `ready` deltaP `6.1008` edge `0.0196` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4644` n `146` status `ready` deltaP `1.8005` edge `0.0156` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.6512` n `146` status `ready` deltaP `1.2612` edge `0.0121` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6653` n `146` status `ready` deltaP `-0.8346` edge `0.0036` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7749` n `146` status `ready` deltaP `-0.2276` edge `0.0208` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.9076` n `146` status `ready` deltaP `3.5875` edge `0.0392` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.9427` n `146` status `ready` deltaP `3.5411` edge `-0.0028` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.9567` n `146` status `ready` deltaP `-0.6828` edge `0.0106` maxDD `-0.8621`
- `market_context_high->commodity_4h` score `-0.9656` n `146` status `ready` deltaP `4.4061` edge `0.0411` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.3794` n `146` status `ready` deltaP `1.6497` edge `0.0145` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
