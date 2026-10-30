# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T13:52:27.868918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7038`

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

- `market_context_high->unknown_24h` score `1615.373` n `134` status `ready` deltaP `-2.7908` edge `134.676` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `214.4284` n `49` status `ready` deltaP `-1.4114` edge `17.891` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.1018` n `134` status `ready` deltaP `1.9407` edge `2.6755` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `9.086` n `37` status `ready` deltaP `28.8357` edge `0.5996` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.3831` n `134` status `ready` deltaP `35.0902` edge `0.0663` maxDD `-0.1315`
- `market_context_high->equity_24h` score `3.0305` n `134` status `ready` deltaP `16.6589` edge `0.4172` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `0.7316` n `49` status `ready` deltaP `7.7019` edge `0.0905` maxDD `-2.1776`
- `market_context_high->metal_1h` score `0.3836` n `134` status `ready` deltaP `10.9036` edge `0.0144` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3348` n `134` status `ready` deltaP `15.6785` edge `0.028` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1826` n `134` status `ready` deltaP `4.7815` edge `0.0709` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.1651` n `134` status `ready` deltaP `13.1757` edge `0.0478` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0996` n `134` status `ready` deltaP `7.6146` edge `0.0603` maxDD `-5.2213`
- `news_risk_high->commodity_4h` score `0.0587` n `37` status `ready` deltaP `-2.0724` edge `0.0551` maxDD `-0.7008`
- `market_context_high->fx_1h` score `-0.0691` n `134` status `ready` deltaP `4.1782` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1432` n `134` status `ready` deltaP `2.6961` edge `0.1221` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3068` n `134` status `ready` deltaP `1.7942` edge `0.0139` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.3182` n `49` status `ready` deltaP `4.7477` edge `-0.0031` maxDD `-0.5475`
- `market_context_high->fx_4h` score `-0.5203` n `134` status `ready` deltaP `-0.4732` edge `-0.0037` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8306` n `134` status `ready` deltaP `3.1482` edge `0.059` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.863` n `134` status `ready` deltaP `-2.3952` edge `-0.0001` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
