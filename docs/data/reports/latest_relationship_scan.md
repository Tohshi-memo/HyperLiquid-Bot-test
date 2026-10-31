# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T10:37:27.907257+00:00`
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

- `market_context_high->unknown_24h` score `1989.6665` n `121` status `ready` deltaP `-6.2371` edge `165.8901` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `102.2886` n `98` status `ready` deltaP `-5.493` edge `8.5893` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `43.7981` n `121` status `ready` deltaP `1.6844` edge `3.6519` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.393` n `36` status `ready` deltaP `48.7847` edge `1.2123` maxDD `-0.049`
- `market_context_high->equity_24h` score `9.7611` n `121` status `ready` deltaP `23.9913` edge `0.9292` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1782` n `98` status `ready` deltaP `18.638` edge `0.4459` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.4768` n `121` status `ready` deltaP `41.4715` edge `0.1149` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.9343` n `121` status `ready` deltaP `13.6302` edge `0.016` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.9272` n `98` status `ready` deltaP `8.2457` edge `0.1052` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.4758` n `121` status `ready` deltaP `16.6448` edge `0.0327` maxDD `-1.6133`
- `market_context_high->equity_1h` score `0.3676` n `121` status `ready` deltaP `4.9946` edge `0.0849` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3094` n `121` status `ready` deltaP `8.528` edge `0.0717` maxDD `-5.2213`
- `market_context_high->commodity_4h` score `0.0849` n `121` status `ready` deltaP `12.0553` edge `0.0524` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.0007` n `121` status `ready` deltaP `1.7612` edge `0.144` maxDD `-5.7854`
- `market_context_high->fx_1h` score `-0.1216` n `121` status `ready` deltaP `3.1982` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->metal_24h` score `-0.1731` n `121` status `ready` deltaP `8.6561` edge `0.1848` maxDD `-10.5088`
- `market_context_high->commodity_1h` score `-0.2848` n `121` status `ready` deltaP `1.7543` edge `0.016` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4085` n `121` status `ready` deltaP `1.3682` edge `-0.0025` maxDD `-0.386`
- `market_context_high->index_1h` score `-0.5297` n `121` status `ready` deltaP `1.5453` edge `0.0014` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8694` n `98` status `ready` deltaP `1.7139` edge `-0.0039` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
