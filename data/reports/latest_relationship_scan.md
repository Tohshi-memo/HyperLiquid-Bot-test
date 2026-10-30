# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T13:22:28.755453+00:00`
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

- `market_context_high->unknown_24h` score `1751.645` n `134` status `ready` deltaP `-2.7908` edge `146.032` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `211.5117` n `47` status `ready` deltaP `-2.0193` edge `17.652` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.2006` n `134` status `ready` deltaP `2.2456` edge `2.6817` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `9.4844` n `35` status `ready` deltaP `30.3049` edge `0.623` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.3385` n `134` status `ready` deltaP `34.7429` edge `0.0649` maxDD `-0.1315`
- `market_context_high->equity_24h` score `2.8355` n `134` status `ready` deltaP `16.4853` edge `0.4021` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `1.6993` n `47` status `ready` deltaP `9.8101` edge `0.1179` maxDD `-1.669`
- `market_context_high->metal_1h` score `0.3844` n `134` status `ready` deltaP `10.9036` edge `0.0145` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3278` n `134` status `ready` deltaP `15.6785` edge `0.0271` maxDD `-1.8344`
- `news_risk_high->commodity_4h` score `0.209` n `35` status `ready` deltaP `0.2482` edge `0.0589` maxDD `-0.7008`
- `market_context_high->equity_1h` score `0.1526` n `134` status `ready` deltaP `4.6318` edge `0.0694` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.1299` n `134` status `ready` deltaP `12.8708` edge `0.0469` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.066` n `134` status `ready` deltaP `7.4649` edge `0.0585` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.087` n `134` status `ready` deltaP `3.8788` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1949` n `134` status `ready` deltaP `2.3912` edge `0.1175` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.326` n `134` status `ready` deltaP `1.6445` edge `0.0133` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.42` n `47` status `ready` deltaP `2.9239` edge `-0.004` maxDD `-0.5475`
- `market_context_high->fx_4h` score `-0.5393` n `134` status `ready` deltaP `-0.7781` edge `-0.0041` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.8384` n `47` status `ready` deltaP `-10.8039` edge `0.0105` maxDD `-0.6773`
- `market_context_high->crypto_alt_1h` score `-0.8485` n `134` status `ready` deltaP `2.9985` edge `0.0577` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
