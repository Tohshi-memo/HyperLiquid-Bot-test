# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T16:52:31.304856+00:00`
- Price records: `672`
- Market context records: `7792`
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

- `market_context_high->equity_24h` score `7.8546` n `132` status `ready` deltaP `28.5507` edge `0.5984` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.5084` n `133` status `ready` deltaP `14.231` edge `0.2399` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.1854` n `133` status `ready` deltaP `14.7286` edge `0.1724` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.142` n `133` status `ready` deltaP `4.036` edge `0.3108` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.0573` n `133` status `ready` deltaP `13.2326` edge `0.044` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.9737` n `133` status `ready` deltaP `9.1885` edge `0.1316` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8101` n `132` status `ready` deltaP `25.2187` edge `0.0445` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6723` n `133` status `ready` deltaP `7.822` edge `0.0898` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3624` n `133` status `ready` deltaP `8.5672` edge `0.0161` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.3557` n `133` status `ready` deltaP `7.6347` edge `0.0381` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.2285` n `133` status `ready` deltaP `4.6495` edge `0.0313` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0372` n `133` status `ready` deltaP `5.43` edge `0.0128` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1164` n `133` status `ready` deltaP `12.1655` edge `0.0498` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3405` n `133` status `ready` deltaP `1.4959` edge `0.0004` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.3574` n `132` status `ready` deltaP `11.9052` edge `0.0492` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9048` n `133` status `ready` deltaP `0.8901` edge `0.019` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.339` n `133` status `ready` deltaP `-1.6541` edge `0.0022` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5354` n `133` status `ready` deltaP `0.452` edge `0.0745` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.6576` n `132` status `ready` deltaP `-9.4875` edge `0.061` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.3333` n `133` status `ready` deltaP `14.7431` edge `0.1321` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
