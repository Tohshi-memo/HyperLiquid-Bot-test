# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T21:37:28.032798+00:00`
- Price records: `672`
- Market context records: `7709`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.6159` n `132` status `ready` deltaP `19.396` edge `0.3062` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.2054` n `133` status `ready` deltaP `15.4135` edge `0.1695` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1077` n `133` status `ready` deltaP `13.3076` edge `0.0477` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.7729` n `133` status `ready` deltaP `8.8093` edge `0.1174` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.75` n `133` status `ready` deltaP `2.8868` edge `0.2682` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6567` n `133` status `ready` deltaP `8.7968` edge `0.082` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.4107` n `133` status `ready` deltaP `9.245` edge `0.0156` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1593` n `133` status `ready` deltaP `3.6795` edge `0.032` maxDD `-1.4603`
- `market_context_high->fx_24h` score `-0.0022` n `132` status `ready` deltaP `12.6413` edge `0.0242` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.1549` n `133` status `ready` deltaP `11.9347` edge `0.0464` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.1904` n `133` status `ready` deltaP `3.5449` edge `0.0064` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2299` n `133` status `ready` deltaP `3.8698` edge `0.0144` maxDD `-1.0817`
- `market_context_high->metal_24h` score `-0.517` n `133` status `ready` deltaP `3.0284` edge `0.1458` maxDD `-2.3927`
- `market_context_high->fx_1h` score `-0.5191` n `133` status `ready` deltaP `-0.5272` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8662` n `133` status `ready` deltaP `1.2674` edge `0.0197` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4247` n `133` status `ready` deltaP `1.5954` edge `0.0761` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5774` n `133` status `ready` deltaP `-5.385` edge `-0.0035` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7513` n `132` status `ready` deltaP `5.6858` edge `-0.0255` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1493` n `133` status `ready` deltaP `-0.9747` edge `-0.1136` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5887` n `132` status `ready` deltaP `-18.4537` edge `0.0014` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
