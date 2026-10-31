# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T18:07:23.937241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7639`

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

- `market_context_high->unknown_24h` score `2854.4313` n `100` status `ready` deltaP `-9.1875` edge `237.9735` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `82.7003` n `100` status `ready` deltaP `0.9268` edge `6.8988` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.2013` n `108` status `ready` deltaP `-5.7939` edge `6.5007` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.7722` n `66` status `ready` deltaP `45.5808` edge `1.2656` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.0011` n `100` status `ready` deltaP `26.2153` edge `1.0177` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.0334` n `106` status `ready` deltaP `18.5832` edge `0.4342` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8847` n `100` status `ready` deltaP `43.5556` edge `0.135` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6863` n `100` status `ready` deltaP `20.8963` edge `0.0437` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8509` n `100` status `ready` deltaP `12.1976` edge `0.0186` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.7476` n `100` status `ready` deltaP `6.2378` edge `0.1936` maxDD `-4.48`
- `news_risk_high->crypto_alt_1h` score `0.703` n `108` status `ready` deltaP `8.1282` edge `0.0998` maxDD `-3.9659`
- `market_context_high->crypto_major_1h` score `0.5497` n `100` status `ready` deltaP `9.4012` edge `0.0859` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.5013` n `100` status `ready` deltaP `7.7006` edge `0.1005` maxDD `-2.3383`
- `market_context_high->fx_1h` score `0.2348` n `100` status `ready` deltaP `8.6048` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.2216` n `100` status `ready` deltaP `8.561` edge `0.0005` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.1718` n `100` status `ready` deltaP `12.7927` edge `0.0573` maxDD `-0.978`
- `market_context_high->metal_24h` score `0.0435` n `100` status `ready` deltaP `13.2847` edge `0.1817` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.1048` n `100` status `ready` deltaP `16.6463` edge `0.1496` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.2799` n `100` status `ready` deltaP `4.503` edge `0.0025` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.3511` n `100` status `ready` deltaP `-1.1078` edge `0.0138` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
