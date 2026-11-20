# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T11:22:29.385214+00:00`
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

- `market_context_high->unknown_1h` score `11231.0947` n `115` status `ready` deltaP `1.7197` edge `935.9329` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7456.1345` n `108` status `ready` deltaP `0.5194` edge `621.3695` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4445` n `102` status `ready` deltaP `30.77` edge `1.3412` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.6676` n `102` status `ready` deltaP `16.8812` edge `1.1304` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.9597` n `108` status `ready` deltaP `6.0749` edge `0.4047` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.6912` n `108` status `ready` deltaP `7.142` edge `0.3009` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5364` n `108` status `ready` deltaP `17.8693` edge `0.06` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0918` n `115` status `ready` deltaP `5.824` edge `0.02` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3581` n `115` status `ready` deltaP `4.0276` edge `0.0669` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3932` n `115` status `ready` deltaP `3.6358` edge `0.0042` maxDD `-1.2295`
- `market_context_high->equity_1h` score `-1.1549` n `115` status `ready` deltaP `6.6935` edge `0.037` maxDD `-10.8962`
- `market_context_high->crypto_alt_1h` score `-1.1728` n `115` status `ready` deltaP `-2.0594` edge `0.0382` maxDD `-5.4428`
- `market_context_high->fx_1h` score `-1.3952` n `115` status `ready` deltaP `-8.8376` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.6775` n `108` status `ready` deltaP `-0.5476` edge `-0.0018` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.2152` n `115` status `ready` deltaP `-7.5475` edge `-0.0211` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.3534` n `108` status `ready` deltaP `-14.493` edge `-0.0035` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.6523` n `102` status `ready` deltaP `14.5425` edge `0.1117` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5491` n `102` status `ready` deltaP `-16.7177` edge `-0.007` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.8123` n `108` status `ready` deltaP `-26.976` edge `-0.1019` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.8092` n `108` status `ready` deltaP `-4.4602` edge `-0.0222` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
