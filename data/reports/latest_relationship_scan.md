# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T09:22:28.263021+00:00`
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

- `market_context_high->unknown_24h` score `1766.8958` n `134` status `ready` deltaP `-2.7908` edge `147.3029` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `328.2606` n `31` status `ready` deltaP `-0.0289` edge `27.3678` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.7793` n `134` status `ready` deltaP `4.0749` edge `2.8844` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0786` n `134` status `ready` deltaP `33.3541` edge `0.0525` maxDD `-0.1315`
- `news_risk_high->index_1h` score `2.1444` n `31` status `ready` deltaP `27.6512` edge `0.0081` maxDD `-0.0996`
- `market_context_high->equity_24h` score `1.6864` n `134` status `ready` deltaP `16.3117` edge `0.3075` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `0.8986` n `31` status `ready` deltaP `9.4794` edge `0.0937` maxDD `-1.669`
- `market_context_high->metal_1h` score `0.3229` n `134` status `ready` deltaP `10.0054` edge `0.0126` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2672` n `134` status `ready` deltaP `15.0688` edge `0.0234` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1819` n `134` status `ready` deltaP `13.1757` edge `0.0492` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.1034` n `134` status `ready` deltaP `4.3324` edge `0.0673` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0155` n `134` status `ready` deltaP `6.7164` edge `0.0567` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1135` n `134` status `ready` deltaP `3.4297` edge `-0.0016` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.314` n `134` status `ready` deltaP `1.7942` edge `0.0133` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4645` n `134` status `ready` deltaP `0.8668` edge `0.0931` maxDD `-6.008`
- `news_risk_high->equity_1h` score `-0.4923` n `31` status `ready` deltaP `2.9602` edge `-0.0236` maxDD `-2.4064`
- `market_context_high->fx_4h` score `-0.5994` n `134` status `ready` deltaP `-1.8452` edge `-0.0047` maxDD `-0.4545`
- `news_risk_high->metal_1h` score `-0.6505` n `31` status `ready` deltaP `-3.0423` edge `-0.0094` maxDD `-0.9639`
- `market_context_high->crypto_alt_1h` score `-0.8165` n `134` status `ready` deltaP `3.1482` edge `0.0608` maxDD `-8.251`
- `news_risk_high->fx_1h` score `-0.8843` n `31` status `ready` deltaP `-9.1124` edge `-0.0012` maxDD `-0.1142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
