# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T01:37:19.483978+00:00`
- Price records: `672`
- Market context records: `2617`
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

- `market_context_high->unknown_24h` score `7.869` n `146` status `ready` deltaP `18.2958` edge `0.5666` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0981` n `146` status `ready` deltaP `24.8914` edge `0.5268` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.3043` n `146` status `ready` deltaP `14.1539` edge `0.362` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.4036` n `146` status `ready` deltaP `11.73` edge `0.1575` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.1241` n `146` status `ready` deltaP `7.837` edge `0.1464` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.8457` n `146` status `ready` deltaP `9.3227` edge `0.1064` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.782` n `146` status `ready` deltaP `9.1625` edge `0.1235` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.5248` n `146` status `ready` deltaP `2.0643` edge `0.6678` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.212` n `146` status `ready` deltaP `8.8227` edge `0.043` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0808` n `146` status `ready` deltaP `4.3905` edge `0.0134` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3499` n `146` status `ready` deltaP `5.9511` edge `0.019` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4428` n `146` status `ready` deltaP `1.9502` edge `0.0164` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.644` n `146` status `ready` deltaP `1.2612` edge `0.0127` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6521` n `146` status `ready` deltaP `-0.6849` edge `0.0037` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7677` n `146` status `ready` deltaP `-0.2276` edge `0.0214` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8992` n `146` status `ready` deltaP `3.5875` edge `0.0399` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.9264` n `146` status `ready` deltaP `3.7148` edge `-0.0026` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.9409` n `146` status `ready` deltaP `-0.5304` edge `0.0109` maxDD `-0.8621`
- `market_context_high->commodity_4h` score `-0.9821` n `146` status `ready` deltaP `4.2536` edge `0.04` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.3854` n `146` status `ready` deltaP `1.6497` edge `0.014` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
