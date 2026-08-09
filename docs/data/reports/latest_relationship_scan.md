# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T22:22:29.671389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10874`

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

- `market_context_high->commodity_4h` score `1.1106` n `144` status `ready` deltaP `14.3462` edge `0.0642` maxDD `-2.7169`
- `market_context_high->metal_24h` score `0.9731` n `123` status `ready` deltaP `5.7884` edge `0.1001` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.8457` n `156` status `ready` deltaP `11.0663` edge `0.031` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.6881` n `123` status `ready` deltaP `3.7687` edge `0.3382` maxDD `-21.1456`
- `market_context_high->fx_24h` score `0.5073` n `123` status `ready` deltaP `19.2158` edge `0.0236` maxDD `-1.9329`
- `market_context_high->index_24h` score `-0.0699` n `123` status `ready` deltaP `4.6029` edge `0.1135` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5572` n `156` status `ready` deltaP `1.0671` edge `-0.004` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.6243` n `144` status `ready` deltaP `-1.609` edge `-0.0088` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.6281` n `156` status `ready` deltaP `-4.1494` edge `-0.0056` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6887` n `156` status `ready` deltaP `-4.0227` edge `-0.0083` maxDD `-1.2546`
- `market_context_high->fx_4h` score `-0.7253` n `144` status `ready` deltaP `2.8624` edge `-0.0042` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0025` n `144` status `ready` deltaP `-1.626` edge `-0.0168` maxDD `-2.7373`
- `market_context_high->equity_1h` score `-1.0055` n `156` status `ready` deltaP `-0.6948` edge `0.0037` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.1337` n `156` status `ready` deltaP `-8.4254` edge `-0.025` maxDD `-2.4677`
- `market_context_high->crypto_major_1h` score `-2.0209` n `156` status `ready` deltaP `-10.8782` edge `-0.0532` maxDD `-7.3365`
- `market_context_high->equity_4h` score `-2.5676` n `144` status `ready` deltaP `-2.1511` edge `-0.0659` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-4.0291` n `123` status `ready` deltaP `3.0404` edge `-0.1066` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.0761` n `144` status `ready` deltaP `-8.689` edge `-0.1161` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-5.0099` n `123` status `ready` deltaP `-14.6384` edge `-0.1756` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8566` n `156` status `ready` deltaP `-6.7519` edge `-0.564` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
