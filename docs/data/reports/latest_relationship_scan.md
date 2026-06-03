# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T11:22:21.567690+00:00`
- Price records: `672`
- Market context records: `2759`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `5.8338` n `128` status `ready` deltaP `12.7604` edge `0.4339` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `4.1007` n `128` status `ready` deltaP `7.3785` edge `0.8259` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9739` n `143` status `ready` deltaP `6.5539` edge `0.1428` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.092` n `143` status `ready` deltaP `10.5514` edge `0.0256` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1124` n `143` status `ready` deltaP `3.6473` edge `0.0394` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1441` n `143` status `ready` deltaP `3.35` edge `0.0086` maxDD `-1.2855`
- `market_context_high->commodity_24h` score `-0.2073` n `128` status `ready` deltaP `7.7256` edge `0.2313` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5853` n `143` status `ready` deltaP `-1.096` edge `0.0029` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6636` n `143` status `ready` deltaP `-0.3967` edge `-0.0071` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6921` n `143` status `ready` deltaP `5.696` edge `0.0493` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7715` n `143` status `ready` deltaP `-0.9506` edge `-0.008` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9728` n `143` status `ready` deltaP `3.4976` edge `0.0389` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1524` n `143` status `ready` deltaP `-3.6367` edge `0.0115` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2161` n `143` status `ready` deltaP `-4.5551` edge `0.0069` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.2256` n `143` status `ready` deltaP `14.9913` edge `0.232` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.2345` n `128` status `ready` deltaP `0.3472` edge `-0.018` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.7134` n `143` status `ready` deltaP `-0.7728` edge `-0.0225` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0335` n `143` status `ready` deltaP `-0.9444` edge `-0.0252` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.43` n `143` status `ready` deltaP `-2.3389` edge `-0.0409` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6078` n `143` status `ready` deltaP `5.2277` edge `0.1214` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
