# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T01:22:22.787650+00:00`
- Price records: `672`
- Market context records: `3131`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7125`

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

- `market_context_high->commodity_24h` score `14.2502` n `106` status `ready` deltaP `47.5858` edge `0.9131` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.7254` n `106` status `ready` deltaP `20.9578` edge `0.8862` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7729` n `106` status `ready` deltaP `10.0727` edge `2.3116` maxDD `-71.142`
- `market_context_high->index_24h` score `6.4595` n `106` status `ready` deltaP `30.703` edge `0.8789` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3387` n `106` status `ready` deltaP `10.8556` edge `1.3255` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0886` n `134` status `ready` deltaP `20.1424` edge `0.1689` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0959` n `146` status `ready` deltaP `3.5334` edge `0.0267` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3665` n `146` status `ready` deltaP `6.0557` edge `0.1256` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4587` n `146` status `ready` deltaP `4.3003` edge `0.0188` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.4657` n `106` status `ready` deltaP `5.3328` edge `-0.0016` maxDD `-0.4876`
- `market_context_high->equity_1h` score `-0.8269` n `146` status `ready` deltaP `3.0391` edge `0.0223` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9335` n `146` status `ready` deltaP `3.2257` edge `0.0851` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1594` n `146` status `ready` deltaP `-11.2173` edge `-0.0056` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.3028` n `134` status `ready` deltaP `10.6161` edge `0.0531` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.5171` n `134` status `ready` deltaP `-14.7252` edge `-0.0088` maxDD `-1.3359`
- `market_context_high->metal_1h` score `-1.9665` n `146` status `ready` deltaP `-3.4062` edge `-0.0018` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.215` n `134` status `ready` deltaP `3.7564` edge `0.0126` maxDD `-14.7778`
- `market_context_high->crypto_alt_4h` score `-2.9092` n `134` status `ready` deltaP `17.1459` edge `0.3172` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.9942` n `146` status `ready` deltaP `2.508` edge `-0.0636` maxDD `-14.2111`
- `market_context_high->equity_4h` score `-3.3968` n `134` status `ready` deltaP `10.6161` edge `0.0243` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
