# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T08:07:32.714793+00:00`
- Price records: `672`
- Market context records: `8601`
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

- `news_risk_high->unknown_24h` score `4748.6772` n `64` status `ready` deltaP `34.7222` edge `395.5337` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8196` n `64` status `ready` deltaP `20.3506` edge `0.409` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2396` n `64` status `ready` deltaP `19.093` edge `0.0784` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7685` n `64` status `ready` deltaP `16.5513` edge `0.0847` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5379` n `62` status `ready` deltaP `11.3788` edge `0.148` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0573` n `64` status `ready` deltaP `7.2027` edge `0.1651` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4095` n `64` status `ready` deltaP `7.8125` edge `0.0531` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.4086` n `64` status `ready` deltaP `10.9756` edge `0.1184` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3602` n `64` status `ready` deltaP `7.064` edge `0.0503` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.1106` n `64` status `ready` deltaP `12.3857` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.1056` n `64` status `ready` deltaP `5.5857` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0554` n `64` status `ready` deltaP `3.3918` edge `0.0321` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0255` n `64` status `ready` deltaP `3.9203` edge `0.0088` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0577` n `62` status `ready` deltaP `9.2103` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1479` n `64` status `ready` deltaP `3.1063` edge `0.0073` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2591` n `62` status `ready` deltaP `2.5111` edge `0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.2795` n `62` status `ready` deltaP `4.7566` edge `-0.005` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5673` n `62` status `ready` deltaP `-3.2258` edge `0.0115` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7441` n `62` status `ready` deltaP `0.9465` edge `-0.0154` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9889` n `62` status `ready` deltaP `-3.1437` edge `-0.012` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
