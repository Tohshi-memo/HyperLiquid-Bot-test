# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T08:52:30.538756+00:00`
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

- `market_context_high->commodity_4h` score `1.096` n `169` status `ready` deltaP `13.4545` edge `0.0731` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8337` n `136` status `ready` deltaP `18.9367` edge `0.024` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7776` n `169` status `ready` deltaP `10.4693` edge `0.0293` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0931` n `169` status `ready` deltaP `8.7055` edge `0.0097` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1241` n `169` status `ready` deltaP `4.2669` edge `0.0008` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6099` n `136` status `ready` deltaP `1.6528` edge `0.0913` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.817` n `169` status `ready` deltaP `-2.7265` edge `-0.0022` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8288` n `169` status `ready` deltaP `-4.9578` edge `-0.0096` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.1091` n `169` status `ready` deltaP `-0.8818` edge `-0.0083` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.23` n `136` status `ready` deltaP `-2.6009` edge `0.043` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.252` n `169` status `ready` deltaP `-2.0559` edge `-0.0036` maxDD `-4.6286`
- `market_context_high->equity_24h` score `-1.2532` n `136` status `ready` deltaP `-0.7366` edge `0.2148` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5863` n `169` status `ready` deltaP `-9.2779` edge `-0.0394` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.916` n `169` status `ready` deltaP `-5.7524` edge `-0.0309` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.095` n `169` status `ready` deltaP `-10.5527` edge `-0.1139` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.6438` n `169` status `ready` deltaP `-10.5401` edge `-0.06` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9423` n `169` status `ready` deltaP `-11.9055` edge `-0.1503` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4411` n `136` status `ready` deltaP `-11.9075` edge `-0.1464` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7747` n `136` status `ready` deltaP `-2.8902` edge `-0.1292` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5729` n `136` status `ready` deltaP `-5.3752` edge `-0.1917` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
