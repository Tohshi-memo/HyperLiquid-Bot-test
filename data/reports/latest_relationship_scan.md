# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T10:37:29.838687+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7058`

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

- `market_context_high->unknown_24h` score `1783.8974` n `134` status `ready` deltaP `-2.7908` edge `148.7197` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `259.6507` n `36` status `ready` deltaP `-3.7924` edge `21.6754` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.5125` n `134` status `ready` deltaP `3.77` edge `2.8642` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.1218` n `134` status `ready` deltaP `33.3541` edge `0.0561` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.9612` n `134` status `ready` deltaP `16.3117` edge `0.3304` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `1.866` n `36` status `ready` deltaP `12.6746` edge `0.1127` maxDD `-1.669`
- `news_risk_high->index_1h` score `0.6836` n `36` status `ready` deltaP `16.7498` edge `0.0007` maxDD `-0.3117`
- `market_context_high->metal_1h` score `0.3501` n `134` status `ready` deltaP `10.4545` edge `0.0131` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2909` n `134` status `ready` deltaP `15.3736` edge `0.0244` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1165` n `134` status `ready` deltaP `12.7184` edge `0.0468` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.0963` n `134` status `ready` deltaP `4.1827` edge `0.0677` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0023` n `134` status `ready` deltaP `6.8661` edge `0.0568` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1135` n `134` status `ready` deltaP `3.4297` edge `-0.0016` maxDD `-0.1986`
- `news_risk_high->commodity_1h` score `-0.2687` n `36` status `ready` deltaP `-4.9568` edge `0.0288` maxDD `-0.4158`
- `market_context_high->commodity_1h` score `-0.3571` n `134` status `ready` deltaP `1.3451` edge `0.0127` maxDD `-0.4475`
- `news_risk_high->fx_1h` score `-0.4447` n `36` status `ready` deltaP `-1.0479` edge `0.0014` maxDD `-0.1142`
- `market_context_high->equity_4h` score `-0.4552` n `134` status `ready` deltaP `0.8668` edge `0.0943` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.6176` n `134` status `ready` deltaP `-2.15` edge `-0.005` maxDD `-0.4545`
- `news_risk_high->metal_1h` score `-0.833` n `36` status `ready` deltaP `-6.0878` edge `-0.0125` maxDD `-0.9639`
- `market_context_high->crypto_alt_1h` score `-0.8469` n `134` status `ready` deltaP `2.8488` edge `0.0589` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
