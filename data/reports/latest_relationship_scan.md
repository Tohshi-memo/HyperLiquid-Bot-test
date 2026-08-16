# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T21:52:23.804455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `151.4478` n `82` status `ready` deltaP `-26.9648` edge `19.8645` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `6.7279` n `82` status `ready` deltaP `41.311` edge `0.291` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.0344` n `116` status `ready` deltaP `11.8061` edge `0.0546` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0881` n `118` status `ready` deltaP `2.6388` edge `0.0162` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.2505` n `118` status `ready` deltaP `2.0425` edge `0.002` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.3332` n `116` status `ready` deltaP `4.0948` edge `0.0054` maxDD `-0.504`
- `market_context_high->metal_4h` score `-0.4787` n `116` status `ready` deltaP `11.8114` edge `0.0006` maxDD `-4.5909`
- `market_context_high->metal_1h` score `-0.4887` n `118` status `ready` deltaP `2.0425` edge `-0.0047` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.7015` n `118` status `ready` deltaP `-5.2902` edge `-0.0025` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.1097` n `116` status `ready` deltaP `-8.4419` edge `-0.0051` maxDD `-0.8045`
- `market_context_high->index_24h` score `-1.5905` n `82` status `ready` deltaP `1.8293` edge `-0.054` maxDD `-1.2587`
- `market_context_high->crypto_major_4h` score `-1.8047` n `116` status `ready` deltaP `0.7097` edge `-0.0268` maxDD `-5.9325`
- `market_context_high->fx_24h` score `-1.891` n `82` status `ready` deltaP `-13.1987` edge `0.0063` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.1041` n `82` status `ready` deltaP `-11.4541` edge `0.0578` maxDD `-7.0954`
- `market_context_high->crypto_major_1h` score `-2.3439` n `118` status `ready` deltaP `-6.0819` edge `-0.0399` maxDD `-5.8571`
- `market_context_high->crypto_alt_1h` score `-2.4006` n `118` status `ready` deltaP `-5.2344` edge `-0.0312` maxDD `-7.0497`
- `market_context_high->crypto_major_24h` score `-2.4707` n `82` status `ready` deltaP `-4.1836` edge `0.0871` maxDD `-22.4106`
- `market_context_high->equity_1h` score `-2.6594` n `118` status `ready` deltaP `-10.7759` edge `-0.0472` maxDD `-4.8731`
- `market_context_high->crypto_alt_4h` score `-6.2498` n `116` status `ready` deltaP `-8.7206` edge `-0.0646` maxDD `-19.1797`
- `market_context_high->unknown_1h` score `-6.5128` n `118` status `ready` deltaP `3.537` edge `-0.5266` maxDD `-0.8437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
