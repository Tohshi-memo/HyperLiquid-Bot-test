# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T20:37:34.934521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1615.6806` n `134` status `ready` deltaP `-2.0963` edge `134.697` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `62.5446` n `134` status `ready` deltaP `5.7517` edge `5.187` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.2778` n `134` status `ready` deltaP `27.7985` edge `0.0228` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2769` n `134` status `ready` deltaP `9.5563` edge `0.0097` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.0831` n `134` status `ready` deltaP `13.087` edge `0.013` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0599` n `134` status `ready` deltaP `11.6513` edge `0.0492` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1182` n `134` status `ready` deltaP `3.28` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.3561` n `134` status `ready` deltaP `5.5188` edge `0.0363` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.4001` n `134` status `ready` deltaP `1.7875` edge `0.0423` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.411` n `134` status `ready` deltaP `0.5966` edge `0.0132` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5124` n `134` status `ready` deltaP `-0.3208` edge `-0.0037` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.9948` n `134` status `ready` deltaP `-3.7425` edge `-0.0021` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.0795` n `134` status `ready` deltaP `4.6668` edge `0.012` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.1043` n `134` status `ready` deltaP `2.25` edge `0.0299` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5003` n `134` status `ready` deltaP `-2.7917` edge `-0.0153` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6553` n `134` status `ready` deltaP `3.9257` edge `0.0263` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4444` n `134` status `ready` deltaP `-7.1965` edge `-0.0237` maxDD `-3.5621`
- `market_context_high->equity_24h` score `-2.4861` n `134` status `ready` deltaP `10.2353` edge `0.0003` maxDD `-14.0571`
- `market_context_high->crypto_major_4h` score `-2.6539` n `134` status `ready` deltaP `4.8076` edge `-0.0428` maxDD `-19.0267`
- `market_context_high->commodity_24h` score `-4.4054` n `134` status `ready` deltaP `1.7724` edge `-0.0176` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
