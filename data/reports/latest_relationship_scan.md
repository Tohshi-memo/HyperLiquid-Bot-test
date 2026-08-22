# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T06:07:34.366616+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14742`

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

- `market_context_high->unknown_1h` score `1.4736` n `133` status `ready` deltaP `8.5375` edge `0.0886` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.6238` n `133` status `ready` deltaP `21.0904` edge `-0.0447` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.128` n `133` status `ready` deltaP `8.5149` edge `0.0099` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1211` n `133` status `ready` deltaP `9.5583` edge `0.0049` maxDD `-0.9144`
- `market_context_high->equity_1h` score `-0.1726` n `133` status `ready` deltaP `7.0134` edge `0.0381` maxDD `-5.2257`
- `market_context_high->fx_1h` score `-0.1782` n `133` status `ready` deltaP `1.2809` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2872` n `133` status `ready` deltaP `1.4306` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3049` n `133` status `ready` deltaP `6.1663` edge `-0.0186` maxDD `-1.5942`
- `market_context_high->commodity_1h` score `-0.6386` n `133` status `ready` deltaP `-3.8224` edge `0.0002` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6602` n `133` status `ready` deltaP `-0.8562` edge `0.0061` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.6822` n `133` status `ready` deltaP `0.9445` edge `0.0098` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.7783` n `133` status `ready` deltaP `-0.0292` edge `0.0155` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.3527` n `133` status `ready` deltaP `-1.5499` edge `-0.0606` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5095` n `105` status `ready` deltaP `-4.9603` edge `0.0906` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.8442` n `133` status `ready` deltaP `-2.5823` edge `0.0613` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4667` n `105` status `ready` deltaP `-6.7461` edge `0.0004` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-2.4768` n `133` status `ready` deltaP `3.8981` edge `-0.1054` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.2493` n `105` status `ready` deltaP `-5.7689` edge `-0.0561` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0879` n `105` status `ready` deltaP `-20.7143` edge `-0.1834` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5899` n `133` status `ready` deltaP `-1.9542` edge `-0.3507` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
