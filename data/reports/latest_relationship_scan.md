# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T11:07:28.890555+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7046`

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

- `market_context_high->unknown_24h` score `1790.9894` n `134` status `ready` deltaP `-2.7908` edge `149.3107` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `234.2749` n `38` status `ready` deltaP `-2.9152` edge `19.5549` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.3995` n `134` status `ready` deltaP `3.6176` edge `2.8558` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.1549` n `134` status `ready` deltaP `33.5277` edge `0.0577` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `2.3979` n `38` status `ready` deltaP `14.7179` edge `0.1434` maxDD `-1.669`
- `market_context_high->equity_24h` score `2.1016` n `134` status `ready` deltaP `16.3117` edge `0.3421` maxDD `-14.0571`
- `news_risk_high->index_1h` score `0.4224` n `38` status `ready` deltaP `13.2446` edge `-0.0005` maxDD `-0.3577`
- `market_context_high->metal_1h` score `0.368` n `134` status `ready` deltaP `10.7539` edge `0.0134` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2925` n `134` status `ready` deltaP `15.3736` edge `0.0246` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1094` n `134` status `ready` deltaP `4.3324` edge `0.0678` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.0923` n `134` status `ready` deltaP `12.566` edge `0.0458` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.0347` n `134` status `ready` deltaP `6.7164` edge `0.0551` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1213` n `134` status `ready` deltaP `3.28` edge `-0.0016` maxDD `-0.1986`
- `news_risk_high->commodity_1h` score `-0.1291` n `38` status `ready` deltaP `-2.3322` edge `0.0292` maxDD `-0.4158`
- `market_context_high->commodity_1h` score `-0.3871` n `134` status `ready` deltaP `1.0457` edge `0.0122` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4176` n `134` status `ready` deltaP `1.0193` edge `0.0981` maxDD `-6.008`
- `news_risk_high->fx_1h` score `-0.4603` n `38` status `ready` deltaP `-1.1976` edge `0.0004` maxDD `-0.1142`
- `market_context_high->fx_4h` score `-0.6097` n `134` status `ready` deltaP `-1.9976` edge `-0.005` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8695` n `134` status `ready` deltaP `2.6991` edge `0.057` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.875` n `134` status `ready` deltaP `-2.5449` edge `-0.0001` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
