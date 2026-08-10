# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T05:37:30.631758+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10952`

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

- `market_context_high->commodity_4h` score `1.3816` n `166` status `ready` deltaP `15.5745` edge `0.0786` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.0449` n `136` status `ready` deltaP `20.7516` edge `0.0295` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.8291` n `169` status `ready` deltaP `10.9184` edge `0.0306` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.14` n `166` status `ready` deltaP `9.0068` edge `0.0116` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0681` n `169` status `ready` deltaP `5.1651` edge `0.002` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6249` n `136` status `ready` deltaP `1.7054` edge `0.0897` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7572` n `169` status `ready` deltaP `-1.978` edge `-0.0022` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8179` n `169` status `ready` deltaP `-4.8081` edge `-0.0092` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.0397` n `166` status `ready` deltaP `-0.0882` edge `-0.0078` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.186` n `136` status `ready` deltaP `-2.2161` edge `0.0441` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.2017` n `169` status `ready` deltaP `-1.4571` edge `-0.0034` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.4741` n `169` status `ready` deltaP `-7.9306` edge `-0.034` maxDD `-5.5029`
- `market_context_high->equity_24h` score `-1.7864` n `136` status `ready` deltaP `-2.2569` edge `0.1805` maxDD `-21.1456`
- `market_context_high->metal_4h` score `-1.9392` n `166` status `ready` deltaP `-6.0186` edge `-0.0321` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-2.9897` n `166` status `ready` deltaP `-9.7487` edge `-0.1094` maxDD `-7.7118`
- `market_context_high->crypto_major_1h` score `-3.4688` n `169` status `ready` deltaP `-9.1928` edge `-0.0544` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.813` n `166` status `ready` deltaP `-10.6487` edge `-0.1421` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.369` n `136` status `ready` deltaP `-11.8771` edge `-0.1406` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8148` n `136` status `ready` deltaP `-2.4918` edge `-0.1352` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5347` n `169` status `ready` deltaP `-4.5876` edge `-0.5516` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
