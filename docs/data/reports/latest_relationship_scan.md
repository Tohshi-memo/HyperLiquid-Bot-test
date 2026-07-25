# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T06:52:33.853691+00:00`
- Price records: `672`
- Market context records: `7853`
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

- `market_context_high->equity_24h` score `10.6686` n `132` status `ready` deltaP `28.5507` edge `0.8329` maxDD `-6.0681`
- `market_context_high->commodity_24h` score `1.299` n `132` status `ready` deltaP `21.6443` edge `0.1223` maxDD `-7.0012`
- `market_context_high->equity_4h` score `1.1838` n `133` status `ready` deltaP `3.8042` edge `0.3177` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.037` n `133` status `ready` deltaP `12.7088` edge `0.0458` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0143` n `133` status `ready` deltaP `13.2794` edge `0.1678` maxDD `-6.7444`
- `market_context_high->metal_24h` score `0.9218` n `133` status `ready` deltaP `8.3384` edge `0.2303` maxDD `-2.3927`
- `market_context_high->fx_24h` score `0.8382` n `132` status `ready` deltaP `25.2187` edge `0.0481` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.683` n `133` status `ready` deltaP `7.4454` edge `0.0932` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.6086` n `133` status `ready` deltaP `9.986` edge `0.0435` maxDD `-1.0817`
- `market_context_high->crypto_alt_4h` score `0.603` n `133` status `ready` deltaP `7.2849` edge `0.1134` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.3758` n `133` status `ready` deltaP `8.6444` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1952` n `133` status `ready` deltaP `4.2783` edge `0.031` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0834` n `133` status `ready` deltaP `5.9473` edge `0.0132` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1285` n `133` status `ready` deltaP `11.7818` edge `0.0508` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3726` n `133` status `ready` deltaP `1.1245` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7644` n `133` status `ready` deltaP `2.465` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1971` n `132` status `ready` deltaP `-4.9658` edge `0.0899` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.2202` n `133` status `ready` deltaP `3.882` edge `0.0779` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.3882` n `133` status `ready` deltaP `-2.4798` edge `0.0014` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.7278` n `133` status `ready` deltaP `15.783` edge `0.2028` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
