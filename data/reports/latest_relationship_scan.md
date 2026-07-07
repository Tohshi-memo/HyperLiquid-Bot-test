# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T07:07:27.506389+00:00`
- Price records: `672`
- Market context records: `5957`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `6.9529` n `30` status `ready` deltaP `63.5417` edge `0.1558` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.3903` n `30` status `ready` deltaP `38.75` edge `0.2114` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8698` n `30` status `ready` deltaP `40.1524` edge `0.0594` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0945` n `30` status `ready` deltaP `25.2794` edge `0.0199` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4378` n `226` status `ready` deltaP `9.1436` edge `0.1683` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8559` n `30` status `ready` deltaP `10.3393` edge `0.0875` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2216` n `30` status `ready` deltaP `5.4691` edge `0.0381` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1788` n `30` status `ready` deltaP `6.9791` edge `0.0177` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3312` n `238` status `ready` deltaP `5.0521` edge `0.0367` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.344` n `30` status `ready` deltaP `2.5848` edge `-0.0247` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4661` n `238` status `ready` deltaP `2.6128` edge `0.0027` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.5256` n `213` status `ready` deltaP `20.6157` edge `0.3028` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.5939` n `238` status `ready` deltaP `-2.9122` edge `-0.001` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6243` n `238` status `ready` deltaP `0.9611` edge `0.0049` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6306` n `238` status `ready` deltaP `-0.1547` edge `-0.0004` maxDD `-0.756`
- `market_context_high->crypto_major_1h` score `-1.0943` n `238` status `ready` deltaP `2.048` edge `0.0228` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1` n `238` status `ready` deltaP `2.1637` edge `0.0198` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.1007` n `30` status `ready` deltaP `-10.2994` edge `-0.021` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.5672` n `226` status `ready` deltaP `-1.9183` edge `-0.0249` maxDD `-5.725`
- `market_context_high->commodity_4h` score `-1.6125` n `226` status `ready` deltaP `-3.2094` edge `-0.014` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
