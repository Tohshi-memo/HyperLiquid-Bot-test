# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T09:07:33.234154+00:00`
- Price records: `672`
- Market context records: `6483`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.6025` n `32` status `ready` deltaP `34.0278` edge `0.8381` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.6683` n `159` status `ready` deltaP `16.4275` edge `0.7762` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4505` n `32` status `ready` deltaP `53.6458` edge `0.1799` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3337` n `32` status `ready` deltaP `16.8403` edge `0.5213` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9654` n `38` status `ready` deltaP `42.2176` edge `0.0536` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.0531` n `32` status `ready` deltaP `28.6458` edge `0.084` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.3464` n `180` status `ready` deltaP `-4.7039` edge `0.317` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8311` n `38` status `ready` deltaP `22.9121` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5528` n `38` status `ready` deltaP `4.751` edge `0.0929` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4477` n `172` status `ready` deltaP `11.4968` edge `0.0283` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.2921` n `159` status `ready` deltaP `6.535` edge `0.1676` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.2512` n `172` status `ready` deltaP `8.5508` edge `0.1193` maxDD `-6.7632`
- `market_context_high->metal_4h` score `0.198` n `172` status `ready` deltaP `12.1986` edge `0.044` maxDD `-2.7056`
- `market_context_high->unknown_4h` score `0.1388` n `172` status `ready` deltaP `-15.8501` edge `0.3578` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0524` n `38` status `ready` deltaP `1.2843` edge `0.0491` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4563` n `32` status `ready` deltaP `4.6875` edge `-0.0026` maxDD `-2.3058`
- `market_context_high->crypto_alt_1h` score `-0.458` n `180` status `ready` deltaP `7.5416` edge `0.0223` maxDD `-5.8368`
- `market_context_high->equity_4h` score `-0.4713` n `172` status `ready` deltaP `8.1395` edge `0.0552` maxDD `-8.2573`
- `market_context_high->crypto_major_1h` score `-0.513` n `180` status `ready` deltaP `7.4119` edge `0.0114` maxDD `-6.7936`
- `market_context_high->metal_1h` score `-0.5538` n `180` status `ready` deltaP `0.835` edge `0.0012` maxDD `-1.8877`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
