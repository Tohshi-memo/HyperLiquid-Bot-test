# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T07:52:31.813192+00:00`
- Price records: `672`
- Market context records: `8600`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4748.778` n `64` status `ready` deltaP `34.7222` edge `395.5421` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8354` n `64` status `ready` deltaP `20.503` edge `0.4093` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.253` n `64` status `ready` deltaP `19.2454` edge `0.0785` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7828` n `64` status `ready` deltaP `16.701` edge `0.0849` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5343` n `62` status `ready` deltaP `11.3788` edge `0.1477` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0455` n `64` status `ready` deltaP `7.0503` edge `0.1646` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4079` n `64` status `ready` deltaP `7.8125` edge `0.0529` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.4063` n `64` status `ready` deltaP `10.9756` edge `0.1181` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3594` n `64` status `ready` deltaP `7.064` edge `0.0502` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1134` n `64` status `ready` deltaP `5.7354` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.1106` n `64` status `ready` deltaP `12.3857` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.0633` n `64` status `ready` deltaP `3.5442` edge `0.0321` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.034` n `64` status `ready` deltaP `4.07` edge `0.0089` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0577` n `62` status `ready` deltaP `9.2103` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1347` n `64` status `ready` deltaP `3.256` edge `0.0074` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2513` n `62` status `ready` deltaP `2.6608` edge `0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.2795` n `62` status `ready` deltaP `4.7566` edge `-0.005` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5688` n `62` status `ready` deltaP `-3.2258` edge `0.0113` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7309` n `62` status `ready` deltaP `1.0962` edge `-0.0153` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9757` n `62` status `ready` deltaP `-2.994` edge `-0.0119` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
