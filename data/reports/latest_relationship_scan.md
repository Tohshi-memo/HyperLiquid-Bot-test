# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T23:07:26.854376+00:00`
- Price records: `672`
- Market context records: `8561`
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

- `news_risk_high->unknown_24h` score `5076.7711` n `61` status `ready` deltaP `40.4912` edge `422.8364` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7236` n `64` status `ready` deltaP `20.3506` edge `0.401` maxDD `-3.4427`
- `market_context_high->crypto_alt_4h` score `2.065` n `62` status `ready` deltaP `14.4276` edge `0.1716` maxDD `-5.323`
- `news_risk_high->index_4h` score `2.0449` n `64` status `ready` deltaP `16.9588` edge `0.0764` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7505` n `64` status `ready` deltaP `16.4016` edge `0.0842` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1091` n `64` status `ready` deltaP `7.5076` edge `0.1697` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7513` n `64` status `ready` deltaP `14.0244` edge `0.142` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.489` n `64` status `ready` deltaP `8.561` edge `0.0583` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3688` n `64` status `ready` deltaP `7.064` edge `0.0514` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0823` n `64` status `ready` deltaP `5.1366` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0546` n `64` status `ready` deltaP `11.7759` edge `0.0218` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0075` n `64` status `ready` deltaP `3.6209` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0372` n `64` status `ready` deltaP `1.7149` edge `0.0314` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1096` n `64` status `ready` deltaP `3.5554` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.1136` n `62` status `ready` deltaP `8.6005` edge `0.0128` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.2825` n `62` status `ready` deltaP `2.062` edge `0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.32` n `62` status `ready` deltaP `4.0081` edge `-0.0052` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4878` n `62` status `ready` deltaP `-2.4773` edge `0.0167` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7716` n `62` status `ready` deltaP `0.6471` edge `-0.0157` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9505` n `62` status `ready` deltaP `-2.6946` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
