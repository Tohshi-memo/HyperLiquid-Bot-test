# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T04:52:16.645684+00:00`
- Price records: `672`
- Market context records: `1391`
- Flow alert records: `5916`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.1987` n `157` status `ready` deltaP `28.5275` edge `1.0229` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.6771` n `157` status `ready` deltaP `28.8184` edge `0.9826` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.4695` n `157` status `ready` deltaP `12.2567` edge `1.0408` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.1538` n `157` status `ready` deltaP `19.9022` edge `0.3221` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5688` n `157` status `ready` deltaP `13.0728` edge `0.3596` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6093` n `187` status `ready` deltaP `8.4151` edge `0.161` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0427` n `157` status `ready` deltaP `9.8803` edge `0.0426` maxDD `-1.3925`
- `market_context_high->index_1h` score `0.0334` n `199` status `ready` deltaP `5.0079` edge `0.0159` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0365` n `199` status `ready` deltaP `3.3611` edge `0.0304` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3036` n `199` status `ready` deltaP `3.5334` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.3843` n `187` status `ready` deltaP `9.0558` edge `0.0507` maxDD `-6.4478`
- `market_context_high->index_4h` score `-0.4711` n `187` status `ready` deltaP `0.8462` edge `0.064` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.5114` n `199` status `ready` deltaP `1.7904` edge `0.0325` maxDD `-3.6309`
- `market_context_high->metal_1h` score `-0.5532` n `199` status `ready` deltaP `5.4043` edge `0.0009` maxDD `-4.2945`
- `market_context_high->commodity_1h` score `-0.9107` n `199` status `ready` deltaP `-1.9514` edge `-0.0014` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1792` n `187` status `ready` deltaP `8.3083` edge `0.1783` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.249` n `187` status `ready` deltaP `5.0101` edge `0.1334` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.269` n `199` status `ready` deltaP `-0.5296` edge `0.0043` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.6855` n `187` status `ready` deltaP `-4.9954` edge `-0.0101` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.5655` n `187` status `ready` deltaP `-13.4089` edge `-0.0364` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
