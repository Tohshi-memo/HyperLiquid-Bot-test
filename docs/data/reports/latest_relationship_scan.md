# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T23:07:18.103212+00:00`
- Price records: `672`
- Market context records: `1676`
- Flow alert records: `6735`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `8.9118` n `157` status `ready` deltaP `27.6673` edge `0.8008` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.1778` n `195` status `ready` deltaP `22.8901` edge `0.5453` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8746` n `157` status `ready` deltaP `19.1821` edge `0.3328` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.2778` n `195` status `ready` deltaP `18.9955` edge `0.4174` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.5545` n `195` status `ready` deltaP `13.9236` edge `0.2295` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8778` n `157` status `ready` deltaP `18.3644` edge `0.5239` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.6449` n `204` status `ready` deltaP `6.3608` edge `0.1137` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.5168` n `157` status `ready` deltaP `25.4964` edge `1.054` maxDD `-88.8062`
- `market_context_high->unknown_24h` score `0.2714` n `157` status `ready` deltaP `13.1036` edge `0.4673` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `0.1616` n `157` status `ready` deltaP `24.4353` edge `0.7164` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.057` n `195` status `ready` deltaP `5.677` edge `0.0758` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1686` n `204` status `ready` deltaP `2.9999` edge `0.0468` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.4078` n `204` status `ready` deltaP `3.2553` edge `0.0717` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.5249` n `157` status `ready` deltaP `6.3397` edge `0.0189` maxDD `-1.3925`
- `market_context_high->metal_1h` score `-0.623` n `204` status `ready` deltaP `6.0467` edge `0.0134` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6705` n `204` status `ready` deltaP `-0.6898` edge `0.0119` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.7017` n `195` status `ready` deltaP `12.6469` edge `0.1264` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.857` n `204` status `ready` deltaP `-0.8835` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.2509` n `195` status `ready` deltaP `-8.3224` edge `-0.012` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.2242` n `204` status `ready` deltaP `-0.8982` edge `-0.0336` maxDD `-14.9789`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
