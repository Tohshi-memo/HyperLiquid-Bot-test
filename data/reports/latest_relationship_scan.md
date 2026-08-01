# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T08:22:29.552650+00:00`
- Price records: `672`
- Market context records: `8602`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4748.5764` n `64` status `ready` deltaP `34.7222` edge `395.5253` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `19.3708` n `30` status `ready` deltaP `48.8195` edge `1.3285` maxDD `-2.1786`
- `market_context_high->crypto_major_24h` score `6.8163` n `30` status `ready` deltaP `22.9861` edge `0.9035` maxDD `-11.9623`
- `news_risk_high->equity_4h` score `5.8039` n `64` status `ready` deltaP `20.1982` edge `0.4087` maxDD `-3.4427`
- `market_context_high->fx_24h` score `3.8004` n `30` status `ready` deltaP `38.6459` edge `0.0929` maxDD `-0.3737`
- `news_risk_high->index_4h` score `2.2518` n `64` status `ready` deltaP `19.2454` edge `0.0784` maxDD `-0.191`
- `market_context_high->metal_24h` score `2.0157` n `30` status `ready` deltaP `16.0416` edge `0.1143` maxDD `-1.5947`
- `news_risk_high->equity_1h` score `1.7529` n `64` status `ready` deltaP `16.4016` edge `0.0844` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5415` n `62` status `ready` deltaP `11.3788` edge `0.1483` maxDD `-5.323`
- `market_context_high->index_24h` score `1.4913` n `30` status `ready` deltaP `27.3264` edge `0.0739` maxDD `-2.5241`
- `news_risk_high->crypto_major_4h` score `1.0699` n `64` status `ready` deltaP `7.3552` edge `0.1657` maxDD `-3.5385`
- `market_context_high->equity_24h` score `0.4706` n `30` status `ready` deltaP `31.1458` edge `0.1419` maxDD `-20.4699`
- `news_risk_high->crypto_alt_4h` score `0.411` n `64` status `ready` deltaP `10.9756` edge `0.1187` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4087` n `64` status `ready` deltaP `7.8125` edge `0.053` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3586` n `64` status `ready` deltaP `7.064` edge `0.0501` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1056` n `64` status `ready` deltaP `5.5857` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0972` n `64` status `ready` deltaP `12.2332` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.0467` n `64` status `ready` deltaP `3.2393` edge `0.032` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0255` n `64` status `ready` deltaP `3.9203` edge `0.0088` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0711` n `62` status `ready` deltaP `9.0578` edge `0.0133` maxDD `-1.3685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
