# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T11:52:34.005677+00:00`
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

- `market_context_high->commodity_4h` score `1.0381` n `169` status `ready` deltaP `13.061` edge `0.0709` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7719` n `136` status `ready` deltaP `18.7634` edge `0.02` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.6877` n `169` status `ready` deltaP `9.5711` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.055` n `169` status `ready` deltaP `8.3192` edge `0.0091` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1249` n `169` status `ready` deltaP `4.2669` edge `0.0007` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.5919` n `136` status `ready` deltaP `1.6528` edge `0.0928` maxDD `-5.9181`
- `market_context_high->equity_24h` score `-0.6143` n `136` status `ready` deltaP `1.1698` edge `0.2544` maxDD `-21.0709`
- `market_context_high->metal_1h` score `-0.7579` n `169` status `ready` deltaP `-3.7602` edge `-0.0085` maxDD `-2.0884`
- `market_context_high->index_1h` score `-0.7655` n `169` status `ready` deltaP `-2.1277` edge `-0.0019` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-1.0782` n `136` status `ready` deltaP `-1.2144` edge `0.0464` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.1763` n `169` status `ready` deltaP `-1.4571` edge `-0.0018` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2025` n `169` status `ready` deltaP `-1.8843` edge `-0.0094` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.5777` n `169` status `ready` deltaP `-9.1282` edge `-0.0393` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9218` n `169` status `ready` deltaP `-6.0002` edge `-0.03` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2089` n `169` status `ready` deltaP `-11.4059` edge `-0.1237` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.6306` n `169` status `ready` deltaP `-10.3904` edge `-0.0599` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-4.0281` n `169` status `ready` deltaP `-12.7598` edge `-0.1556` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3763` n `136` status `ready` deltaP `-11.9075` edge `-0.141` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.433` n `136` status `ready` deltaP `-2.0236` edge `-0.1065` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5963` n `136` status `ready` deltaP `-5.3752` edge `-0.1947` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
