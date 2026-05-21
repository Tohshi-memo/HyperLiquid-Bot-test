# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T13:37:21.314326+00:00`
- Price records: `672`
- Market context records: `1427`
- Flow alert records: `6024`
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

- `market_context_high->crypto_alt_24h` score `11.7917` n `154` status `ready` deltaP `28.7811` edge `0.9924` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.759` n `154` status `ready` deltaP `12.3354` edge `1.0644` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.738` n `154` status `ready` deltaP `27.3539` edge `0.909` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8445` n `154` status `ready` deltaP `19.3813` edge `0.2998` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7687` n `154` status `ready` deltaP `12.5271` edge `0.3799` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0004` n `202` status `ready` deltaP `5.6946` edge `0.1284` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0755` n `154` status `ready` deltaP `9.3592` edge `0.0488` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2287` n `213` status `ready` deltaP `2.8127` edge `0.0087` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3313` n `213` status `ready` deltaP `1.996` edge `0.0191` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4611` n `213` status `ready` deltaP `1.5954` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.5858` n `213` status `ready` deltaP `-0.2144` edge `0.0141` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.6296` n `202` status `ready` deltaP `0.2898` edge `0.0545` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.8066` n `213` status `ready` deltaP `1.2075` edge `0.0271` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9598` n `213` status `ready` deltaP `3.725` edge `-0.0143` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.11` n `202` status `ready` deltaP `8.2588` edge `0.1844` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.2698` n `202` status `ready` deltaP `5.29` edge `0.1298` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5812` n `202` status `ready` deltaP `-3.811` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.8214` n `213` status `ready` deltaP `-1.7999` edge `-0.0041` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-2.7018` n `202` status `ready` deltaP `-10.5469` edge `-0.0214` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.7193` n `202` status `ready` deltaP `4.6063` edge `0.0025` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
