# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T02:07:13.602133+00:00`
- Price records: `672`
- Market context records: `1176`
- Flow alert records: `5289`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `20.2902` n `144` status `ready` deltaP `45.4861` edge `1.5008` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.9446` n `144` status `ready` deltaP `22.2223` edge `0.8822` maxDD `-15.1306`
- `market_context_high->equity_24h` score `6.6099` n `144` status `ready` deltaP `19.4444` edge `0.5305` maxDD `-7.0775`
- `market_context_high->metal_24h` score `5.5748` n `144` status `ready` deltaP `-2.7778` edge `0.6498` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.266` n `144` status `ready` deltaP `19.0972` edge `0.3673` maxDD `-3.4627`
- `market_context_high->equity_4h` score `2.6726` n `152` status `ready` deltaP `13.9121` edge `0.1963` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2636` n `152` status `ready` deltaP `10.0208` edge `0.1068` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5918` n `152` status `ready` deltaP `8.4462` edge `0.0247` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4024` n `152` status `ready` deltaP `3.51` edge `0.0479` maxDD `-1.3546`
- `market_context_high->unknown_4h` score `0.2222` n `152` status `ready` deltaP `6.3703` edge `0.0977` maxDD `-6.7322`
- `market_context_high->fx_1h` score `0.1275` n `152` status `ready` deltaP `8.399` edge `0.0002` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0972` n `152` status `ready` deltaP `8.352` edge `0.1489` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0633` n `152` status `ready` deltaP `5.9486` edge `0.0288` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.322` n `152` status `ready` deltaP `6.6302` edge `-0.01` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.4843` n `152` status `ready` deltaP `1.6979` edge `0.0326` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8557` n `152` status `ready` deltaP `-3.648` edge `-0.0046` maxDD `-3.7959`
- `market_context_high->unknown_24h` score `-1.0036` n `144` status `ready` deltaP `4.3403` edge `0.1604` maxDD `-10.1706`
- `market_context_high->fx_4h` score `-1.0396` n `152` status `ready` deltaP `-4.2201` edge `-0.0055` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3602` n `152` status `ready` deltaP `3.7067` edge `0.0974` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.8796` n `152` status `ready` deltaP `5.1188` edge `-0.0797` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
