# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T02:37:21.877724+00:00`
- Price records: `672`
- Market context records: `2621`
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

- `market_context_high->unknown_24h` score `7.7106` n `146` status `ready` deltaP `18.2958` edge `0.5534` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0405` n `146` status `ready` deltaP `24.8914` edge `0.522` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.2333` n `146` status `ready` deltaP `14.0014` edge `0.3571` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.3832` n `146` status `ready` deltaP `11.5803` edge `0.1568` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0783` n `146` status `ready` deltaP `7.6846` edge `0.1436` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.9762` n `146` status `ready` deltaP `9.8435` edge `0.1138` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.7532` n `146` status `ready` deltaP `9.0128` edge `0.1221` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.5092` n `146` status `ready` deltaP `2.0643` edge `0.6665` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2384` n `146` status `ready` deltaP `8.8227` edge `0.0452` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.082` n `146` status `ready` deltaP `4.3905` edge `0.0133` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3044` n `146` status `ready` deltaP `6.2505` edge `0.0208` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.3888` n `146` status `ready` deltaP `1.6508` edge `0.0229` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.6464` n `146` status `ready` deltaP `1.2612` edge `0.0125` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7036` n `146` status `ready` deltaP `-1.2837` edge `0.0034` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8025` n `146` status `ready` deltaP `-0.3773` edge `0.0195` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-0.9184` n `146` status `ready` deltaP `4.8634` edge `0.0441` maxDD `-10.2078`
- `market_context_high->metal_4h` score `-0.9596` n `146` status `ready` deltaP `3.2826` edge `0.0369` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.9764` n `146` status `ready` deltaP `3.1939` edge `-0.0033` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.9993` n `146` status `ready` deltaP `-1.1402` edge `0.0101` maxDD `-0.8621`
- `market_context_high->equity_4h` score `-1.3662` n `146` status `ready` deltaP `1.6497` edge `0.0156` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
