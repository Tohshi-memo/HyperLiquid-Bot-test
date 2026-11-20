# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T12:37:29.083416+00:00`
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

- `market_context_high->unknown_1h` score `10734.3736` n `120` status `ready` deltaP `1.507` edge `894.5409` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7364.1071` n `109` status `ready` deltaP `0.5874` edge `613.7001` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.5057` n `102` status `ready` deltaP `30.77` edge `1.3463` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.7744` n `102` status `ready` deltaP `16.8812` edge `1.1393` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.9204` n `109` status `ready` deltaP `6.243` edge `0.4003` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.6975` n `109` status `ready` deltaP `7.3101` edge `0.3003` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.4575` n `109` status `ready` deltaP `17.3851` edge `0.0583` maxDD `-6.5525`
- `market_context_high->metal_1h` score `-0.162` n `120` status `ready` deltaP `4.3213` edge `0.0169` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3424` n `120` status `ready` deltaP `2.2056` edge `0.0026` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-1.1945` n `120` status `ready` deltaP `2.6746` edge `0.039` maxDD `-7.843`
- `market_context_high->fx_1h` score `-1.2406` n `120` status `ready` deltaP `-7.026` edge `-0.0006` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.5851` n `120` status `ready` deltaP `5.1547` edge `0.0197` maxDD `-11.559`
- `market_context_high->index_4h` score `-1.7157` n `109` status `ready` deltaP `-0.786` edge `-0.0034` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.9505` n `120` status `ready` deltaP `-3.1587` edge `0.0161` maxDD `-8.2736`
- `market_context_high->commodity_1h` score `-2.0064` n `120` status `ready` deltaP `-5.8084` edge `-0.0153` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.3037` n `109` status `ready` deltaP `-13.644` edge `-0.0028` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.5539` n `102` status `ready` deltaP `14.5425` edge `0.1199` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5551` n `102` status `ready` deltaP `-16.7177` edge `-0.0075` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.6844` n `109` status `ready` deltaP `-25.8726` edge `-0.0986` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.2264` n `109` status `ready` deltaP `-4.6221` edge `-0.0365` maxDD `-45.7908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
