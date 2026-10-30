# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T15:37:39.297236+00:00`
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

- `market_context_high->unknown_24h` score `1612.033` n `134` status `ready` deltaP `-3.4852` edge `134.4023` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `159.7961` n `56` status `ready` deltaP `-0.0749` edge `13.3294` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.6914` n `134` status `ready` deltaP `1.0261` edge `2.6474` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.4681` n `44` status `ready` deltaP `20.9118` edge `0.5226` maxDD `-1.5072`
- `market_context_high->equity_24h` score `3.7001` n `134` status `ready` deltaP `16.6589` edge `0.473` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.4546` n `134` status `ready` deltaP `35.2638` edge `0.0711` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4058` n `56` status `ready` deltaP `8.2121` edge `0.1335` maxDD `-3.3547`
- `market_context_high->metal_1h` score `0.4117` n `134` status `ready` deltaP `11.3527` edge `0.015` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3756` n `134` status `ready` deltaP `15.9834` edge `0.0312` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3037` n `134` status `ready` deltaP `5.3803` edge `0.077` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2075` n `134` status `ready` deltaP `13.4806` edge `0.0493` maxDD `-1.0837`
- `news_risk_high->commodity_4h` score `0.1384` n `44` status `ready` deltaP `0.0139` edge `0.0452` maxDD `-0.7008`
- `market_context_high->crypto_major_1h` score `0.0648` n `134` status `ready` deltaP `7.6146` edge `0.0574` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0312` n `134` status `ready` deltaP `3.3059` edge `0.1324` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0753` n `134` status `ready` deltaP `4.0285` edge `-0.0007` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.326` n `134` status `ready` deltaP `1.6445` edge `0.0133` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.3919` n `56` status `ready` deltaP `3.411` edge `-0.0031` maxDD `-0.5909`
- `market_context_high->fx_4h` score `-0.5038` n `134` status `ready` deltaP `-0.3208` edge `-0.0026` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.8174` n `134` status `ready` deltaP `-1.9461` edge `0.0007` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.861` n `134` status `ready` deltaP `3.1482` edge `0.0551` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
