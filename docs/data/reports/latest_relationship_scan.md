# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T14:07:25.788881+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7026`

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

- `market_context_high->unknown_24h` score `1618.931` n `134` status `ready` deltaP `-2.7908` edge `134.9725` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `205.93` n `50` status `ready` deltaP `-1.1257` edge `17.1809` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.0308` n `134` status `ready` deltaP `1.7883` edge `2.6706` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `8.7722` n `38` status `ready` deltaP `26.7731` edge `0.5872` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.4066` n `134` status `ready` deltaP `35.2638` edge `0.0671` maxDD `-0.1315`
- `market_context_high->equity_24h` score `3.1205` n `134` status `ready` deltaP `16.6589` edge `0.4247` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `0.5977` n `50` status `ready` deltaP `6.7904` edge `0.0836` maxDD `-2.5122`
- `market_context_high->metal_1h` score `0.3836` n `134` status `ready` deltaP `10.9036` edge `0.0144` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3387` n `134` status `ready` deltaP `15.6785` edge `0.0285` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1898` n `134` status `ready` deltaP `4.7815` edge `0.0715` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.1663` n `134` status `ready` deltaP `13.1757` edge `0.0479` maxDD `-1.0837`
- `news_risk_high->commodity_4h` score `0.1256` n `38` status `ready` deltaP `-0.6499` edge `0.0542` maxDD `-0.7008`
- `market_context_high->crypto_major_1h` score `0.1199` n `134` status `ready` deltaP `7.7643` edge `0.061` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0598` n `134` status `ready` deltaP `4.3279` edge `-0.0007` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1267` n `134` status `ready` deltaP `2.8486` edge `0.1232` maxDD `-6.008`
- `news_risk_high->index_1h` score `-0.2689` n `50` status `ready` deltaP `5.6048` edge `-0.0025` maxDD `-0.5475`
- `market_context_high->commodity_1h` score `-0.3248` n `134` status `ready` deltaP `1.6445` edge `0.0134` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.51` n `134` status `ready` deltaP `-0.3208` edge `-0.0034` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8173` n `134` status `ready` deltaP `3.2979` edge `0.0597` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8606` n `134` status `ready` deltaP `-2.3952` edge `0.0001` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
