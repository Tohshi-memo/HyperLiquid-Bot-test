# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T03:07:19.718010+00:00`
- Price records: `672`
- Market context records: `2724`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `11.2375` n `111` status `ready` deltaP `16.3523` edge `1.1768` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7187` n `111` status `ready` deltaP `17.652` edge `0.6417` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.0021` n `111` status `ready` deltaP `6.5175` edge `0.8413` maxDD `-44.169`
- `market_context_high->unknown_4h` score `0.9923` n `143` status `ready` deltaP `6.8587` edge `0.1423` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1199` n `143` status `ready` deltaP `10.3989` edge `0.0302` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1464` n `143` status `ready` deltaP `3.35` edge `0.0083` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1951` n `143` status `ready` deltaP `2.7491` edge `0.0385` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.4223` n `143` status `ready` deltaP `16.3633` edge `0.2898` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.4943` n `143` status `ready` deltaP `-0.0481` edge `0.0035` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5055` n `143` status `ready` deltaP `1.3997` edge `0.0012` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5299` n `143` status `ready` deltaP `6.2948` edge `0.0661` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7395` n `143` status `ready` deltaP `-1.25` edge `-0.0019` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9198` n `143` status `ready` deltaP `3.6473` edge `0.0447` maxDD `-9.622`
- `market_context_high->fx_24h` score `-0.9733` n `111` status `ready` deltaP `2.4869` edge `-0.0105` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-1.0165` n `143` status `ready` deltaP `-2.421` edge `0.0093` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.1764` n `143` status `ready` deltaP `-3.7864` edge `0.0105` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3213` n `143` status `ready` deltaP `1.8186` edge `0.0105` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.5558` n `111` status `ready` deltaP `2.928` edge `0.0904` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0065` n `143` status `ready` deltaP `-0.4871` edge `-0.026` maxDD `-5.7037`
- `market_context_high->index_24h` score `-2.2586` n `111` status `ready` deltaP `-1.1918` edge `-0.0822` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
