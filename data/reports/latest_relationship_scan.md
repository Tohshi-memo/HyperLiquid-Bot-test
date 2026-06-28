# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T22:52:25.356505+00:00`
- Price records: `672`
- Market context records: `5086`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `11.82` n `73` status `ready` deltaP `26.8883` edge `0.84` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `10.1573` n `106` status `ready` deltaP `1.1383` edge `0.903` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `9.0215` n `94` status `ready` deltaP `21.5718` edge `0.7102` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.7898` n `94` status `ready` deltaP `16.4277` edge `0.4949` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `4.6735` n `94` status `ready` deltaP `14.9099` edge `0.4881` maxDD `-11.5101`
- `market_context_high->equity_4h` score `2.4374` n `94` status `ready` deltaP `13.5249` edge `0.2261` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.3318` n `106` status `ready` deltaP `12.1145` edge `0.0834` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.7403` n `106` status `ready` deltaP `5.8694` edge `0.1082` maxDD `-4.1845`
- `market_context_high->index_1h` score `0.5604` n `106` status `ready` deltaP `8.6855` edge `0.0186` maxDD `-0.3843`
- `market_context_high->metal_1h` score `0.4439` n `106` status `ready` deltaP `11.14` edge `0.0323` maxDD `-1.3057`
- `market_context_high->crypto_major_1h` score `0.4172` n `106` status `ready` deltaP `7.1263` edge `0.1205` maxDD `-6.1613`
- `market_context_high->index_4h` score `0.3968` n `94` status `ready` deltaP `9.2825` edge `0.0473` maxDD `-1.0893`
- `market_context_high->metal_4h` score `0.2598` n `94` status `ready` deltaP `7.9204` edge `0.0884` maxDD `-1.9651`
- `market_context_high->commodity_4h` score `-0.5262` n `94` status `ready` deltaP `8.3841` edge `0.0081` maxDD `-3.6276`
- `market_context_high->fx_24h` score `-0.6889` n `73` status `ready` deltaP `-0.9941` edge `-0.0055` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.8467` n `106` status `ready` deltaP `-0.2853` edge `0.0016` maxDD `-1.6202`
- `market_context_high->commodity_24h` score `-1.2755` n `73` status `ready` deltaP `11.758` edge `0.0543` maxDD `-15.0303`
- `market_context_high->fx_1h` score `-1.8259` n `106` status `ready` deltaP `-12.3997` edge `-0.0054` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-2.133` n `94` status `ready` deltaP `-9.4221` edge `-0.0105` maxDD `-1.6885`
- `market_context_high->metal_24h` score `-4.5561` n `73` status `ready` deltaP `-4.9705` edge `-0.0055` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
