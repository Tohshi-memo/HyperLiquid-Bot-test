# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T14:37:23.362861+00:00`
- Price records: `672`
- Market context records: `3187`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9761`

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

- `market_context_high->commodity_24h` score `13.8097` n `105` status `ready` deltaP `47.4206` edge `0.8775` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9498` n `105` status `ready` deltaP `19.7768` edge `0.936` maxDD `-3.7624`
- `market_context_high->crypto_alt_24h` score `11.5875` n `105` status `ready` deltaP `14.742` edge `2.3849` maxDD `-71.142`
- `market_context_high->index_24h` score `6.2658` n `105` status `ready` deltaP `30.2777` edge `0.8569` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5484` n `105` status `ready` deltaP `12.8919` edge `1.3388` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.188` n `138` status `ready` deltaP `20.6345` edge `0.1739` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.6401` n `105` status `ready` deltaP `11.1459` edge `0.0018` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.5444` n `138` status `ready` deltaP `11.7135` edge `0.1895` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3876` n `140` status `ready` deltaP `6.4286` edge `0.0317` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3392` n `140` status `ready` deltaP `6.4628` edge `0.0197` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.5265` n `140` status `ready` deltaP `5.633` edge `0.1079` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.7052` n `138` status `ready` deltaP `17.7735` edge `0.082` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0882` n `140` status `ready` deltaP `3.1309` edge `0.0659` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2921` n `140` status `ready` deltaP `4.1702` edge `0.0131` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3184` n `138` status `ready` deltaP `-11.0618` edge `-0.0068` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6359` n `140` status `ready` deltaP `-9.367` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.1253` n `140` status `ready` deltaP `-4.4012` edge `-0.0084` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.3868` n `138` status `ready` deltaP `16.3927` edge `0.3892` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1099` n `140` status `ready` deltaP `2.6519` edge `-0.0742` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.7413` n `138` status `ready` deltaP `9.6766` edge `0.2482` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
