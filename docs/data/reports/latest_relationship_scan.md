# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T07:22:32.729131+00:00`
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

- `market_context_high->commodity_4h` score `1.147` n `169` status `ready` deltaP `13.9111` edge `0.0743` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.9168` n `136` status `ready` deltaP `19.6299` edge `0.0263` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.8162` n `169` status `ready` deltaP `10.8472` edge `0.03` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.1393` n `169` status `ready` deltaP `9.1622` edge `0.0105` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1123` n `169` status `ready` deltaP `4.494` edge `0.0008` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6171` n `136` status `ready` deltaP `1.6528` edge `0.0907` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7973` n `169` status `ready` deltaP `-2.4943` edge `-0.0021` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8337` n `169` status `ready` deltaP `-5.0229` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.052` n `169` status `ready` deltaP `-0.2729` edge `-0.0076` maxDD `-1.26`
- `market_context_high->equity_1h` score `-1.2279` n `169` status `ready` deltaP `-1.8149` edge `-0.0032` maxDD `-4.6286`
- `market_context_high->metal_24h` score `-1.245` n `136` status `ready` deltaP `-2.7742` edge `0.0429` maxDD `-2.9193`
- `market_context_high->equity_24h` score `-1.4645` n `136` status `ready` deltaP `-1.0832` edge `0.1995` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5382` n `169` status `ready` deltaP `-8.5919` edge `-0.0378` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.8962` n `169` status `ready` deltaP `-5.448` edge `-0.0304` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0337` n `169` status `ready` deltaP `-9.9439` edge `-0.1101` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.5836` n `169` status `ready` deltaP `-10.0122` edge `-0.0585` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.8653` n `169` status `ready` deltaP `-11.1444` edge `-0.1455` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4435` n `136` status `ready` deltaP `-11.9075` edge `-0.1466` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8503` n `136` status `ready` deltaP `-2.8902` edge `-0.1355` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5596` n `136` status `ready` deltaP `-5.3752` edge `-0.19` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
