# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T09:07:27.932057+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.1989` n `128` status `ready` deltaP `-27.0622` edge `11.9049` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.4582` n `32` status `ready` deltaP `-40.3434` edge `4.6335` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.4582` n `32` status `ready` deltaP `-40.3434` edge `4.6335` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.1759` n `36` status `ready` deltaP `22.5014` edge `0.9026` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6181` n `36` status `ready` deltaP `39.726` edge `0.37` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.2005` n `128` status `ready` deltaP `29.7186` edge `0.241` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.7766` n `32` status `ready` deltaP `32.0624` edge `0.1843` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7766` n `32` status `ready` deltaP `32.0624` edge `0.1843` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1999` n `32` status `ready` deltaP `28.0275` edge `0.4672` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.1999` n `32` status `ready` deltaP `28.0275` edge `0.4672` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.2788` n `36` status `ready` deltaP `26.6898` edge `0.0953` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9183` n `32` status `ready` deltaP `21.1996` edge `0.1201` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9183` n `32` status `ready` deltaP `21.1996` edge `0.1201` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.9705` n `128` status `ready` deltaP `19.6371` edge `0.0804` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8392` n `36` status `ready` deltaP `21.2328` edge `0.0249` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.719` n `36` status `ready` deltaP `8.2835` edge `0.1199` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2731` n `32` status `ready` deltaP `13.5105` edge `0.0393` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2731` n `32` status `ready` deltaP `13.5105` edge `0.0393` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6365` n `128` status `ready` deltaP `8.823` edge `0.0239` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5374` n `32` status `ready` deltaP `6.5687` edge `0.0151` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
