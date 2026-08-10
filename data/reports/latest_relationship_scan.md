# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T09:37:32.081437+00:00`
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

- `market_context_high->commodity_4h` score `1.0621` n `169` status `ready` deltaP `13.1501` edge `0.0723` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8055` n `136` status `ready` deltaP `18.7634` edge `0.0228` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7332` n `169` status `ready` deltaP `10.0202` edge `0.0286` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0628` n `169` status `ready` deltaP `8.4011` edge `0.0092` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1491` n `169` status `ready` deltaP `3.8178` edge `0.0006` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6075` n `136` status `ready` deltaP `1.6528` edge `0.0915` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7907` n `169` status `ready` deltaP `-2.4271` edge `-0.002` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8016` n `169` status `ready` deltaP `-4.5087` edge `-0.0091` maxDD `-2.0884`
- `market_context_high->equity_24h` score `-1.118` n `136` status `ready` deltaP `-0.2166` edge `0.2226` maxDD `-21.1456`
- `market_context_high->index_4h` score `-1.1481` n `169` status `ready` deltaP `-1.3384` edge `-0.0085` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.195` n `136` status `ready` deltaP `-2.2543` edge `0.0436` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.2184` n `169` status `ready` deltaP `-1.7565` edge `-0.0028` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.5668` n `169` status `ready` deltaP `-8.9785` edge `-0.0389` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9334` n `169` status `ready` deltaP `-6.0568` edge `-0.0311` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.1375` n `169` status `ready` deltaP `-11.0094` edge `-0.1163` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.6126` n `169` status `ready` deltaP `-10.2407` edge `-0.0594` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9848` n `169` status `ready` deltaP `-12.3621` edge `-0.1527` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4327` n `136` status `ready` deltaP `-11.9075` edge `-0.1457` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7291` n `136` status `ready` deltaP `-2.8902` edge `-0.1254` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5799` n `136` status `ready` deltaP `-5.3752` edge `-0.1926` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
