# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T22:22:30.803415+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10145`

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

- `market_context_high->unknown_1h` score `84.5371` n `47` status `ready` deltaP `10.116` edge `6.9844` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.1285` n `47` status `ready` deltaP `30.4226` edge `3.6805` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.5596` n `47` status `ready` deltaP `24.782` edge `2.4194` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3615` n `47` status `ready` deltaP `32.8531` edge `1.93` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.0095` n `47` status `ready` deltaP `36.4989` edge `0.4371` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `6.8481` n `114` status `ready` deltaP `-4.0498` edge `0.6221` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.2079` n `47` status `ready` deltaP `35.5792` edge `0.1373` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.253` n `114` status `ready` deltaP `16.1572` edge `0.2124` maxDD `-1.5895`
- `news_risk_high->commodity_24h` score `2.8935` n `76` status `ready` deltaP `27.4214` edge `0.0973` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.8817` n `47` status `ready` deltaP `33.1117` edge `0.0348` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.3155` n `114` status `ready` deltaP `16.0705` edge `0.1335` maxDD `-1.8141`
- `market_context_high->equity_4h` score `2.3139` n `47` status `ready` deltaP `16.5347` edge `0.1244` maxDD `-1.3444`
- `news_risk_high->crypto_major_4h` score `2.2551` n `102` status `ready` deltaP `16.302` edge `0.2924` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.15` n `102` status `ready` deltaP `8.5037` edge `0.3676` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `1.4558` n `114` status `ready` deltaP `18.7835` edge `0.0246` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.4294` n `102` status `ready` deltaP `21.5866` edge `0.0388` maxDD `-0.421`
- `market_context_high->index_1h` score `0.9739` n `47` status `ready` deltaP `14.7598` edge `0.0106` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9223` n `47` status `ready` deltaP `11.4664` edge `0.0407` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.5695` n `76` status `ready` deltaP `21.6374` edge `0.0736` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.5253` n `76` status `ready` deltaP `20.0201` edge `0.097` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
