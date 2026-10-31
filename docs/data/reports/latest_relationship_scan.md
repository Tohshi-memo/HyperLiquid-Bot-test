# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T12:07:30.599309+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2204.2099` n `115` status `ready` deltaP `-6.9701` edge `183.7736` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `94.2654` n `98` status `ready` deltaP `-5.493` edge `7.9207` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `54.0939` n `115` status `ready` deltaP `1.3825` edge `4.5119` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.3172` n `42` status `ready` deltaP `45.9325` edge `1.142` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.4` n `115` status `ready` deltaP `25.8273` edge `0.9702` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `4.952` n `98` status `ready` deltaP `18.1807` edge `0.4301` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.6003` n `115` status `ready` deltaP `41.9958` edge `0.1217` maxDD `-0.1315`
- `market_context_high->metal_4h` score `0.8804` n `115` status `ready` deltaP `19.0734` edge `0.0365` maxDD `-1.0629`
- `news_risk_high->crypto_alt_1h` score `0.8744` n `98` status `ready` deltaP `7.7966` edge `0.1038` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.5961` n `115` status `ready` deltaP `13.3858` edge `0.0162` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.4016` n `115` status `ready` deltaP `4.1728` edge `0.163` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.3482` n `115` status `ready` deltaP `4.6615` edge `0.0855` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.2485` n `115` status `ready` deltaP `7.8118` edge `0.0714` maxDD `-5.2213`
- `market_context_high->metal_24h` score `-0.0127` n `115` status `ready` deltaP `11.2001` edge `0.1884` maxDD `-10.5088`
- `market_context_high->commodity_4h` score `-0.0504` n `115` status `ready` deltaP `9.8131` edge `0.05` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.0663` n `115` status `ready` deltaP `4.1552` edge `-0.0008` maxDD `-0.1655`
- `market_context_high->fx_4h` score `-0.2929` n `115` status `ready` deltaP `2.6485` edge `-0.0017` maxDD `-0.2811`
- `market_context_high->commodity_1h` score `-0.3304` n `115` status `ready` deltaP `-0.6196` edge `0.0132` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.5081` n `115` status `ready` deltaP `1.8459` edge `0.0012` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-0.6305` n `115` status `ready` deltaP `13.648` edge `0.1022` maxDD `-14.5879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
