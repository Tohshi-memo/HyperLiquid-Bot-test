# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T10:37:25.843584+00:00`
- Price records: `672`
- Market context records: `7240`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `12851`

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

- `risk_on_high->crypto_major_4h` score `6.5114` n `34` status `ready` deltaP `27.0804` edge `0.4017` maxDD `-0.8359`
- `risk_on_and_context->crypto_major_4h` score `6.5114` n `34` status `ready` deltaP `27.0804` edge `0.4017` maxDD `-0.8359`
- `risk_on_high->crypto_alt_4h` score `4.3391` n `34` status `ready` deltaP `17.5574` edge `0.2841` maxDD `-1.1649`
- `risk_on_and_context->crypto_alt_4h` score `4.3391` n `34` status `ready` deltaP `17.5574` edge `0.2841` maxDD `-1.1649`
- `risk_on_high->metal_4h` score `0.5106` n `34` status `ready` deltaP `-6.9315` edge `0.1666` maxDD `-1.3947`
- `risk_on_and_context->metal_4h` score `0.5106` n `34` status `ready` deltaP `-6.9315` edge `0.1666` maxDD `-1.3947`
- `risk_on_high->crypto_major_1h` score `0.289` n `34` status `ready` deltaP `7.7756` edge `0.016` maxDD `-1.13`
- `risk_on_and_context->crypto_major_1h` score `0.289` n `34` status `ready` deltaP `7.7756` edge `0.016` maxDD `-1.13`
- `risk_on_high->unknown_4h` score `0.0867` n `34` status `ready` deltaP `5.0485` edge `0.0332` maxDD `-1.1261`
- `risk_on_and_context->unknown_4h` score `0.0867` n `34` status `ready` deltaP `5.0485` edge `0.0332` maxDD `-1.1261`
- `market_context_high->crypto_alt_1h` score `-0.7175` n `164` status `ready` deltaP `-0.3323` edge `0.0152` maxDD `-6.0641`
- `market_context_high->crypto_major_1h` score `-0.8149` n `164` status `ready` deltaP `3.2204` edge `0.0287` maxDD `-8.7053`
- `market_context_high->unknown_1h` score `-1.529` n `164` status `ready` deltaP `-5.9077` edge `-0.0904` maxDD `-1.6328`
- `market_context_high->metal_1h` score `-1.6288` n `164` status `ready` deltaP `-4.6553` edge `-0.002` maxDD `-3.5495`
- `risk_on_high->crypto_alt_1h` score `-1.7016` n `34` status `ready` deltaP `-13.2089` edge `-0.0112` maxDD `-1.4034`
- `risk_on_and_context->crypto_alt_1h` score `-1.7016` n `34` status `ready` deltaP `-13.2089` edge `-0.0112` maxDD `-1.4034`
- `market_context_high->unknown_4h` score `-1.7904` n `164` status `ready` deltaP `-0.1524` edge `0.0209` maxDD `-7.2874`
- `risk_on_high->metal_1h` score `-2.4351` n `34` status `ready` deltaP `-21.9796` edge `-0.0065` maxDD `-0.658`
- `risk_on_and_context->metal_1h` score `-2.4351` n `34` status `ready` deltaP `-21.9796` edge `-0.0065` maxDD `-0.658`
- `risk_on_high->unknown_1h` score `-3.548` n `34` status `ready` deltaP `-17.242` edge `-0.1247` maxDD `-1.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
