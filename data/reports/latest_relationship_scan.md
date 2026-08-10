# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T09:07:38.884015+00:00`
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

- `market_context_high->commodity_4h` score `1.079` n `169` status `ready` deltaP `13.3023` edge `0.0727` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8289` n `136` status `ready` deltaP `18.9367` edge `0.0236` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7608` n `169` status `ready` deltaP `10.3196` edge `0.0289` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0919` n `169` status `ready` deltaP `8.7055` edge `0.0096` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1327` n `169` status `ready` deltaP `4.1172` edge `0.0007` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6099` n `136` status `ready` deltaP `1.6528` edge `0.0913` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.8158` n `169` status `ready` deltaP `-2.7265` edge `-0.0021` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8202` n `169` status `ready` deltaP `-4.8081` edge `-0.0095` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.1225` n `169` status `ready` deltaP `-1.034` edge `-0.0084` maxDD `-1.26`
- `market_context_high->equity_24h` score `-1.2093` n `136` status `ready` deltaP `-0.5633` edge `0.2173` maxDD `-21.1456`
- `market_context_high->metal_24h` score `-1.2288` n `136` status `ready` deltaP `-2.6009` edge `0.0431` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.2508` n `169` status `ready` deltaP `-2.0559` edge `-0.0035` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.5871` n `169` status `ready` deltaP `-9.2779` edge `-0.0395` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9255` n `169` status `ready` deltaP `-5.9046` edge `-0.0311` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.11` n `169` status `ready` deltaP `-10.705` edge `-0.1148` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.645` n `169` status `ready` deltaP `-10.5401` edge `-0.0601` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9588` n `169` status `ready` deltaP `-12.0577` edge `-0.1514` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4387` n `136` status `ready` deltaP `-11.9075` edge `-0.1462` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7603` n `136` status `ready` deltaP `-2.8902` edge `-0.128` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.576` n `136` status `ready` deltaP `-5.3752` edge `-0.1921` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
