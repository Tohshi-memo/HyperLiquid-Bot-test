# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T09:07:27.109644+00:00`
- Price records: `672`
- Market context records: `2749`
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

- `market_context_high->unknown_24h` score `7.2423` n `119` status `ready` deltaP `15.0064` edge `0.5363` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `5.4848` n `119` status `ready` deltaP `11.8099` edge `0.9738` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9183` n `143` status `ready` deltaP `6.249` edge `0.1402` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1815` n `143` status `ready` deltaP `11.3136` edge `0.032` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1412` n `143` status `ready` deltaP `3.3479` edge `0.039` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.155` n `143` status `ready` deltaP `3.2003` edge `0.0082` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5338` n `143` status `ready` deltaP `-0.4972` edge `0.0032` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6461` n `143` status `ready` deltaP `5.9954` edge `0.0532` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7045` n `143` status `ready` deltaP `-0.5015` edge `-0.0024` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.7088` n `143` status `ready` deltaP `-0.8458` edge `-0.0099` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.9471` n `143` status `ready` deltaP `3.6473` edge `0.0412` maxDD `-9.622`
- `market_context_high->commodity_24h` score `-1.0305` n `119` status `ready` deltaP `5.1849` edge `0.1427` maxDD `-12.4171`
- `market_context_high->crypto_alt_4h` score `-1.0688` n `143` status `ready` deltaP `15.6011` edge `0.241` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2015` n `143` status `ready` deltaP `-4.4027` edge `0.0071` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.2184` n `143` status `ready` deltaP `-4.2355` edge `0.01` maxDD `-2.6634`
- `market_context_high->fx_24h` score `-1.2393` n `119` status `ready` deltaP `0.1371` edge `-0.017` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.654` n `143` status `ready` deltaP `-0.6204` edge `-0.0159` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.9833` n `143` status `ready` deltaP `-1.0969` edge `-0.02` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3737` n `143` status `ready` deltaP `-2.1864` edge `-0.0347` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4571` n `143` status `ready` deltaP `6.2948` edge `0.1336` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
