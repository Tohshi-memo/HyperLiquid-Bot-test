# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T11:22:28.619424+00:00`
- Price records: `672`
- Market context records: `7770`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `6.5032` n `132` status `ready` deltaP `25.6678` edge `0.505` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.1734` n `133` status `ready` deltaP `11.709` edge `0.2288` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9398` n `133` status `ready` deltaP `12.7088` edge `0.0377` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5993` n `132` status `ready` deltaP `22.0489` edge `0.0386` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.4766` n `133` status `ready` deltaP `7.8958` edge `0.073` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `0.4419` n `133` status `ready` deltaP `12.3647` edge `0.1262` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.3586` n `133` status `ready` deltaP `1.5107` edge `0.2272` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3398` n `133` status `ready` deltaP `8.4943` edge `0.0147` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2172` n `133` status `ready` deltaP `6.8276` edge `0.0843` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.1418` n `133` status `ready` deltaP `6.0104` edge `0.0311` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1184` n `133` status `ready` deltaP `4.2783` edge `0.0246` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0583` n `133` status `ready` deltaP `4.7461` edge `0.0094` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2916` n `133` status `ready` deltaP `10.0998` edge `0.0411` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4243` n `133` status `ready` deltaP `0.5239` edge `-0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9226` n `133` status `ready` deltaP `0.8183` edge `0.018` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.0834` n `132` status `ready` deltaP `8.1248` edge `0.0139` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4658` n `133` status `ready` deltaP `-3.703` edge `-0.0004` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.7024` n `133` status `ready` deltaP `-0.6912` edge `0.0682` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.9761` n `132` status `ready` deltaP `-13.2272` edge `0.0451` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2968` n `133` status `ready` deltaP `-1.7232` edge `-0.1209` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
