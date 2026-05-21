# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T14:57:01.171423+00:00`
- Price records: `672`
- Market context records: `1433`
- Flow alert records: `6039`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8796`

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

- `market_context_high->crypto_alt_24h` score `12.0461` n `154` status `ready` deltaP `28.7811` edge `1.0136` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.9387` n `154` status `ready` deltaP `12.8562` edge `1.0759` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.702` n `154` status `ready` deltaP `27.3539` edge `0.906` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9669` n `154` status `ready` deltaP `19.3813` edge `0.31` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.1071` n `154` status `ready` deltaP `12.5271` edge `0.4081` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0335` n `206` status `ready` deltaP `5.9274` edge `0.1296` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1248` n `154` status `ready` deltaP `9.7065` edge `0.0506` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1979` n `218` status `ready` deltaP `3.0023` edge `0.01` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3095` n `218` status `ready` deltaP `1.8334` edge `0.022` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.6516` n `206` status `ready` deltaP `0.0296` edge `0.0544` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.6904` n `218` status `ready` deltaP `-0.7581` edge `0.009` maxDD `-2.252`
- `market_context_high->fx_1h` score `-0.7542` n `218` status `ready` deltaP `0.5068` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.761` n `218` status `ready` deltaP `1.4627` edge `0.0292` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9202` n `218` status `ready` deltaP `3.9156` edge `-0.0105` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.1583` n `206` status `ready` deltaP `8.285` edge `0.1802` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3604` n `206` status `ready` deltaP `4.8026` edge `0.1255` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5991` n `206` status `ready` deltaP `-4.0197` edge `-0.0094` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.737` n `218` status `ready` deltaP `-1.2992` edge `-0.0004` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.789` n `206` status `ready` deltaP `4.9387` edge `0.0069` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.1257` n `206` status `ready` deltaP `-10.431` edge `-0.0196` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
