# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T17:37:27.049326+00:00`
- Price records: `672`
- Market context records: `6002`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11142`

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

- `news_risk_high->fx_24h` score `7.5755` n `30` status `ready` deltaP `68.9236` edge `0.1718` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1701` n `30` status `ready` deltaP `43.2012` edge `0.0641` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.973` n `30` status `ready` deltaP `31.4584` edge `0.1419` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.231` n `30` status `ready` deltaP `26.7764` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2323` n `222` status `ready` deltaP `7.7895` edge `0.1602` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7374` n `30` status `ready` deltaP `9.7405` edge `0.0763` maxDD `-2.0691`
- `market_context_high->equity_24h` score `0.2987` n `195` status `ready` deltaP `23.9103` edge `0.3931` maxDD `-30.542`
- `news_risk_high->crypto_alt_1h` score `0.1374` n `30` status `ready` deltaP `5.02` edge `0.0303` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1218` n `30` status `ready` deltaP `9.2361` edge `0.0412` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4126` n `30` status `ready` deltaP `1.5369` edge `-0.0265` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.5009` n `222` status `ready` deltaP `2.2577` edge `0.0006` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5651` n `222` status `ready` deltaP `-0.4491` edge `0.0023` maxDD `-0.7117`
- `market_context_high->equity_1h` score `-0.5676` n `222` status `ready` deltaP `2.2617` edge `0.025` maxDD `-4.3608`
- `market_context_high->fx_1h` score `-0.6754` n `222` status `ready` deltaP `-0.611` edge `-0.0014` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0392` n `30` status `ready` deltaP `-9.4012` edge `-0.0191` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0812` n `222` status `ready` deltaP `-0.6935` edge `-0.0044` maxDD `-3.0339`
- `market_context_high->index_4h` score `-1.1581` n `222` status `ready` deltaP `0.4436` edge `0.0162` maxDD `-3.0774`
- `market_context_high->crypto_major_1h` score `-1.2103` n `222` status `ready` deltaP `1.8126` edge `0.0095` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2559` n `222` status `ready` deltaP `1.056` edge `0.0072` maxDD `-9.3536`
- `market_context_high->index_1h` score `-1.3162` n `222` status `ready` deltaP `-3.0048` edge `0.0017` maxDD `-1.3078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
