# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T10:07:30.786159+00:00`
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

- `market_context_high->unknown_24h` score `1777.0586` n `134` status `ready` deltaP `-2.7908` edge `148.1498` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `288.5632` n `34` status `ready` deltaP `-1.9813` edge `24.0727` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.6833` n `134` status `ready` deltaP `4.0749` edge `2.8764` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.1038` n `134` status `ready` deltaP `33.3541` edge `0.0546` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.8448` n `134` status `ready` deltaP `16.3117` edge `0.3207` maxDD `-14.0571`
- `news_risk_high->index_1h` score `0.9799` n `34` status `ready` deltaP `20.6851` edge `0.0031` maxDD `-0.2301`
- `news_risk_high->crypto_alt_1h` score `0.924` n `34` status `ready` deltaP `10.5231` edge `0.09` maxDD `-1.669`
- `market_context_high->metal_1h` score `0.3299` n `134` status `ready` deltaP `10.1551` edge `0.0125` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2901` n `134` status `ready` deltaP `15.3736` edge `0.0243` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1395` n `134` status `ready` deltaP `12.8708` edge `0.0477` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.0963` n `134` status `ready` deltaP `4.1827` edge `0.0677` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.0265` n `134` status `ready` deltaP `7.0158` edge `0.0582` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1135` n `134` status `ready` deltaP `3.4297` edge `-0.0016` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3284` n `134` status `ready` deltaP `1.6445` edge `0.0131` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.4495` n `34` status `ready` deltaP `-7.9253` edge `0.0254` maxDD `-0.4158`
- `market_context_high->equity_4h` score `-0.4676` n `134` status `ready` deltaP `0.8668` edge `0.0927` maxDD `-6.008`
- `news_risk_high->fx_1h` score `-0.6` n `34` status `ready` deltaP `-3.9891` edge `0.0011` maxDD `-0.1142`
- `market_context_high->fx_4h` score `-0.6168` n `134` status `ready` deltaP `-2.15` edge `-0.0049` maxDD `-0.4545`
- `news_risk_high->metal_1h` score `-0.6868` n `34` status `ready` deltaP `-3.9363` edge `-0.0081` maxDD `-0.9639`
- `market_context_high->crypto_alt_1h` score `-0.8142` n `134` status `ready` deltaP `3.1482` edge `0.0611` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
