# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T21:22:27.533004+00:00`
- Price records: `672`
- Market context records: `3113`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6925`

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

- `market_context_high->commodity_24h` score `14.6724` n `92` status `ready` deltaP `46.2938` edge `0.9569` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `14.3342` n `92` status `ready` deltaP `12.1226` edge `2.4401` maxDD `-45.9894`
- `market_context_high->unknown_24h` score `13.355` n `92` status `ready` deltaP `22.5317` edge `1.0115` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.3962` n `92` status `ready` deltaP `32.7295` edge `0.9036` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.0791` n `92` status `ready` deltaP `14.7116` edge `1.3421` maxDD `-43.864`
- `market_context_high->commodity_4h` score `2.9894` n `120` status `ready` deltaP `17.9878` edge `0.175` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0036` n `130` status `ready` deltaP `2.1995` edge `0.0273` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4258` n `130` status `ready` deltaP `4.8733` edge `0.0192` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5054` n `92` status `ready` deltaP `4.5969` edge `0.0` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7883` n `130` status `ready` deltaP `3.1644` edge `0.0908` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0409` n `130` status `ready` deltaP `0.7692` edge `0.01` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3454` n `120` status `ready` deltaP `-12.7235` edge `-0.0033` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4305` n `120` status `ready` deltaP `9.4817` edge `0.0443` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.4487` n `130` status `ready` deltaP `-9.871` edge `-0.0052` maxDD `-0.644`
- `market_context_high->unknown_4h` score `-1.9576` n `120` status `ready` deltaP `4.2887` edge `0.01` maxDD `-13.8046`
- `market_context_high->crypto_major_1h` score `-2.1248` n `130` status `ready` deltaP `-0.6564` edge `0.0536` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3054` n `130` status `ready` deltaP `-6.5776` edge `-0.0089` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.8447` n `130` status `ready` deltaP `2.2616` edge `-0.0495` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.954` n `120` status `ready` deltaP `12.0528` edge `0.2172` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0648` n `120` status `ready` deltaP `5.9146` edge `-0.03` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
