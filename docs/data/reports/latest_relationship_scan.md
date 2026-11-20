# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T11:52:40.670390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2612`

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

- `market_context_high->unknown_1h` score `11045.7377` n `117` status `ready` deltaP `1.9129` edge `920.4852` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7456.1117` n `108` status `ready` deltaP `0.5194` edge `621.3676` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4637` n `102` status `ready` deltaP `30.77` edge `1.3428` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.7132` n `102` status `ready` deltaP `16.8812` edge `1.1342` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `2.0309` n `108` status `ready` deltaP `6.3798` edge `0.4086` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.7756` n `108` status `ready` deltaP `7.4469` edge `0.3059` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5146` n `108` status `ready` deltaP `17.7168` edge `0.0592` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.1069` n `117` status `ready` deltaP `5.1115` edge `0.0187` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4466` n `117` status `ready` deltaP `3.1027` edge `0.0033` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.4669` n `117` status `ready` deltaP `3.4648` edge `0.0567` maxDD `-6.5061`
- `market_context_high->equity_1h` score `-1.2804` n `117` status `ready` deltaP `6.116` edge `0.0304` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.3755` n `117` status `ready` deltaP `-8.6072` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->crypto_alt_1h` score `-1.3821` n `117` status `ready` deltaP `-2.5181` edge `0.0302` maxDD `-5.954`
- `market_context_high->index_4h` score `-1.6641` n `108` status `ready` deltaP `-0.3952` edge `-0.0017` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.0803` n `117` status `ready` deltaP `-6.4922` edge `-0.0169` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.3534` n `108` status `ready` deltaP `-14.493` edge `-0.0035` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.6127` n `102` status `ready` deltaP `14.5425` edge `0.115` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5515` n `102` status `ready` deltaP `-16.7177` edge `-0.0072` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.7807` n `108` status `ready` deltaP `-26.6711` edge `-0.1013` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.7838` n `108` status `ready` deltaP `-4.3078` edge `-0.0211` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
