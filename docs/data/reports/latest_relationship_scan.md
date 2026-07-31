# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T22:22:32.329851+00:00`
- Price records: `672`
- Market context records: `8557`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `5076.9892` n `61` status `ready` deltaP `41.012` edge `422.8511` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6477` n `64` status `ready` deltaP `20.0457` edge `0.3967` maxDD `-3.4427`
- `market_context_high->crypto_alt_4h` score `2.0044` n `62` status `ready` deltaP `13.9703` edge `0.1696` maxDD `-5.323`
- `news_risk_high->index_4h` score `1.9999` n `64` status `ready` deltaP `16.5015` edge `0.0757` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7529` n `64` status `ready` deltaP `16.4016` edge `0.0844` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0658` n `64` status `ready` deltaP `7.0503` edge `0.1672` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7119` n `64` status `ready` deltaP `13.5671` edge `0.14` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4835` n `64` status `ready` deltaP `8.561` edge `0.0576` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3641` n `64` status `ready` deltaP `7.064` edge `0.0508` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0807` n `64` status `ready` deltaP `5.1366` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0161` n `64` status `ready` deltaP `3.7706` edge `0.0086` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0132` n `64` status `ready` deltaP `11.3186` edge `0.0214` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0396` n `64` status `ready` deltaP `1.7149` edge `0.0311` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.0976` n `64` status `ready` deltaP `3.7051` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.155` n `62` status `ready` deltaP `8.1432` edge `0.0124` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.284` n `62` status `ready` deltaP `2.062` edge `0.0001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3294` n `62` status `ready` deltaP `3.8584` edge `-0.0054` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4933` n `62` status `ready` deltaP `-2.4773` edge `0.016` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7585` n `62` status `ready` deltaP `0.7968` edge `-0.0156` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9386` n `62` status `ready` deltaP `-2.5449` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
