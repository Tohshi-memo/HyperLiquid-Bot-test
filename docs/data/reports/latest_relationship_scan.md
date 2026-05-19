# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T02:22:20.216140+00:00`
- Price records: `672`
- Market context records: `1177`
- Flow alert records: `5292`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `20.0445` n `144` status `ready` deltaP `44.9652` edge `1.4838` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.7454` n `144` status `ready` deltaP `22.2223` edge `0.8656` maxDD `-15.1306`
- `market_context_high->equity_24h` score `6.0505` n `144` status `ready` deltaP `18.9236` edge `0.5066` maxDD `-8.2841`
- `market_context_high->metal_24h` score `5.4656` n `144` status `ready` deltaP `-2.7778` edge `0.6407` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.0227` n `144` status `ready` deltaP `18.5764` edge `0.3505` maxDD `-3.4627`
- `market_context_high->equity_4h` score `2.7036` n `151` status `ready` deltaP `13.9991` edge `0.1983` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2486` n `151` status `ready` deltaP `10.0731` edge `0.1052` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5927` n `151` status `ready` deltaP `8.4129` edge `0.025` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4522` n `151` status `ready` deltaP `3.9675` edge `0.049` maxDD `-1.3546`
- `market_context_high->unknown_4h` score `0.4197` n `151` status `ready` deltaP `6.2439` edge `0.115` maxDD `-6.7322`
- `market_context_high->fx_1h` score `0.106` n `151` status `ready` deltaP `8.1463` edge `0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0602` n `151` status `ready` deltaP `8.2257` edge `0.145` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0825` n `151` status `ready` deltaP `5.8195` edge `0.0272` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.263` n `151` status `ready` deltaP `7.0528` edge `-0.0079` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.5177` n `151` status `ready` deltaP `1.4147` edge `0.0317` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8688` n `151` status `ready` deltaP `-3.8555` edge `-0.0049` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0605` n `151` status `ready` deltaP `-4.5469` edge `-0.006` maxDD `-1.6381`
- `market_context_high->unknown_24h` score `-1.1968` n `144` status `ready` deltaP `4.3403` edge `0.1443` maxDD `-10.1706`
- `market_context_high->crypto_alt_4h` score `-1.3735` n `151` status `ready` deltaP `3.6151` edge `0.0963` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.8741` n `151` status `ready` deltaP `5.0446` edge `-0.0785` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
