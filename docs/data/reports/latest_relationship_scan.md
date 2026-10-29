# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T15:23:06.415678+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6784`

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

- `market_context_high->unknown_24h` score `1541.1122` n `137` status `ready` deltaP `-0.7096` edge `128.4865` maxDD `-2.1267`
- `market_context_high->unknown_4h` score `59.6814` n `137` status `ready` deltaP `7.0856` edge `4.9395` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.864` n `137` status `ready` deltaP `24.156` edge `0.0126` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `0.2533` n `137` status `ready` deltaP `12.9584` edge `0.0566` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.1311` n `137` status `ready` deltaP `9.4792` edge `0.0083` maxDD `-0.7082`
- `market_context_high->metal_4h` score `-0.0325` n `137` status `ready` deltaP `12.4221` edge `0.0105` maxDD `-2.4653`
- `market_context_high->fx_1h` score `-0.0352` n `137` status `ready` deltaP `4.726` edge `-0.0002` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.224` n `137` status `ready` deltaP `2.4236` edge `0.0166` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.3021` n `137` status `ready` deltaP `3.1968` edge `-0.0002` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.5017` n `137` status `ready` deltaP `0.7769` edge `0.0276` maxDD `-3.1012`
- `market_context_high->index_1h` score `-0.7205` n `137` status `ready` deltaP `-3.8081` edge `-0.0028` maxDD `-1.1344`
- `market_context_high->crypto_major_1h` score `-0.7387` n `137` status `ready` deltaP `4.7074` edge `0.024` maxDD `-6.0219`
- `market_context_high->fx_24h` score `-0.8799` n `137` status `ready` deltaP `6.8317` edge `0.0142` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.3541` n `137` status `ready` deltaP `1.6183` edge `0.0144` maxDD `-9.2367`
- `market_context_high->metal_24h` score `-1.8381` n `137` status `ready` deltaP `2.9615` edge `0.0093` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-1.9912` n `137` status `ready` deltaP `-2.8685` edge `-0.0367` maxDD `-9.2902`
- `market_context_high->index_4h` score `-2.5324` n `137` status `ready` deltaP `-7.4094` edge `-0.0253` maxDD `-3.9067`
- `market_context_high->crypto_major_4h` score `-2.7495` n `137` status `ready` deltaP `3.9412` edge `-0.0353` maxDD `-20.1447`
- `market_context_high->equity_24h` score `-3.8143` n `137` status `ready` deltaP `6.6378` edge `-0.0864` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.7046` n `137` status `ready` deltaP `-0.6805` edge `-0.0396` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
