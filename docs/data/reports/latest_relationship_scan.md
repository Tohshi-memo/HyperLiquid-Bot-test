# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T05:07:23.205150+00:00`
- Price records: `672`
- Market context records: `3250`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10598`

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

- `risk_on_high->crypto_major_4h` score `16.7214` n `31` status `ready` deltaP `30.8517` edge `1.3` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.7214` n `31` status `ready` deltaP `30.8517` edge `1.3` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.9442` n `103` status `ready` deltaP `16.9144` edge `2.6591` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.3304` n `103` status `ready` deltaP `47.4734` edge `0.8372` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.2805` n `103` status `ready` deltaP `30.2741` edge `0.827` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.2424` n `103` status `ready` deltaP `17.6595` edge `1.5242` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `5.164` n `31` status `ready` deltaP `12.1312` edge `0.7656` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.164` n `31` status `ready` deltaP `12.1312` edge `0.7656` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.2131` n `31` status `ready` deltaP `18.809` edge `0.5282` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.2131` n `31` status `ready` deltaP `18.809` edge `0.5282` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.2957` n `32` status `ready` deltaP `8.8136` edge `0.3425` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.2957` n `32` status `ready` deltaP `8.8136` edge `0.3425` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.2174` n `148` status `ready` deltaP `19.0508` edge `0.1536` maxDD `-3.9989`
- `market_context_high->crypto_major_24h` score `1.8719` n `103` status `ready` deltaP `20.985` edge `2.17` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.5788` n `31` status `ready` deltaP `5.7533` edge `0.2228` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.5788` n `31` status `ready` deltaP `5.7533` edge `0.2228` maxDD `-1.7001`
- `risk_on_high->crypto_alt_1h` score `0.4371` n `32` status `ready` deltaP `2.0958` edge `0.1858` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.4371` n `32` status `ready` deltaP `2.0958` edge `0.1858` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.3289` n `32` status `ready` deltaP `6.5494` edge `0.067` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3289` n `32` status `ready` deltaP `6.5494` edge `0.067` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
