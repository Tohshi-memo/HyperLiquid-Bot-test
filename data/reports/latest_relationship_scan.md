# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T18:22:28.776393+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->equity_24h` score `1.9192` n `137` status `ready` deltaP `5.1285` edge `0.4433` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.8192` n `173` status `ready` deltaP `11.5836` edge `0.0625` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7578` n `181` status `ready` deltaP `10.0573` edge `0.0304` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7177` n `137` status `ready` deltaP `18.9566` edge `0.0142` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.1172` n `173` status `ready` deltaP `6.4509` edge `0.0072` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1224` n `181` status `ready` deltaP `4.3612` edge `0.0004` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.1468` n `137` status `ready` deltaP `4.7717` edge `0.1091` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6001` n `181` status `ready` deltaP `-3.8583` edge `-0.0035` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.8025` n `137` status `ready` deltaP `1.179` edge `0.0577` maxDD `-2.9283`
- `market_context_high->metal_1h` score `-0.8542` n `181` status `ready` deltaP `-5.2519` edge `-0.0109` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.0164` n `181` status `ready` deltaP `-3.2165` edge `-0.0159` maxDD `-5.1036`
- `market_context_high->index_4h` score `-1.1917` n `173` status `ready` deltaP `-1.5843` edge `-0.0105` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.8016` n `181` status `ready` deltaP `-10.2706` edge `-0.0456` maxDD `-6.3518`
- `market_context_high->metal_4h` score `-2.0623` n `173` status `ready` deltaP `-7.4404` edge `-0.0384` maxDD `-6.1111`
- `market_context_high->crypto_major_24h` score `-3.0676` n `137` status `ready` deltaP `1.4687` edge `-0.016` maxDD `-14.2873`
- `market_context_high->equity_4h` score `-3.1771` n `173` status `ready` deltaP `-11.017` edge `-0.1081` maxDD `-9.0618`
- `market_context_high->crypto_alt_24h` score `-3.7302` n `137` status `ready` deltaP `-9.9963` edge `-0.0999` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.8915` n `181` status `ready` deltaP `-10.5559` edge `-0.0635` maxDD `-11.9002`
- `market_context_high->crypto_alt_4h` score `-5.8493` n `173` status `ready` deltaP `-11.4427` edge `-0.1354` maxDD `-15.3937`
- `market_context_high->commodity_24h` score `-8.8234` n `137` status `ready` deltaP `-5.8875` edge `-0.2204` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
