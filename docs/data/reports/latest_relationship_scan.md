# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T01:37:28.163379+00:00`
- Price records: `672`
- Market context records: `6560`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9872`

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

- `market_context_high->unknown_24h` score `6.3059` n `144` status `ready` deltaP `11.3735` edge `0.7797` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.8143` n `210` status `ready` deltaP `-4.6806` edge `0.2725` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3803` n `144` status `ready` deltaP `13.4773` edge `0.212` maxDD `-5.2791`
- `market_context_high->index_4h` score `-0.0346` n `200` status `ready` deltaP `10.689` edge `0.0215` maxDD `-1.7754`
- `market_context_high->fx_1h` score `-0.3386` n `210` status `ready` deltaP `1.1577` edge `-0.0004` maxDD `-0.7249`
- `market_context_high->crypto_alt_4h` score `-0.3624` n `200` status `ready` deltaP `7.8476` edge `0.0957` maxDD `-9.8917`
- `market_context_high->crypto_major_1h` score `-0.4329` n `210` status `ready` deltaP `7.0473` edge `0.0241` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4815` n `210` status `ready` deltaP `6.7893` edge `0.0243` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5822` n `210` status `ready` deltaP `-0.2595` edge `-0.0046` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5981` n `210` status `ready` deltaP `-1.1292` edge `0.0028` maxDD `-0.7564`
- `market_context_high->crypto_major_4h` score `-0.6266` n `200` status `ready` deltaP `10.5671` edge `0.0866` maxDD `-12.6576`
- `market_context_high->equity_4h` score `-1.0959` n `200` status `ready` deltaP `8.7195` edge `0.0343` maxDD `-9.3669`
- `market_context_high->unknown_4h` score `-1.099` n `200` status `ready` deltaP `-16.4268` edge `0.2585` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-1.1765` n `210` status `ready` deltaP `2.0816` edge `-0.0009` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2284` n `210` status `ready` deltaP `-3.128` edge `-0.0008` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.3909` n `200` status `ready` deltaP `-2.3171` edge `-0.0134` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.4422` n `200` status `ready` deltaP `0.4512` edge `0.0324` maxDD `-3.291`
- `market_context_high->metal_24h` score `-1.9733` n `144` status `ready` deltaP `5.966` edge `0.0888` maxDD `-5.7746`
- `market_context_high->fx_4h` score `-2.9168` n `200` status `ready` deltaP `-2.2134` edge `-0.0071` maxDD `-3.3635`
- `market_context_high->fx_24h` score `-3.8295` n `144` status `ready` deltaP `-4.6144` edge `-0.0067` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
