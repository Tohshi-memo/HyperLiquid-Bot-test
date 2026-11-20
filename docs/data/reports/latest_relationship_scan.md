# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T10:37:26.889450+00:00`
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

- `market_context_high->unknown_1h` score `11509.9516` n `112` status `ready` deltaP `1.4169` edge `959.173` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.6233` n `108` status `ready` deltaP `0.5194` edge `621.3269` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4433` n `102` status `ready` deltaP `30.77` edge `1.3411` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.6124` n `102` status `ready` deltaP `16.8812` edge `1.1258` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.8271` n `108` status `ready` deltaP `5.6176` edge `0.3967` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.5634` n `108` status `ready` deltaP `6.6847` edge `0.2933` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5788` n `108` status `ready` deltaP `18.1741` edge `0.0615` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.1311` n `112` status `ready` deltaP `4.9454` edge `0.0167` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3647` n `112` status `ready` deltaP `4.1863` edge `0.065` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.4484` n `112` status `ready` deltaP `3.0047` edge `0.0038` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1671` n `112` status `ready` deltaP `-2.0637` edge `0.0387` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.285` n `112` status `ready` deltaP `6.1324` edge `0.0299` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.4382` n `112` status `ready` deltaP `-9.3456` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7043` n `108` status `ready` deltaP `-0.8525` edge `-0.002` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3708` n `108` status `ready` deltaP `-14.7979` edge `-0.0037` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4039` n `112` status `ready` deltaP `-9.0516` edge `-0.0268` maxDD `-4.3877`
- `market_context_high->metal_24h` score `-4.7075` n `102` status `ready` deltaP `14.5425` edge `0.1071` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5479` n `102` status `ready` deltaP `-16.7177` edge `-0.0069` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.8559` n `108` status `ready` deltaP `-27.2809` edge `-0.1035` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.8913` n `108` status `ready` deltaP `-4.9175` edge `-0.026` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
