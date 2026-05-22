# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T17:22:21.316057+00:00`
- Price records: `672`
- Market context records: `1547`
- Flow alert records: `6366`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.2283` n `182` status `ready` deltaP `22.6018` edge `0.9684` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.9969` n `182` status `ready` deltaP `27.171` edge `0.9369` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.2709` n `182` status `ready` deltaP `26.7399` edge `0.7075` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.134` n `182` status `ready` deltaP `20.7799` edge `0.3146` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5653` n `182` status `ready` deltaP `13.3738` edge `0.3573` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.6875` n `182` status `ready` deltaP `16.5293` edge `0.052` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.2685` n `199` status `ready` deltaP `4.9386` edge `0.0989` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.2226` n `199` status `ready` deltaP `12.7972` edge `0.2181` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.311` n `199` status `ready` deltaP `8.8223` edge `0.1722` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.4509` n `199` status `ready` deltaP `0.5183` edge `0.0411` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6242` n `199` status `ready` deltaP `-1.9942` edge `-0.0035` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.711` n `199` status `ready` deltaP `-0.1978` edge `0.0023` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7625` n `199` status `ready` deltaP `4.8484` edge `0.0035` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7968` n `199` status `ready` deltaP `-0.4235` edge `-0.0004` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8584` n `199` status `ready` deltaP `-1.4819` edge `0.0192` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.9753` n `199` status `ready` deltaP `-0.8929` edge `0.0166` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3372` n `199` status `ready` deltaP `-9.7875` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3499` n `199` status `ready` deltaP `10.3636` edge `0.0876` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4354` n `199` status `ready` deltaP `-4.5923` edge `0.0199` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.2052` n `199` status `ready` deltaP `-15.0049` edge `-0.1046` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
