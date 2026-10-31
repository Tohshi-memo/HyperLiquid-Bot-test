# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T09:52:28.177683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7653`

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

- `market_context_high->unknown_24h` score `1890.1393` n `124` status `ready` deltaP `-5.8972` edge `157.5939` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `100.1574` n `98` status `ready` deltaP `-5.7924` edge `8.4137` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `35.3421` n `124` status `ready` deltaP `1.8243` edge `2.9463` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.6725` n `33` status `ready` deltaP `49.053` edge `1.2338` maxDD `-0.049`
- `market_context_high->equity_24h` score `9.5143` n `124` status `ready` deltaP `24.0704` edge `0.9081` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1902` n `98` status `ready` deltaP `18.638` edge `0.4469` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.4159` n `124` status `ready` deltaP `41.1907` edge `0.1117` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9104` n `98` status `ready` deltaP `8.096` edge `0.1048` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.9004` n `124` status `ready` deltaP `13.2364` edge `0.0158` maxDD `-0.3209`
- `market_context_high->metal_4h` score `0.4438` n `124` status `ready` deltaP `16.7781` edge `0.0326` maxDD `-1.671`
- `market_context_high->equity_1h` score `0.4244` n `124` status `ready` deltaP `5.7949` edge `0.0843` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3978` n `124` status `ready` deltaP `9.378` edge `0.0734` maxDD `-5.2213`
- `market_context_high->commodity_4h` score `0.1881` n `124` status `ready` deltaP `12.6377` edge `0.0533` maxDD `-1.0837`
- `market_context_high->equity_4h` score `-0.031` n `124` status `ready` deltaP `1.8096` edge `0.1424` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0715` n `124` status `ready` deltaP `4.1482` edge `-0.001` maxDD `-0.1986`
- `market_context_high->metal_24h` score `-0.2547` n `124` status `ready` deltaP `7.4764` edge `0.1822` maxDD `-10.5088`
- `market_context_high->commodity_1h` score `-0.2645` n `124` status `ready` deltaP `2.0378` edge `0.0158` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.458` n `124` status `ready` deltaP `0.5458` edge `-0.0028` maxDD `-0.4315`
- `market_context_high->index_1h` score `-0.4613` n `124` status `ready` deltaP `2.3856` edge `0.0015` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8204` n `124` status `ready` deltaP `2.994` edge `0.0524` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
