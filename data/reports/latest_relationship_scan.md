# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T08:37:24.191446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6595`

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

- `market_context_high->unknown_24h` score `1756.4342` n `134` status `ready` deltaP `-2.7908` edge `146.4311` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `34.7781` n `134` status `ready` deltaP `4.0749` edge `2.8843` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.063` n `134` status `ready` deltaP `33.3541` edge `0.0512` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.57` n `134` status `ready` deltaP `16.3117` edge `0.2978` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3517` n `134` status `ready` deltaP `10.4545` edge `0.0133` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2539` n `134` status `ready` deltaP `14.9163` edge `0.0227` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.2183` n `134` status `ready` deltaP `13.4806` edge `0.0502` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.1466` n `134` status `ready` deltaP `4.4821` edge `0.0699` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.0061` n `134` status `ready` deltaP `6.8661` edge `0.0575` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0886` n `134` status `ready` deltaP `3.8788` edge `-0.0014` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3463` n `134` status `ready` deltaP `1.4948` edge `0.0126` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.452` n `134` status `ready` deltaP `0.8668` edge `0.0947` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.582` n `134` status `ready` deltaP `-1.5403` edge `-0.0045` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7908` n `134` status `ready` deltaP `3.4476` edge `0.0621` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8857` n `134` status `ready` deltaP `-2.6946` edge `0.0` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.3231` n `134` status `ready` deltaP `3.9257` edge `0.0689` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.8224` n `134` status `ready` deltaP `7.7039` edge `0.0445` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.89` n `134` status `ready` deltaP `-3.3193` edge `-0.0023` maxDD `-0.9792`
- `market_context_high->index_4h` score `-2.1229` n `134` status `ready` deltaP `-4.4526` edge `-0.0152` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.7538` n `134` status `ready` deltaP `8.5432` edge `0.0208` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
