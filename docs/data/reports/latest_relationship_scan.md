# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T21:52:27.607365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2630`

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

- `market_context_high->unknown_1h` score `12005.6745` n `108` status `ready` deltaP `0.8373` edge `1000.4871` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7545.412` n `107` status `ready` deltaP `-0.0071` edge `628.8128` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.0574` n `88` status `ready` deltaP `42.6767` edge `1.7796` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `12.0254` n `88` status `ready` deltaP `25.9628` edge `1.5079` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.9152` n `107` status `ready` deltaP `4.5432` edge `0.4112` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.2169` n `107` status `ready` deltaP `5.4579` edge `0.2726` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.5564` n `88` status `ready` deltaP `19.0656` edge `0.2281` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.4094` n `107` status `ready` deltaP `17.7527` edge `0.045` maxDD `-6.0054`
- `market_context_high->crypto_major_1h` score `-0.1931` n `108` status `ready` deltaP `5.1453` edge `0.0806` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2841` n `108` status `ready` deltaP `2.9663` edge `0.005` maxDD `-1.2295`
- `market_context_high->metal_1h` score `-0.3112` n `108` status `ready` deltaP `3.8922` edge `0.0146` maxDD `-2.6517`
- `market_context_high->crypto_alt_1h` score `-0.7012` n `108` status `ready` deltaP `-1.7853` edge `0.0442` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.2286` n `108` status `ready` deltaP `6.0435` edge `0.0352` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6313` n `108` status `ready` deltaP `-11.6988` edge `-0.002` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.9521` n `107` status `ready` deltaP `-3.3508` edge `-0.006` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3962` n `107` status `ready` deltaP `-15.1826` edge `-0.0044` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4259` n `108` status `ready` deltaP `-9.969` edge `-0.0275` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.268` n `88` status `ready` deltaP `-24.9842` edge `-0.0118` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1095` n `107` status `ready` deltaP `-29.1615` edge `-0.1121` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.5505` n `107` status `ready` deltaP `-7.7986` edge `-0.0762` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
