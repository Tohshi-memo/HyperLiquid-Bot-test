# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T05:07:15.886635+00:00`
- Price records: `672`
- Market context records: `1188`
- Flow alert records: `5326`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5282` n `141` status `ready` deltaP `44.3411` edge `1.3616` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.979` n `141` status `ready` deltaP `22.1779` edge `0.7187` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.3202` n `141` status `ready` deltaP `-3.2506` edge `0.5484` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `3.3204` n `141` status `ready` deltaP `4.7623` edge `0.3666` maxDD `-6.7322`
- `market_context_high->equity_4h` score `2.809` n `141` status `ready` deltaP `14.9715` edge `0.2006` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.3834` n `141` status `ready` deltaP `15.7358` edge `0.3264` maxDD `-14.2815`
- `market_context_high->index_24h` score `2.3478` n `141` status `ready` deltaP `15.4181` edge `0.2015` maxDD `-5.3574`
- `market_context_high->index_4h` score `1.0695` n `141` status `ready` deltaP `10.6696` edge `0.0863` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6606` n `141` status `ready` deltaP `9.5765` edge `0.0229` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4143` n `141` status `ready` deltaP `3.8242` edge `0.0468` maxDD `-1.3546`
- `market_context_high->fx_1h` score `-0.079` n `141` status `ready` deltaP `5.4221` edge `-0.0007` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1486` n `141` status `ready` deltaP `6.744` edge `0.1281` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.2187` n `141` status `ready` deltaP `8.1019` edge `-0.0112` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3371` n `141` status `ready` deltaP `3.562` edge `0.0096` maxDD `-4.1256`
- `market_context_high->fx_24h` score `-0.4497` n `141` status `ready` deltaP `6.7893` edge `0.0352` maxDD `-6.7155`
- `market_context_high->crypto_alt_1h` score `-0.5258` n `141` status `ready` deltaP `-1.0394` edge `0.0238` maxDD `-3.4088`
- `market_context_high->commodity_24h` score `-0.618` n `141` status `ready` deltaP `-4.6321` edge `0.467` maxDD `-36.2275`
- `market_context_high->fx_4h` score `-0.9602` n `141` status `ready` deltaP `-4.3246` edge `-0.0045` maxDD `-0.8488`
- `market_context_high->commodity_1h` score `-1.0055` n `141` status `ready` deltaP `-3.6013` edge `0.0017` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.275` n `141` status `ready` deltaP `3.8747` edge `0.1072` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
