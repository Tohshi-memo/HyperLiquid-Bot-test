# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T08:22:25.031592+00:00`
- Price records: `672`
- Market context records: `7757`
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

- `market_context_high->equity_24h` score `5.5608` n `132` status `ready` deltaP `23.5772` edge `0.4404` maxDD `-6.0681`
- `market_context_high->metal_24h` score `0.8651` n `133` status `ready` deltaP `9.6256` edge `0.217` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.7768` n `133` status `ready` deltaP `11.5112` edge `0.0321` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.4723` n `132` status `ready` deltaP `20.1325` edge `0.0351` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4637` n `133` status `ready` deltaP `12.5172` edge `0.127` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.4046` n `133` status `ready` deltaP `7.7457` edge `0.068` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.3942` n `133` status `ready` deltaP `1.9694` edge `0.2287` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.347` n `133` status `ready` deltaP `8.6444` edge `0.0143` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2076` n `133` status `ready` deltaP `6.8276` edge `0.0835` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0446` n `133` status `ready` deltaP `3.0807` edge `0.019` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1304` n `133` status `ready` deltaP `4.1455` edge `0.0074` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.149` n `133` status `ready` deltaP `4.1756` edge `0.0191` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2584` n `133` status `ready` deltaP `10.5585` edge `0.0423` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4759` n `133` status `ready` deltaP `-0.0767` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8411` n `133` status `ready` deltaP `1.7165` edge `0.0188` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4855` n `133` status `ready` deltaP `0.9857` edge `0.0751` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4936` n `133` status `ready` deltaP `-4.1617` edge `-0.0009` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.4942` n `132` status `ready` deltaP `6.0342` edge `-0.0064` maxDD `-7.0012`
- `market_context_high->index_24h` score `-2.194` n `132` status `ready` deltaP `-15.3178` edge `0.0311` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2812` n `133` status `ready` deltaP `-1.5735` edge `-0.1206` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
