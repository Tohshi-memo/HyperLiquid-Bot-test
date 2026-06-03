# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T02:52:24.838052+00:00`
- Price records: `672`
- Market context records: `2723`
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

- `market_context_high->crypto_alt_24h` score `11.2003` n `111` status `ready` deltaP `16.3523` edge `1.1737` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7199` n `111` status `ready` deltaP `17.652` edge `0.6418` maxDD `-1.6255`
- `market_context_high->unknown_4h` score `0.9741` n `143` status `ready` deltaP `6.7063` edge `0.1418` maxDD `-3.7602`
- `market_context_high->crypto_major_24h` score `0.9451` n `111` status `ready` deltaP `6.5175` edge `0.834` maxDD `-44.169`
- `market_context_high->index_4h` score `0.1349` n `143` status `ready` deltaP `10.5514` edge `0.0311` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1456` n `143` status `ready` deltaP `3.35` edge `0.0084` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1915` n `143` status `ready` deltaP `2.7491` edge `0.0388` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.4139` n `143` status `ready` deltaP `16.3633` edge `0.2905` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.4823` n `143` status `ready` deltaP `0.1016` edge `0.0035` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5055` n `143` status `ready` deltaP `1.3997` edge `0.0012` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5315` n `143` status `ready` deltaP `6.2948` edge `0.0659` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7271` n `143` status `ready` deltaP `-1.1003` edge `-0.0013` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9214` n `143` status `ready` deltaP `3.6473` edge `0.0445` maxDD `-9.622`
- `market_context_high->fx_24h` score `-0.957` n `111` status `ready` deltaP `2.6605` edge `-0.0103` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-1.0153` n `143` status `ready` deltaP `-2.421` edge `0.0094` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.1764` n `143` status `ready` deltaP `-3.7864` edge `0.0105` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3181` n `143` status `ready` deltaP `1.8186` edge `0.0109` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.5304` n `111` status `ready` deltaP `3.1016` edge `0.0925` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0017` n `143` status `ready` deltaP `-0.4871` edge `-0.0256` maxDD `-5.7037`
- `market_context_high->index_24h` score `-2.1944` n `111` status `ready` deltaP `-1.0182` edge `-0.078` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
