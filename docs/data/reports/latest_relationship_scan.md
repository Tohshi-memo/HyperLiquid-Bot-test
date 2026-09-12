# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T21:07:27.151602+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12791`

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

- `risk_on_high->unknown_24h` score `12045.4681` n `31` status `ready` deltaP `15.4514` edge `1003.686` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `12045.4681` n `31` status `ready` deltaP `15.4514` edge `1003.686` maxDD `0.0`
- `market_context_high->unknown_24h` score `11833.5137` n `71` status `ready` deltaP `12.6345` edge `986.0471` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.9876` n `82` status `ready` deltaP `-5.5499` edge `31.9948` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `19.0654` n `74` status `ready` deltaP `40.9159` edge `1.4533` maxDD `-8.3162`
- `news_risk_high->crypto_alt_24h` score `17.4308` n `74` status `ready` deltaP `31.2547` edge `1.293` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `13.5958` n `31` status `ready` deltaP `34.0446` edge `0.929` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.5958` n `31` status `ready` deltaP `34.0446` edge `0.929` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `12.8834` n `71` status `ready` deltaP `27.6384` edge `0.9721` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `10.2299` n `31` status `ready` deltaP `43.2292` edge `0.5643` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.2299` n `31` status `ready` deltaP `43.2292` edge `0.5643` maxDD `0.0`
- `market_context_high->equity_24h` score `9.7415` n `71` status `ready` deltaP `43.2292` edge `0.5236` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.8979` n `74` status `ready` deltaP `20.2562` edge `0.6412` maxDD `-4.4467`
- `news_risk_high->index_24h` score `6.5607` n `74` status `ready` deltaP `44.6086` edge `0.267` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.8466` n `74` status `ready` deltaP `35.5574` edge `0.2943` maxDD `-0.5303`
- `risk_on_high->index_24h` score `5.3849` n `31` status `ready` deltaP `53.545` edge `0.096` maxDD `-0.005`
- `risk_on_and_context->index_24h` score `5.3849` n `31` status `ready` deltaP `53.545` edge `0.096` maxDD `-0.005`
- `market_context_high->index_24h` score `3.3069` n `71` status `ready` deltaP `35.644` edge `0.0773` maxDD `-0.1483`
- `market_context_high->commodity_24h` score `2.9695` n `71` status `ready` deltaP `33.216` edge `0.0399` maxDD `-0.1105`
- `risk_on_high->commodity_24h` score `2.4426` n `31` status `ready` deltaP `28.7635` edge `0.0211` maxDD `-0.0777`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
