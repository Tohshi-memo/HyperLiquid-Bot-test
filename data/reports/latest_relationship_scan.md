# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T09:52:23.847515+00:00`
- Price records: `672`
- Market context records: `2752`
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

- `market_context_high->unknown_24h` score `6.8603` n `122` status `ready` deltaP `14.6716` edge `0.5067` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `4.9806` n `122` status `ready` deltaP `10.2601` edge `0.9195` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.8821` n `143` status `ready` deltaP `6.0965` edge `0.1382` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1736` n `143` status `ready` deltaP `11.1611` edge `0.032` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1388` n `143` status `ready` deltaP `3.3479` edge `0.0392` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1542` n `143` status `ready` deltaP `3.2003` edge `0.0083` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5602` n `143` status `ready` deltaP `-0.7966` edge `0.003` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.643` n `143` status `ready` deltaP `5.9954` edge `0.0536` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.6944` n `143` status `ready` deltaP `-0.3518` edge `-0.0021` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.7088` n `143` status `ready` deltaP `-0.8458` edge `-0.0099` maxDD `-4.3601`
- `market_context_high->commodity_24h` score `-0.7167` n `122` status `ready` deltaP `6.0735` edge `0.177` maxDD `-12.4171`
- `market_context_high->crypto_major_1h` score `-0.9277` n `143` status `ready` deltaP `3.9467` edge `0.0417` maxDD `-9.622`
- `market_context_high->crypto_alt_4h` score `-1.0856` n `143` status `ready` deltaP `15.6011` edge `0.2396` maxDD `-28.7261`
- `market_context_high->equity_1h` score `-1.162` n `143` status `ready` deltaP `-3.7864` edge `0.0117` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2283` n `143` status `ready` deltaP `-4.7075` edge `0.0069` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2338` n `122` status `ready` deltaP `0.2362` edge `-0.0172` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6892` n `143` status `ready` deltaP `-0.7728` edge `-0.0194` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.9615` n `143` status `ready` deltaP `-0.9444` edge `-0.0192` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3846` n `143` status `ready` deltaP `-2.1864` edge `-0.0361` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4847` n `143` status `ready` deltaP `5.9899` edge `0.1321` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
