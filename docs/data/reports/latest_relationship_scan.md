# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T05:16:01.519420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8811`

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

- `market_context_high->equity_24h` score `3.5688` n `103` status `ready` deltaP `4.5729` edge `0.5729` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6995` n `103` status `ready` deltaP `13.2535` edge `0.1942` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3917` n `135` status `ready` deltaP `15.5352` edge `0.0797` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9424` n `143` status `ready` deltaP `11.84` edge `0.0339` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8105` n `103` status `ready` deltaP `21.4013` edge `0.0479` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5439` n `103` status `ready` deltaP `9.1002` edge `0.1622` maxDD `-5.9181`
- `market_context_high->fx_4h` score `-0.2535` n `135` status `ready` deltaP `8.4304` edge `-0.002` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.3313` n `143` status `ready` deltaP `3.8462` edge `-0.0037` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4953` n `143` status `ready` deltaP `-2.7406` edge `-0.0063` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6945` n `135` status `ready` deltaP `-2.5237` edge `-0.0117` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.704` n `143` status `ready` deltaP `-5.0374` edge `-0.0071` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9781` n `143` status `ready` deltaP `-0.3371` edge `0.0036` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.1089` n `135` status `ready` deltaP `-3.3717` edge `-0.0188` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0235` n `143` status `ready` deltaP `-10.8821` edge `-0.0319` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.7039` n `135` status `ready` deltaP `-2.8049` edge `-0.0729` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2284` n `143` status `ready` deltaP `-10.9868` edge `-0.0637` maxDD `-7.2335`
- `market_context_high->crypto_major_24h` score `-3.2923` n `103` status `ready` deltaP `6.2197` edge `-0.0664` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.9168` n `135` status `ready` deltaP `-8.1233` edge `-0.1066` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.5634` n `103` status `ready` deltaP `-12.4461` edge `-0.153` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.3772` n `143` status `ready` deltaP `-6.7931` edge `-0.6081` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
