# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T20:07:32.966040+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6928`

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

- `market_context_high->unknown_24h` score `1590.1762` n `134` status `ready` deltaP `-5.9158` edge `132.5971` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `116.7001` n `74` status `ready` deltaP `-0.785` edge `9.7428` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `36.3768` n `134` status `ready` deltaP `0.5688` edge `3.0409` maxDD `-0.3966`
- `market_context_high->equity_24h` score `5.6465` n `134` status `ready` deltaP `16.6589` edge `0.6352` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.6044` n `62` status `ready` deltaP `20.9038` edge `0.3913` maxDD `-3.4234`
- `market_context_high->index_24h` score `3.6166` n `134` status `ready` deltaP `35.2638` edge `0.0846` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `0.8847` n `62` status `ready` deltaP `7.8875` edge `0.0549` maxDD `-0.7008`
- `news_risk_high->crypto_alt_1h` score `0.4192` n `74` status `ready` deltaP `4.491` edge `0.0879` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.4023` n `134` status `ready` deltaP `16.1358` edge `0.0336` maxDD `-1.8344`
- `market_context_high->metal_1h` score `0.3899` n `134` status `ready` deltaP `10.9036` edge `0.0152` maxDD `-0.3659`
- `market_context_high->equity_1h` score `0.3325` n `134` status `ready` deltaP `5.3803` edge `0.0794` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2961` n `134` status `ready` deltaP `14.2428` edge `0.0516` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.2209` n `134` status `ready` deltaP `3.4583` edge `0.1637` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0564` n `134` status `ready` deltaP `7.4649` edge `0.0577` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1104` n `134` status `ready` deltaP `3.4297` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2613` n `134` status `ready` deltaP `2.2433` edge `0.0147` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5061` n `134` status `ready` deltaP `-0.3208` edge `-0.0029` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.5486` n `74` status `ready` deltaP `-3.9084` edge `0.0098` maxDD `-0.9927`
- `market_context_high->index_1h` score `-0.7899` n `134` status `ready` deltaP `-1.6467` edge `0.001` maxDD `-1.1344`
- `news_risk_high->fx_1h` score `-0.847` n `74` status `ready` deltaP `-5.102` edge `-0.0045` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
