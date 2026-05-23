# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T00:22:14.188935+00:00`
- Price records: `672`
- Market context records: `1578`
- Flow alert records: `6455`
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

- `market_context_high->metal_24h` score `13.3624` n `182` status `ready` deltaP `27.4629` edge `1.0305` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6094` n `182` status `ready` deltaP `26.9974` edge `0.9891` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.0461` n `182` status `ready` deltaP `26.7399` edge `0.7721` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0387` n `182` status `ready` deltaP `20.9535` edge `0.3055` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0371` n `182` status `ready` deltaP `18.0613` edge `0.4487` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.87` n `199` status `ready` deltaP `7.9873` edge `0.1287` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2263` n `199` status `ready` deltaP `13.2545` edge `0.2726` maxDD `-19.5565`
- `market_context_high->fx_24h` score `0.187` n `182` status `ready` deltaP `11.6682` edge `0.0427` maxDD `-1.3925`
- `market_context_high->crypto_major_4h` score `0.0451` n `199` status `ready` deltaP `9.2796` edge `0.2148` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2646` n `199` status `ready` deltaP `1.2668` edge `0.06` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5719` n `199` status `ready` deltaP `0.7636` edge `0.0281` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.5979` n `199` status `ready` deltaP `1.5226` edge `0.0032` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6257` n `199` status `ready` deltaP `-1.9942` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6987` n `199` status `ready` deltaP `5.7466` edge `0.0057` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7624` n `199` status `ready` deltaP `-0.6469` edge `-0.0013` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8295` n `199` status `ready` deltaP `0.0053` edge `0.0293` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.177` n `199` status `ready` deltaP `-2.4582` edge `0.0272` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3042` n `199` status `ready` deltaP `10.516` edge `0.0904` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3783` n `199` status `ready` deltaP `-10.3973` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1931` n `199` status `ready` deltaP `-14.5476` edge `-0.1061` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
