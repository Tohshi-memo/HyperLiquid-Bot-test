# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T01:37:30.333349+00:00`
- Price records: `672`
- Market context records: `5098`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `19.7027` n `79` status `ready` deltaP `27.547` edge `1.4925` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2399` n `105` status `ready` deltaP `21.732` edge `0.644` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `8.034` n `117` status `ready` deltaP `4.9568` edge `0.7006` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `2.9036` n `105` status `ready` deltaP `13.7354` edge `0.4406` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.2498` n `105` status `ready` deltaP `11.9832` edge `0.4378` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.1982` n `105` status `ready` deltaP `11.4097` edge `0.1907` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.5402` n `117` status `ready` deltaP `7.0961` edge `0.1181` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.5141` n `117` status `ready` deltaP `9.5732` edge `0.0614` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.444` n `117` status `ready` deltaP `7.8254` edge `0.1293` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.3497` n `117` status `ready` deltaP `9.5975` edge `0.0305` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.1207` n `105` status `ready` deltaP `7.754` edge `0.0399` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.0127` n `117` status `ready` deltaP `5.5556` edge `0.0117` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.3448` n `105` status `ready` deltaP `3.5265` edge `0.0666` maxDD `-4.0781`
- `market_context_high->commodity_1h` score `-0.9401` n `117` status `ready` deltaP `-0.3404` edge `-0.0003` maxDD `-2.062`
- `market_context_high->fx_1h` score `-1.4743` n `117` status `ready` deltaP `-8.3948` edge `-0.0028` maxDD `-0.7944`
- `market_context_high->fx_24h` score `-1.5455` n `79` status `ready` deltaP `-2.9689` edge `-0.0078` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.6753` n `79` status `ready` deltaP `7.7004` edge `0.0301` maxDD `-15.0303`
- `market_context_high->commodity_4h` score `-1.9891` n `105` status `ready` deltaP `3.146` edge `-0.0232` maxDD `-7.0824`
- `market_context_high->fx_4h` score `-2.0378` n `105` status `ready` deltaP `-8.133` edge `-0.0083` maxDD `-1.9169`
- `market_context_high->metal_24h` score `-4.5254` n `79` status `ready` deltaP `-6.5995` edge `0.0093` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
