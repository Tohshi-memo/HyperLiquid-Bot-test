# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T18:07:19.113808+00:00`
- Price records: `672`
- Market context records: `1447`
- Flow alert records: `6078`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8808`

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

- `market_context_high->crypto_alt_24h` score `12.8267` n `157` status `ready` deltaP `28.8184` edge `1.0784` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.9592` n `157` status `ready` deltaP `14.2826` edge `1.0681` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.8052` n `157` status `ready` deltaP `27.4283` edge `0.9141` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.3144` n `157` status `ready` deltaP `19.555` edge `0.3378` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9906` n `157` status `ready` deltaP `12.7256` edge `0.4804` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.4637` n `219` status `ready` deltaP `7.1953` edge `0.157` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2456` n `157` status `ready` deltaP `11.0956` edge `0.0514` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1295` n `227` status `ready` deltaP `1.9988` edge `0.0359` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1323` n `227` status `ready` deltaP `3.3719` edge `0.013` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.463` n `227` status `ready` deltaP `0.9259` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.563` n `219` status `ready` deltaP `0.6571` edge `0.0576` maxDD `-3.7119`
- `market_context_high->crypto_alt_4h` score `-0.6087` n `219` status `ready` deltaP `10.2649` edge `0.2128` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.6607` n `227` status `ready` deltaP `1.4561` edge `0.0376` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0742` n `219` status `ready` deltaP `-4.6442` edge `-0.0097` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.1055` n `219` status `ready` deltaP `5.3938` edge `0.1428` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.1068` n `227` status `ready` deltaP `-0.9602` edge `0.0018` maxDD `-4.3439`
- `market_context_high->metal_1h` score `-1.1913` n `227` status `ready` deltaP `4.681` edge `0.0031` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.7105` n `227` status `ready` deltaP `-1.4779` edge `0.003` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.0688` n `219` status `ready` deltaP `7.228` edge `0.0486` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-2.9152` n `219` status `ready` deltaP `-11.1865` edge `-0.0445` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
