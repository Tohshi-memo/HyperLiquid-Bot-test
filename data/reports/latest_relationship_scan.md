# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T09:52:37.281757+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2005` n `85` status `ready` deltaP `7.75` edge `0.2525` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5331` n `85` status `ready` deltaP `16.7356` edge `0.2683` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0435` n `97` status `ready` deltaP `9.175` edge `0.0562` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7864` n `97` status `ready` deltaP `9.874` edge `0.1018` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.7314` n `97` status `ready` deltaP `14.3748` edge `0.0227` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6542` n `97` status `ready` deltaP `12.8017` edge `0.0079` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5255` n `97` status `ready` deltaP `9.4605` edge `0.0034` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.3975` n `97` status `ready` deltaP `11.2459` edge `0.1077` maxDD `-5.5373`
- `market_context_high->metal_1h` score `0.0041` n `97` status `ready` deltaP `4.5064` edge `0.009` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.0704` n `85` status `ready` deltaP `13.822` edge `-0.0792` maxDD `-0.1719`
- `market_context_high->equity_4h` score `-0.1878` n `97` status `ready` deltaP `1.4253` edge `0.0653` maxDD `-2.5696`
- `market_context_high->fx_4h` score `-0.2731` n `97` status `ready` deltaP `2.3526` edge `-0.0002` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.2824` n `97` status `ready` deltaP `3.3088` edge `0.0219` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.4109` n `97` status `ready` deltaP `3.6522` edge `0.008` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4312` n `97` status `ready` deltaP `1.8288` edge `0.017` maxDD `-2.7581`
- `market_context_high->fx_1h` score `-0.4767` n `97` status `ready` deltaP `-3.8907` edge `0.001` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.6211` n `97` status `ready` deltaP `0.5752` edge `0.0099` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9112` n `97` status `ready` deltaP `-7.2829` edge `-0.007` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-2.0038` n `85` status `ready` deltaP `-7.3442` edge `0.0167` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.4626` n `85` status `ready` deltaP `-15.2166` edge `-0.1824` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
