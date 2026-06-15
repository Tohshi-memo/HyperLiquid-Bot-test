# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T18:52:38.921285+00:00`
- Price records: `672`
- Market context records: `4017`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10566`

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

- `risk_on_high->unknown_4h` score `146.5446` n `40` status `ready` deltaP `-5.0571` edge `12.4274` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.5446` n `40` status `ready` deltaP `-5.0571` edge `12.4274` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.8788` n `134` status `ready` deltaP `-3.9461` edge `4.5024` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.5446` n `145` status `ready` deltaP `2.2705` edge `2.7392` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `6.8234` n `40` status `ready` deltaP `39.1681` edge `0.3075` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.8234` n `40` status `ready` deltaP `39.1681` edge `0.3075` maxDD `0.0`
- `market_context_high->index_24h` score `3.7981` n `134` status `ready` deltaP `26.1168` edge `0.1636` maxDD `-1.3629`
- `risk_on_high->equity_4h` score `3.4408` n `40` status `ready` deltaP `36.0084` edge `0.0514` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.4408` n `40` status `ready` deltaP `36.0084` edge `0.0514` maxDD `-0.0446`
- `market_context_high->metal_24h` score `2.8246` n `134` status `ready` deltaP `14.1274` edge `0.2399` maxDD `-4.8962`
- `market_context_high->equity_4h` score `1.7412` n `145` status `ready` deltaP `19.1981` edge `0.1452` maxDD `-6.9137`
- `risk_on_high->index_24h` score `1.3558` n `40` status `ready` deltaP `26.8631` edge `-0.0661` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.3558` n `40` status `ready` deltaP `26.8631` edge `-0.0661` maxDD `0.0`
- `market_context_high->equity_1h` score `1.3109` n `148` status `ready` deltaP `8.8809` edge `0.106` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.0996` n `40` status `ready` deltaP `19.2275` edge `0.03` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0996` n `40` status `ready` deltaP `19.2275` edge `0.03` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `0.996` n `148` status `ready` deltaP `9.767` edge `0.0721` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `0.9644` n `40` status `ready` deltaP `4.2028` edge `0.2805` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9644` n `40` status `ready` deltaP `4.2028` edge `0.2805` maxDD `-12.9187`
- `market_context_high->equity_24h` score `0.8734` n `134` status `ready` deltaP `16.0338` edge `0.2657` maxDD `-14.318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
