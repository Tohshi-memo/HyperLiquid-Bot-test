# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T22:46:01.240930+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14774`

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

- `market_context_high->unknown_1h` score `1.3703` n `133` status `ready` deltaP `8.9866` edge `0.077` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3768` n `133` status `ready` deltaP `22.1575` edge `-0.0724` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1826` n `133` status `ready` deltaP `10.7559` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1399` n `133` status `ready` deltaP `8.8197` edge `0.0094` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0848` n `133` status `ready` deltaP `3.0773` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2085` n `133` status `ready` deltaP `6.714` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3176` n `133` status `ready` deltaP `0.9815` edge `-0.0054` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3815` n `133` status `ready` deltaP `4.9468` edge `-0.0203` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5885` n `133` status `ready` deltaP `0.0584` edge `0.0092` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.5919` n `133` status `ready` deltaP `2.6213` edge `0.0102` maxDD `-2.618`
- `market_context_high->commodity_1h` score `-0.6768` n `133` status `ready` deltaP `-4.5709` edge `0.0003` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8` n `133` status `ready` deltaP `0.5696` edge `0.0097` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.0881` n `105` status `ready` deltaP `-0.9672` edge `0.0991` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3637` n `133` status `ready` deltaP `-1.5499` edge `-0.062` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.476` n `133` status `ready` deltaP `3.8981` edge `-0.022` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8256` n `133` status `ready` deltaP `-1.8201` edge `0.0586` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4027` n `105` status `ready` deltaP `-6.0516` edge `0.0011` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.2435` n `133` status `ready` deltaP `-0.1249` edge `-0.2507` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.3514` n `105` status `ready` deltaP `-7.8522` edge `-0.0553` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.8605` n `105` status `ready` deltaP `-18.4574` edge `-0.1693` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
