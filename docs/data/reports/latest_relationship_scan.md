# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T11:41:03.077070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.0327` n `145` status `ready` deltaP `7.7969` edge `0.0568` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.2919` n `133` status `ready` deltaP `18.6514` edge `-0.0561` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0535` n `133` status `ready` deltaP `7.1429` edge `0.0095` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0241` n `145` status `ready` deltaP `7.7225` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0225` n `145` status `ready` deltaP `4.2154` edge `0.0049` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2899` n `145` status `ready` deltaP `1.4247` edge `-0.0048` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2971` n `133` status `ready` deltaP `6.1663` edge `-0.0176` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3437` n `145` status `ready` deltaP `4.4879` edge `0.033` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5524` n `133` status `ready` deltaP `3.2311` edge `0.0112` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6324` n `133` status `ready` deltaP `-0.2464` edge `0.0056` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8982` n `145` status `ready` deltaP `-6.6694` edge `-0.0016` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.3571` n `133` status `ready` deltaP `5.8798` edge `-0.0253` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.6345` n `133` status `ready` deltaP `0.0092` edge `0.0709` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-1.9097` n `119` status `ready` deltaP `-5.6271` edge `0.0617` maxDD `-4.666`
- `market_context_high->fx_24h` score `-1.9573` n `119` status `ready` deltaP `-1.4283` edge `0.0074` maxDD `-2.2121`
- `market_context_high->crypto_alt_1h` score `-2.3169` n `145` status `ready` deltaP `-1.9492` edge `-0.0306` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.373` n `145` status `ready` deltaP `-4.6221` edge `-0.1044` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.4182` n `119` status `ready` deltaP `-7.6637` edge `-0.0468` maxDD `-20.1505`
- `market_context_high->crypto_major_4h` score `-4.8103` n `133` status `ready` deltaP `-0.4298` edge `-0.2959` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.3775` n `119` status `ready` deltaP `-23.6286` edge `-0.2011` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
