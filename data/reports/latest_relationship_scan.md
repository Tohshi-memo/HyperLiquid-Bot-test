# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T04:52:34.028556+00:00`
- Price records: `672`
- Market context records: `7845`
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

- `market_context_high->equity_24h` score `10.2798` n `132` status `ready` deltaP `28.5507` edge `0.8005` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.2778` n `133` status `ready` deltaP `5.0275` edge `0.3216` maxDD `-6.9701`
- `market_context_high->commodity_24h` score `1.0737` n `132` status `ready` deltaP `20.253` edge `0.1128` maxDD `-7.0012`
- `market_context_high->metal_24h` score `1.0627` n `133` status `ready` deltaP `9.7249` edge `0.2328` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0442` n `133` status `ready` deltaP `12.8585` edge `0.0454` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0167` n `133` status `ready` deltaP `13.2794` edge `0.168` maxDD `-6.7444`
- `market_context_high->fx_24h` score `0.8335` n `132` status `ready` deltaP `25.2187` edge `0.0475` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.701` n `133` status `ready` deltaP `7.5955` edge `0.0937` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6306` n `133` status `ready` deltaP `7.2849` edge `0.1157` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.488` n `133` status `ready` deltaP `8.7627` edge `0.0416` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3758` n `133` status `ready` deltaP `8.6444` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1988` n `133` status `ready` deltaP `4.428` edge `0.0303` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0978` n `133` status `ready` deltaP `6.0975` edge `0.0134` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.092` n `133` status `ready` deltaP `12.3934` edge `0.0514` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3474` n `133` status `ready` deltaP `1.4248` edge `0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7884` n `133` status `ready` deltaP `2.1656` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.208` n `132` status `ready` deltaP `-4.9658` edge `0.0885` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.3213` n `133` status `ready` deltaP `2.6625` edge `0.0776` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4056` n `133` status `ready` deltaP `-2.7856` edge `0.0012` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.9327` n `133` status `ready` deltaP `14.9164` edge `0.1823` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
