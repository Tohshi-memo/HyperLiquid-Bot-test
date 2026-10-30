# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T15:07:27.461289+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7030`

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

- `market_context_high->unknown_24h` score `1613.6561` n `134` status `ready` deltaP `-3.3116` edge `134.5364` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `173.9394` n `54` status `ready` deltaP `-0.2384` edge `14.5091` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.897` n `134` status `ready` deltaP `1.331` edge `2.6625` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.605` n `42` status `ready` deltaP `22.0384` edge `0.5265` maxDD `-1.5072`
- `market_context_high->equity_24h` score `3.5009` n `134` status `ready` deltaP `16.6589` edge `0.4564` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.439` n `134` status `ready` deltaP `35.2638` edge `0.0698` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.8242` n `54` status `ready` deltaP `6.4926` edge `0.0965` maxDD `-3.3547`
- `market_context_high->metal_1h` score `0.4039` n `134` status `ready` deltaP `11.203` edge `0.015` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3702` n `134` status `ready` deltaP `15.9834` edge `0.0305` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2797` n `134` status `ready` deltaP `5.2306` edge `0.076` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.1869` n `134` status `ready` deltaP `13.3281` edge `0.0486` maxDD `-1.0837`
- `news_risk_high->commodity_4h` score `0.1403` n `42` status `ready` deltaP `-0.2469` edge `0.0471` maxDD `-0.7008`
- `market_context_high->crypto_major_1h` score `0.0972` n `134` status `ready` deltaP `7.6146` edge `0.0601` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0507` n `134` status `ready` deltaP `3.3059` edge `0.1299` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0676` n `134` status `ready` deltaP `4.1782` edge `-0.0007` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3583` n `134` status `ready` deltaP `1.3451` edge `0.0126` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.3956` n `54` status `ready` deltaP `3.4598` edge `-0.0039` maxDD `-0.5909`
- `market_context_high->fx_4h` score `-0.5053` n `134` status `ready` deltaP `-0.3208` edge `-0.0028` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.8294` n `134` status `ready` deltaP `-2.0958` edge `0.0007` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8399` n `134` status `ready` deltaP `3.1482` edge `0.0578` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
