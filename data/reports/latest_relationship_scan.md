# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T04:22:26.569805+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2790`

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

- `market_context_high->unknown_1h` score `11994.7256` n `108` status `ready` deltaP `0.987` edge `999.5737` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.1989` n `108` status `ready` deltaP `-0.0903` edge `621.2956` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `18.0305` n `97` status `ready` deltaP `34.4591` edge `1.493` maxDD `-14.6149`
- `market_context_high->crypto_alt_24h` score `7.794` n `97` status `ready` deltaP `19.7112` edge `1.2306` maxDD `-25.3558`
- `market_context_high->crypto_major_4h` score `1.2332` n `108` status `ready` deltaP `3.7883` edge `0.3594` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.9161` n `108` status `ready` deltaP `5.3127` edge `0.2485` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.8103` n `108` status `ready` deltaP `20.0034` edge `0.0686` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0451` n `108` status `ready` deltaP `6.1377` edge `0.0218` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2475` n `108` status `ready` deltaP `3.5651` edge `0.0057` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.328` n `108` status `ready` deltaP `4.5465` edge `0.0673` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.7504` n `108` status `ready` deltaP `-1.935` edge `0.0389` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.123` n `108` status `ready` deltaP `6.6423` edge `0.04` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6468` n `108` status `ready` deltaP `-11.8485` edge `-0.0023` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8332` n `108` status `ready` deltaP `-2.2245` edge `-0.0036` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.4111` n `108` status `ready` deltaP `-15.4076` edge `-0.0048` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4355` n `108` status `ready` deltaP `-9.969` edge `-0.0283` maxDD `-3.9892`
- `market_context_high->metal_24h` score `-2.8444` n `97` status `ready` deltaP `16.008` edge `0.138` maxDD `-28.5406`
- `market_context_high->fx_24h` score `-6.6862` n `97` status `ready` deltaP `-18.5209` edge `-0.0064` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.109` n `108` status `ready` deltaP `-29.1102` edge `-0.1124` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.3667` n `108` status `ready` deltaP `-6.8992` edge `-0.0524` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
