# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T07:37:24.604424+00:00`
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

- `market_context_high->commodity_4h` score `1.1458` n `169` status `ready` deltaP `13.9111` edge `0.0742` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8981` n `136` status `ready` deltaP `19.4566` edge `0.0259` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.815` n `169` status `ready` deltaP `10.8472` edge `0.0299` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.1247` n `169` status `ready` deltaP `9.01` edge `0.0103` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1209` n `169` status `ready` deltaP `4.3445` edge `0.0007` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6147` n `136` status `ready` deltaP `1.6528` edge `0.0909` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7949` n `169` status `ready` deltaP `-2.4943` edge `-0.0019` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8423` n `169` status `ready` deltaP `-5.1724` edge `-0.0099` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.0508` n `169` status `ready` deltaP `-0.2729` edge `-0.0075` maxDD `-1.26`
- `market_context_high->equity_1h` score `-1.2243` n `169` status `ready` deltaP `-1.8149` edge `-0.0029` maxDD `-4.6286`
- `market_context_high->metal_24h` score `-1.2462` n `136` status `ready` deltaP `-2.7742` edge `0.0428` maxDD `-2.9193`
- `market_context_high->equity_24h` score `-1.417` n `136` status `ready` deltaP `-0.9099` edge `0.2023` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5389` n `169` status `ready` deltaP `-8.5919` edge `-0.0379` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9065` n `169` status `ready` deltaP `-5.6002` edge `-0.0307` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0345` n `169` status `ready` deltaP `-9.9439` edge `-0.1102` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.6003` n `169` status `ready` deltaP `-10.1617` edge `-0.0589` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.8787` n `169` status `ready` deltaP `-11.2967` edge `-0.1462` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4459` n `136` status `ready` deltaP `-11.9075` edge `-0.1468` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8443` n `136` status `ready` deltaP `-2.8902` edge `-0.135` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5627` n `136` status `ready` deltaP `-5.3752` edge `-0.1904` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
