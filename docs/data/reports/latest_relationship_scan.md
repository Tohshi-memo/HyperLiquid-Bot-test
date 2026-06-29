# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T11:07:29.507715+00:00`
- Price records: `672`
- Market context records: `5138`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5588`

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

- `market_context_high->unknown_24h` score `27.6094` n `65` status `ready` deltaP `29.7062` edge `2.137` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `7.1409` n `122` status `ready` deltaP `20.0545` edge `0.5636` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.9194` n `134` status `ready` deltaP `9.5496` edge `0.5771` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.0551` n `122` status `ready` deltaP `15.4763` edge `0.478` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.6428` n `122` status `ready` deltaP `13.3221` edge `0.444` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.3047` n `65` status `ready` deltaP `18.3333` edge `0.1392` maxDD `-4.1987`
- `market_context_high->crypto_alt_1h` score `0.8519` n `134` status `ready` deltaP `6.1265` edge `0.1263` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.8395` n `122` status `ready` deltaP `8.749` edge `0.1755` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.8373` n `134` status `ready` deltaP `8.524` edge `0.1375` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.7289` n `134` status `ready` deltaP `8.0637` edge `0.0663` maxDD `-2.745`
- `market_context_high->index_1h` score `0.039` n `134` status `ready` deltaP `5.8227` edge `0.0148` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0876` n `134` status `ready` deltaP `4.6407` edge `0.0144` maxDD `-1.8592`
- `market_context_high->metal_24h` score `-0.2486` n `65` status `ready` deltaP `-0.2297` edge `0.1818` maxDD `-11.4122`
- `market_context_high->index_4h` score `-0.3837` n `122` status `ready` deltaP `6.4599` edge `0.0367` maxDD `-2.9391`
- `market_context_high->crypto_alt_24h` score `-0.4268` n `65` status `ready` deltaP `16.8135` edge `0.5345` maxDD `-50.438`
- `market_context_high->commodity_1h` score `-0.5767` n `134` status `ready` deltaP `0.601` edge `-0.001` maxDD `-2.155`
- `market_context_high->fx_1h` score `-0.6116` n `134` status `ready` deltaP `-1.9372` edge `-0.0014` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.7009` n `122` status `ready` deltaP `1.6743` edge `0.047` maxDD `-5.1748`
- `market_context_high->fx_4h` score `-0.973` n `122` status `ready` deltaP `-2.7064` edge `0.0006` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.0004` n `65` status `ready` deltaP `1.7629` edge `-0.0036` maxDD `-0.9885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
