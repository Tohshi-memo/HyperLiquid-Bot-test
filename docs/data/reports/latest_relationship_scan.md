# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T11:22:27.303773+00:00`
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

- `market_context_high->unknown_1h` score `1.0523` n `144` status `ready` deltaP `7.7263` edge `0.0589` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3077` n `133` status `ready` deltaP `18.8039` edge `-0.0558` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0622` n `133` status `ready` deltaP `7.2953` edge `0.0096` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0084` n `144` status `ready` deltaP `7.4351` edge `0.0046` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0314` n `144` status `ready` deltaP `4.0586` edge `0.0048` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2704` n `144` status `ready` deltaP `1.7839` edge `-0.0047` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2891` n `133` status `ready` deltaP `6.3187` edge `-0.0176` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.329` n `144` status `ready` deltaP `4.7405` edge `0.0332` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5603` n `133` status `ready` deltaP `3.0786` edge `0.0112` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6403` n `133` status `ready` deltaP `-0.3989` edge `0.0056` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8581` n `144` status `ready` deltaP `-6.5078` edge `-0.0017` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4029` n `133` status `ready` deltaP `5.7274` edge `-0.0281` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.6464` n `133` status `ready` deltaP `-0.1433` edge `0.0704` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-1.9128` n `118` status `ready` deltaP `-5.8763` edge `0.0631` maxDD `-4.666`
- `market_context_high->fx_24h` score `-2.0113` n `118` status `ready` deltaP `-1.998` edge `0.0067` maxDD `-2.2121`
- `market_context_high->crypto_alt_1h` score `-2.3355` n `144` status `ready` deltaP `-2.0916` edge `-0.0312` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.3391` n `144` status `ready` deltaP `-4.2581` edge `-0.104` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.3955` n `118` status `ready` deltaP `-7.4741` edge `-0.047` maxDD `-20.0029`
- `market_context_high->crypto_major_4h` score `-4.8621` n `133` status `ready` deltaP `-0.5822` edge `-0.2992` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.3529` n `118` status `ready` deltaP `-23.3963` edge `-0.1995` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
