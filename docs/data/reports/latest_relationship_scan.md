# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T12:22:20.369222+00:00`
- Price records: `672`
- Market context records: `1422`
- Flow alert records: `6008`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `11.8136` n `154` status `ready` deltaP `27.3539` edge `0.9153` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.6165` n `154` status `ready` deltaP `28.7811` edge `0.9778` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.5823` n `154` status `ready` deltaP `11.6409` edge `1.0543` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7725` n `154` status `ready` deltaP `19.3813` edge `0.2938` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4879` n `154` status `ready` deltaP `12.5271` edge `0.3565` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8663` n `202` status `ready` deltaP `4.9324` edge `0.1223` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0563` n `154` status `ready` deltaP `9.3592` edge `0.0472` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1317` n `208` status `ready` deltaP `3.7397` edge `0.0106` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2563` n `208` status `ready` deltaP `2.2743` edge `0.0235` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3764` n `208` status `ready` deltaP `2.5939` edge `-0.0021` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6003` n `208` status `ready` deltaP `0.4347` edge `0.0225` maxDD `-4.1892`
- `market_context_high->commodity_1h` score `-0.6562` n `208` status `ready` deltaP `-0.6305` edge `0.011` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.7542` n `202` status `ready` deltaP `-0.4724` edge `0.0492` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.9131` n `208` status `ready` deltaP `4.1628` edge `-0.0128` maxDD `-6.2283`
- `market_context_high->crypto_major_1h` score `-1.2351` n `208` status `ready` deltaP `-2.2138` edge `-0.0079` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.2669` n `202` status `ready` deltaP `7.4966` edge `0.1764` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.336` n `202` status `ready` deltaP `5.1376` edge `0.1253` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6262` n `202` status `ready` deltaP `-4.2683` edge `-0.01` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5867` n `202` status `ready` deltaP `-10.0896` edge `-0.0097` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8531` n `202` status `ready` deltaP `4.149` edge `-0.0056` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
