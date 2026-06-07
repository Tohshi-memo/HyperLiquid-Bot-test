# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T01:52:22.671290+00:00`
- Price records: `672`
- Market context records: `3133`
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

- `market_context_high->commodity_24h` score `14.2862` n `106` status `ready` deltaP `47.5858` edge `0.9161` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.7789` n `106` status `ready` deltaP `21.1314` edge `0.8895` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7651` n `106` status `ready` deltaP `10.0727` edge `2.3106` maxDD `-71.142`
- `market_context_high->index_24h` score `6.4595` n `106` status `ready` deltaP `30.703` edge `0.8789` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3317` n `106` status `ready` deltaP `10.8556` edge `1.3246` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0945` n `136` status `ready` deltaP `20.4717` edge `0.1672` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1079` n `146` status `ready` deltaP `3.6831` edge `0.0267` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.4226` n `146` status `ready` deltaP `5.7563` edge `0.1204` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4657` n `106` status `ready` deltaP `5.3328` edge `-0.0016` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.479` n `146` status `ready` deltaP `4.0009` edge `0.0182` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8363` n `146` status `ready` deltaP `3.0391` edge `0.0211` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9717` n `146` status `ready` deltaP `3.076` edge `0.0812` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1586` n `146` status `ready` deltaP `-11.2173` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.3071` n `136` status `ready` deltaP `10.4734` edge `0.0535` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4975` n `136` status `ready` deltaP `-14.3203` edge `-0.0088` maxDD `-1.3508`
- `market_context_high->metal_1h` score `-1.9989` n `146` status `ready` deltaP `-3.7056` edge `-0.0025` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.1605` n `136` status `ready` deltaP `4.1965` edge `0.0142` maxDD `-14.7778`
- `market_context_high->crypto_alt_4h` score `-2.6461` n `136` status `ready` deltaP `17.8264` edge `0.3464` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.029` n `146` status `ready` deltaP `2.3583` edge `-0.0655` maxDD `-14.2111`
- `market_context_high->equity_4h` score `-3.2849` n `136` status `ready` deltaP `11.2087` edge `0.0347` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
