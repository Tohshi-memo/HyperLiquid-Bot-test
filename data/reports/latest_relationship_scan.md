# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T06:22:26.469432+00:00`
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

- `market_context_high->commodity_4h` score `1.1849` n `169` status `ready` deltaP `14.2805` edge `0.075` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.9841` n `136` status `ready` deltaP `20.2308` edge `0.0279` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.8578` n `169` status `ready` deltaP `11.2178` edge `0.031` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.1498` n `169` status `ready` deltaP `9.2339` edge `0.0109` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0992` n `169` status `ready` deltaP `4.716` edge `0.001` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6141` n `136` status `ready` deltaP `1.7054` edge `0.0906` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7943` n `169` status `ready` deltaP `-2.4271` edge `-0.0023` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8389` n `169` status `ready` deltaP `-5.1075` edge `-0.0099` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.0468` n `169` status `ready` deltaP `-0.2075` edge `-0.0076` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.2095` n `136` status `ready` deltaP `-2.3897` edge `0.0433` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.2196` n `169` status `ready` deltaP `-1.7565` edge `-0.0029` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.5201` n `169` status `ready` deltaP `-8.3797` edge `-0.0369` maxDD `-5.5029`
- `market_context_high->equity_24h` score `-1.6187` n `136` status `ready` deltaP `-1.7361` edge `0.191` maxDD `-21.1456`
- `market_context_high->metal_4h` score `-1.887` n `169` status `ready` deltaP `-5.3904` edge `-0.0296` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0163` n `169` status `ready` deltaP `-9.7291` edge `-0.1093` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.5359` n `169` status `ready` deltaP `-9.6419` edge `-0.057` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.8118` n `169` status `ready` deltaP `-10.6256` edge `-0.1421` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.405` n `136` status `ready` deltaP `-11.8771` edge `-0.1436` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8347` n `136` status `ready` deltaP `-2.6654` edge `-0.1357` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5401` n `136` status `ready` deltaP `-5.3002` edge `-0.188` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
