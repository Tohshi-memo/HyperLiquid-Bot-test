# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T12:52:32.350791+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2634`

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

- `market_context_high->unknown_1h` score `10735.09` n `120` status `ready` deltaP `1.507` edge `894.6006` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7272.8164` n `110` status `ready` deltaP `0.6541` edge `606.0921` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.5177` n `102` status `ready` deltaP `30.77` edge `1.3473` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.7972` n `102` status `ready` deltaP `16.8812` edge `1.1412` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.7393` n `110` status `ready` deltaP `5.8093` edge `0.3881` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.5428` n `110` status `ready` deltaP `6.8764` edge `0.2903` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.4005` n `110` status `ready` deltaP `16.9097` edge `0.0577` maxDD `-6.631`
- `market_context_high->metal_1h` score `-0.1534` n `120` status `ready` deltaP `4.471` edge `0.017` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3416` n `120` status `ready` deltaP `2.2056` edge `0.0027` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-1.1717` n `120` status `ready` deltaP `2.8243` edge `0.0399` maxDD `-7.843`
- `market_context_high->fx_1h` score `-1.2418` n `120` status `ready` deltaP `-7.026` edge `-0.0007` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.5803` n `120` status `ready` deltaP `5.1547` edge `0.0201` maxDD `-11.559`
- `market_context_high->index_4h` score `-1.7632` n `110` status `ready` deltaP `-1.1696` edge `-0.0048` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.9278` n `120` status `ready` deltaP `-3.009` edge `0.017` maxDD `-8.2736`
- `market_context_high->commodity_1h` score `-2.0064` n `120` status `ready` deltaP `-5.8084` edge `-0.0153` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.2714` n `110` status `ready` deltaP `-13.1126` edge `-0.0022` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.5335` n `102` status `ready` deltaP `14.5425` edge `0.1216` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5575` n `102` status `ready` deltaP `-16.7177` edge `-0.0077` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.5907` n `110` status `ready` deltaP `-25.2411` edge `-0.095` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.6214` n `110` status `ready` deltaP `-4.9307` edge `-0.0494` maxDD `-47.2276`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
