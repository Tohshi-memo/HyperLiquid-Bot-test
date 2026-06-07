# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T15:07:22.186775+00:00`
- Price records: `672`
- Market context records: `3189`
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

- `market_context_high->commodity_24h` score `13.7317` n `105` status `ready` deltaP `47.4206` edge `0.871` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.6603` n `105` status `ready` deltaP `14.5684` edge `2.3954` maxDD `-71.142`
- `market_context_high->unknown_24h` score `10.6963` n `105` status `ready` deltaP `19.1717` edge `0.8894` maxDD `-8.0685`
- `market_context_high->index_24h` score `6.2775` n `105` status `ready` deltaP `30.2777` edge `0.8584` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6688` n `105` status `ready` deltaP `13.497` edge `1.3502` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.188` n `138` status `ready` deltaP `20.6345` edge `0.1739` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.6921` n `105` status `ready` deltaP `11.7509` edge `0.0021` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6238` n `138` status `ready` deltaP `12.2857` edge `0.1923` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3541` n `139` status `ready` deltaP `6.1151` edge `0.031` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3558` n `139` status `ready` deltaP `6.2939` edge `0.0187` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.5631` n `139` status `ready` deltaP `5.3041` edge `0.1054` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.7045` n `138` status `ready` deltaP `17.7735` edge `0.0821` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.1228` n `139` status `ready` deltaP `2.7506` edge `0.064` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.2942` n `138` status `ready` deltaP `-10.642` edge `-0.0065` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.3332` n `139` status `ready` deltaP `3.8362` edge `0.0119` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.6121` n `139` status `ready` deltaP `-9.0844` edge `-0.0051` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0994` n `139` status `ready` deltaP `-4.0775` edge `-0.0084` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.3782` n `138` status `ready` deltaP `16.3927` edge `0.3903` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0842` n `139` status `ready` deltaP `2.7636` edge `-0.0728` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.7304` n `138` status `ready` deltaP `9.6766` edge `0.2496` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
