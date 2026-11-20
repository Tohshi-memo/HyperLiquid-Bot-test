# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T13:07:25.808238+00:00`
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

- `market_context_high->unknown_1h` score `10732.9768` n `120` status `ready` deltaP `1.507` edge `894.4245` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7273.5184` n `110` status `ready` deltaP `0.6541` edge `606.1506` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.5357` n `102` status `ready` deltaP `30.77` edge `1.3488` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.8296` n `102` status `ready` deltaP `16.8812` edge `1.1439` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.7429` n `110` status `ready` deltaP `5.8093` edge `0.3884` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.562` n `110` status `ready` deltaP `6.8764` edge `0.2919` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.3823` n `110` status `ready` deltaP `16.7572` edge `0.0572` maxDD `-6.631`
- `market_context_high->metal_1h` score `-0.162` n `120` status `ready` deltaP `4.3213` edge `0.0169` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3424` n `120` status `ready` deltaP `2.2056` edge `0.0026` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-1.1753` n `120` status `ready` deltaP `2.8243` edge `0.0396` maxDD `-7.843`
- `market_context_high->fx_1h` score `-1.255` n `120` status `ready` deltaP `-7.1757` edge `-0.0008` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.6006` n `120` status `ready` deltaP `5.005` edge `0.0194` maxDD `-11.559`
- `market_context_high->index_4h` score `-1.7668` n `110` status `ready` deltaP `-1.1696` edge `-0.0051` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.9254` n `120` status `ready` deltaP `-3.009` edge `0.0172` maxDD `-8.2736`
- `market_context_high->commodity_1h` score `-1.9921` n `120` status `ready` deltaP `-5.6587` edge `-0.0151` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.2817` n `110` status `ready` deltaP `-13.265` edge `-0.0025` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.5155` n `102` status `ready` deltaP `14.5425` edge `0.1231` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5599` n `102` status `ready` deltaP `-16.7177` edge `-0.0079` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.6089` n `110` status `ready` deltaP `-25.3935` edge `-0.0955` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.6562` n `110` status `ready` deltaP `-4.9307` edge `-0.0523` maxDD `-47.2276`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
