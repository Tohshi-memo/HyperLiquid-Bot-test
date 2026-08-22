# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T17:52:28.310182+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14866`

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

- `market_context_high->unknown_1h` score `1.5527` n `149` status `ready` deltaP `6.7074` edge `0.1074` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9879` n `149` status `ready` deltaP `18.7418` edge `0.0013` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1089` n `149` status `ready` deltaP `8.2071` edge `0.0095` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0204` n `149` status `ready` deltaP `6.8973` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1114` n `149` status `ready` deltaP `2.566` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2801` n `149` status `ready` deltaP `8.3023` edge `-0.0171` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3283` n `149` status `ready` deltaP `4.8738` edge `0.0324` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3561` n `149` status `ready` deltaP `0.1809` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5047` n `149` status `ready` deltaP `4.0872` edge `0.0116` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.843` n `149` status `ready` deltaP `-3.4713` edge `0.0001` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0807` n `133` status `ready` deltaP `1.6552` edge `0.0114` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1391` n `149` status `ready` deltaP `-8.6213` edge `-0.0028` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6863` n `149` status `ready` deltaP `-0.6701` edge `0.0699` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.2021` n `133` status `ready` deltaP `-5.2475` edge `0.0348` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.4227` n `149` status `ready` deltaP `3.3035` edge `-0.0771` maxDD `-7.0785`
- `market_context_high->crypto_alt_1h` score `-2.5256` n `149` status `ready` deltaP `-2.5338` edge `-0.0441` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.6052` n `149` status `ready` deltaP `-5.358` edge `-0.117` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.4054` n `133` status `ready` deltaP `-7.2565` edge `-0.0357` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.453` n `133` status `ready` deltaP `-24.3304` edge `-0.2061` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.6076` n `149` status `ready` deltaP `-0.5412` edge `-0.3307` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
