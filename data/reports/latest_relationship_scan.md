# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T11:37:26.551187+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->commodity_4h` score `1.0441` n `169` status `ready` deltaP `13.061` edge `0.0714` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7755` n `136` status `ready` deltaP `18.7634` edge `0.0203` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7033` n `169` status `ready` deltaP `9.7208` edge `0.0281` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0538` n `169` status `ready` deltaP `8.3192` edge `0.009` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1249` n `169` status `ready` deltaP `4.2669` edge `0.0007` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.5967` n `136` status `ready` deltaP `1.6528` edge `0.0924` maxDD `-5.9181`
- `market_context_high->equity_24h` score `-0.6809` n `136` status `ready` deltaP `0.9965` edge `0.25` maxDD `-21.0709`
- `market_context_high->index_1h` score `-0.7655` n `169` status `ready` deltaP `-2.1277` edge `-0.0019` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7665` n `169` status `ready` deltaP `-3.9099` edge `-0.0086` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-1.0969` n `136` status `ready` deltaP `-1.3878` edge `0.046` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.1763` n `169` status `ready` deltaP `-1.4571` edge `-0.0018` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2025` n `169` status `ready` deltaP `-1.8843` edge `-0.0094` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.5661` n `169` status `ready` deltaP `-8.9785` edge `-0.0388` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9234` n `169` status `ready` deltaP `-6.0002` edge `-0.0302` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2043` n `169` status `ready` deltaP `-11.4059` edge `-0.1231` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.6138` n `169` status `ready` deltaP `-10.2407` edge `-0.0595` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-4.0186` n `169` status `ready` deltaP `-12.6073` edge `-0.1554` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3775` n `136` status `ready` deltaP `-11.9075` edge `-0.1411` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.4546` n `136` status `ready` deltaP `-2.0236` edge `-0.1083` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5916` n `136` status `ready` deltaP `-5.3752` edge `-0.1941` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
