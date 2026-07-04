# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T09:07:28.105204+00:00`
- Price records: `672`
- Market context records: `5647`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.6232` n `179` status `ready` deltaP `14.3389` edge `0.6309` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.1589` n `179` status `ready` deltaP `20.3154` edge `0.0607` maxDD `-1.6317`
- `market_context_high->crypto_major_4h` score `0.6494` n `237` status `ready` deltaP `10.0899` edge `0.2161` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4515` n `237` status `ready` deltaP `7.229` edge `0.1533` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.1606` n `237` status `ready` deltaP `5.7644` edge `0.1331` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2735` n `239` status `ready` deltaP `1.7331` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3637` n `239` status `ready` deltaP `5.4876` edge `0.0338` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5671` n `239` status `ready` deltaP `-0.7773` edge `0.0` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6435` n `239` status `ready` deltaP `1.2496` edge `0.0342` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.699` n `239` status `ready` deltaP `3.6448` edge `0.042` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.956` n `239` status `ready` deltaP `0.2361` edge `0.0056` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.049` n `239` status `ready` deltaP `-0.8349` edge `-0.0053` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.301` n `237` status `ready` deltaP `1.5231` edge `0.0064` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0221` n `237` status `ready` deltaP `-1.5366` edge `0.0089` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.2945` n `179` status `ready` deltaP `10.533` edge `0.0343` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.052` n `237` status `ready` deltaP `-14.674` edge `-0.0551` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8044` n `237` status `ready` deltaP `-2.1875` edge `-0.0349` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5087` n `179` status `ready` deltaP `4.1851` edge `0.0504` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3325` n `179` status `ready` deltaP `-12.0713` edge `-0.2517` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.0732` n `179` status `ready` deltaP `-16.881` edge `-0.116` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
