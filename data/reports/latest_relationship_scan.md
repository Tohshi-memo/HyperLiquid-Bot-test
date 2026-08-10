# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T08:02:56.597164+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10712`

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

- `market_context_high->commodity_4h` score `1.1482` n `169` status `ready` deltaP `13.9111` edge `0.0744` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8608` n `136` status `ready` deltaP `19.11` edge `0.0251` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.8231` n `169` status `ready` deltaP `10.9184` edge `0.0301` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0955` n `169` status `ready` deltaP `8.7055` edge `0.0099` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1171` n `169` status `ready` deltaP `4.4166` edge `0.0007` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6111` n `136` status `ready` deltaP `1.6528` edge `0.0912` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.8027` n `169` status `ready` deltaP `-2.5768` edge `-0.002` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8381` n `169` status `ready` deltaP `-5.1075` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.0666` n `169` status `ready` deltaP `-0.4251` edge `-0.0078` maxDD `-1.26`
- `market_context_high->equity_1h` score `-1.2352` n `169` status `ready` deltaP `-1.9062` edge `-0.0032` maxDD `-4.6286`
- `market_context_high->metal_24h` score `-1.2486` n `136` status `ready` deltaP `-2.7742` edge `0.0426` maxDD `-2.9193`
- `market_context_high->equity_24h` score `-1.3522` n `136` status `ready` deltaP `-0.9099` edge `0.2077` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5544` n `169` status `ready` deltaP `-8.8288` edge `-0.0383` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9175` n `169` status `ready` deltaP `-5.7524` edge `-0.0311` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0518` n `169` status `ready` deltaP `-10.0961` edge `-0.1114` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.6234` n `169` status `ready` deltaP `-10.3904` edge `-0.0593` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.8952` n `169` status `ready` deltaP `-11.4489` edge `-0.1473` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4435` n `136` status `ready` deltaP `-11.9075` edge `-0.1466` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8143` n `136` status `ready` deltaP `-2.8902` edge `-0.1325` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5651` n `136` status `ready` deltaP `-5.3752` edge `-0.1907` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
