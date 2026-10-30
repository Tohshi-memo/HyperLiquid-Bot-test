# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T16:22:35.879383+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7068`

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

- `market_context_high->unknown_24h` score `1609.1685` n `134` status `ready` deltaP `-3.8324` edge `134.1659` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `169.435` n `59` status `ready` deltaP `0.1116` edge `14.1314` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.7478` n `134` status `ready` deltaP `1.0261` edge `2.6521` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.3856` n `47` status `ready` deltaP `22.3404` edge `0.5062` maxDD `-1.5072`
- `market_context_high->equity_24h` score `4.0001` n `134` status `ready` deltaP `16.6589` edge `0.498` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.475` n `134` status `ready` deltaP `35.2638` edge `0.0728` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.1266` n `59` status `ready` deltaP `7.3328` edge `0.1161` maxDD `-3.3547`
- `news_risk_high->commodity_4h` score `0.4377` n `47` status `ready` deltaP `3.3504` edge `0.0479` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.414` n `134` status `ready` deltaP `11.3527` edge `0.0153` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3795` n `134` status `ready` deltaP `15.9834` edge `0.0317` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3457` n `134` status `ready` deltaP `5.53` edge `0.0795` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2147` n `134` status `ready` deltaP `13.4806` edge `0.0499` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.1007` n `134` status `ready` deltaP `7.7643` edge `0.0594` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0054` n `134` status `ready` deltaP `3.3059` edge `0.1357` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0847` n `134` status `ready` deltaP `3.8788` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.326` n `134` status `ready` deltaP `1.6445` edge `0.0133` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5022` n `134` status `ready` deltaP `-0.3208` edge `-0.0024` maxDD `-0.4545`
- `news_risk_high->index_1h` score `-0.5773` n `59` status `ready` deltaP `0.5963` edge `-0.0062` maxDD `-0.7428`
- `news_risk_high->commodity_1h` score `-0.7718` n `59` status `ready` deltaP `-5.034` edge `0.0195` maxDD `-0.6872`
- `market_context_high->index_1h` score `-0.8162` n `134` status `ready` deltaP `-1.9461` edge `0.0008` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
