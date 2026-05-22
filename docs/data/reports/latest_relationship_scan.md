# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T23:52:14.023717+00:00`
- Price records: `672`
- Market context records: `1576`
- Flow alert records: `6449`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `13.2807` n `182` status `ready` deltaP `27.1157` edge `1.026` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.4858` n `182` status `ready` deltaP `26.9974` edge `0.9788` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.9465` n `182` status `ready` deltaP `26.7399` edge `0.7638` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0152` n `182` status `ready` deltaP `20.7799` edge `0.3047` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8977` n `182` status `ready` deltaP `17.7141` edge `0.4394` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8508` n `199` status `ready` deltaP `7.9873` edge `0.1271` maxDD `-5.0894`
- `market_context_high->fx_24h` score `0.222` n `182` status `ready` deltaP `12.0154` edge `0.0433` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.2099` n `199` status `ready` deltaP `13.2545` edge `0.2705` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0318` n `199` status `ready` deltaP `9.2796` edge `0.2131` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2802` n `199` status `ready` deltaP `1.2668` edge `0.058` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5815` n `199` status `ready` deltaP `0.7636` edge `0.0273` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6257` n `199` status `ready` deltaP `-1.9942` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6266` n `199` status `ready` deltaP `1.2232` edge `0.0028` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7088` n `199` status `ready` deltaP `5.5969` edge `0.0054` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7593` n `199` status `ready` deltaP `-0.6469` edge `-0.0009` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8506` n `199` status `ready` deltaP `-0.1444` edge `0.0276` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.1976` n `199` status `ready` deltaP `-2.6106` edge `0.0265` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3078` n `199` status `ready` deltaP `10.516` edge `0.0901` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3791` n `199` status `ready` deltaP `-10.3973` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1555` n `199` status `ready` deltaP `-14.2427` edge `-0.1033` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
