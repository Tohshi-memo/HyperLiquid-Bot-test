# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T04:07:26.563419+00:00`
- Price records: `672`
- Market context records: `7842`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `10.1574` n `132` status `ready` deltaP `28.5507` edge `0.7903` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3165` n `133` status `ready` deltaP `5.4862` edge `0.3235` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.1175` n `133` status `ready` deltaP `10.2449` edge `0.2339` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0753` n `133` status `ready` deltaP `13.1579` edge `0.046` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0579` n `133` status `ready` deltaP `13.5842` edge `0.1694` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `0.9839` n `132` status `ready` deltaP `19.7312` edge `0.1088` maxDD `-7.0012`
- `market_context_high->fx_24h` score `0.8312` n `132` status `ready` deltaP `25.2187` edge `0.0472` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7418` n `133` status `ready` deltaP `8.046` edge `0.0941` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6826` n `133` status `ready` deltaP `7.5898` edge `0.118` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.4685` n `133` status `ready` deltaP `8.6098` edge `0.041` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3758` n `133` status `ready` deltaP `8.6444` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2371` n `133` status `ready` deltaP `4.7274` edge `0.0315` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1122` n `133` status `ready` deltaP `6.2476` edge `0.0136` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0666` n `133` status `ready` deltaP `12.8521` edge `0.0516` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3726` n `133` status `ready` deltaP `1.1245` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8004` n `133` status `ready` deltaP `2.0159` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2315` n `132` status `ready` deltaP `-5.3136` edge `0.0878` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.3603` n `133` status `ready` deltaP `2.2052` edge `0.0774` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4302` n `133` status `ready` deltaP `-3.2443` edge `0.0011` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.9694` n `133` status `ready` deltaP `14.9164` edge `0.1776` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
