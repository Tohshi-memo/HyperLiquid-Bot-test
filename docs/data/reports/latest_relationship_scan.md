# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T03:37:25.348872+00:00`
- Price records: `672`
- Market context records: `2726`
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

- `market_context_high->crypto_alt_24h` score `11.3335` n `111` status `ready` deltaP `16.3523` edge `1.1848` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7031` n `111` status `ready` deltaP `17.652` edge `0.6404` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.1277` n `111` status `ready` deltaP `6.5175` edge `0.8574` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.0599` n `143` status `ready` deltaP `7.1636` edge `0.1459` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0877` n `143` status `ready` deltaP `10.0941` edge `0.0281` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.148` n `143` status `ready` deltaP `3.35` edge `0.0081` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1651` n `143` status `ready` deltaP `2.8988` edge `0.04` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.4415` n `143` status `ready` deltaP `16.3633` edge `0.2882` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5075` n `143` status `ready` deltaP `-0.1978` edge `0.0034` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.514` n `143` status `ready` deltaP `1.25` edge `0.0011` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.54` n `143` status `ready` deltaP `6.1451` edge `0.0658` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.766` n `143` status `ready` deltaP `-1.5494` edge `-0.0033` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9151` n `143` status `ready` deltaP `3.6473` edge `0.0453` maxDD `-9.622`
- `market_context_high->fx_24h` score `-1.0047` n `111` status `ready` deltaP `2.1397` edge `-0.0108` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-1.0165` n `143` status `ready` deltaP `-2.421` edge `0.0093` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.2088` n `143` status `ready` deltaP `-4.0858` edge `0.0098` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3228` n `143` status `ready` deltaP `1.8186` edge `0.0103` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.5965` n `111` status `ready` deltaP `2.5807` edge `0.0875` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0489` n `143` status `ready` deltaP `-0.792` edge `-0.0275` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3086` n `143` status `ready` deltaP `-1.7291` edge `-0.0294` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
