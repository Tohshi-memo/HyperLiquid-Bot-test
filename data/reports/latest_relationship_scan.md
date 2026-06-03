# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T13:07:27.803520+00:00`
- Price records: `672`
- Market context records: `2766`
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

- `market_context_high->unknown_24h` score `5.054` n `132` status `ready` deltaP `11.1584` edge `0.3796` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `3.2393` n `132` status `ready` deltaP `5.6029` edge `0.7273` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `1.0149` n `143` status `ready` deltaP `6.7063` edge `0.1452` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.0718` n `132` status `ready` deltaP `8.7436` edge `0.2603` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.002` n `143` status `ready` deltaP `10.2465` edge `0.0161` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0201` n `143` status `ready` deltaP `4.0964` edge `0.0441` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1807` n `143` status `ready` deltaP `3.0506` edge `0.0059` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5722` n `143` status `ready` deltaP `-0.9463` edge `0.003` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6083` n `143` status `ready` deltaP `0.2021` edge `-0.004` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7108` n `143` status `ready` deltaP `5.5463` edge `0.0479` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7614` n `143` status `ready` deltaP `-0.8009` edge `-0.0077` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9923` n `143` status `ready` deltaP `3.4976` edge `0.0364` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.2124` n `143` status `ready` deltaP `-3.7864` edge `0.0075` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2441` n `143` status `ready` deltaP `-4.86` edge `0.0066` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.296` n `143` status `ready` deltaP `14.3815` edge `0.2302` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.3106` n `132` status `ready` deltaP `-0.3945` edge `-0.0194` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6224` n `143` status `ready` deltaP `-0.1631` edge `-0.0149` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.1681` n `143` status `ready` deltaP `-1.0969` edge `-0.0354` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4529` n `143` status `ready` deltaP `-2.6437` edge `-0.0418` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.665` n `143` status `ready` deltaP `4.9229` edge `0.1161` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
