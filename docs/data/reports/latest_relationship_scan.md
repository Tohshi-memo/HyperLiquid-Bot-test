# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T10:07:24.977403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10800`

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

- `market_context_high->equity_4h` score `1.9493` n `96` status `ready` deltaP `10.5437` edge `0.181` maxDD `-2.4411`
- `market_context_high->equity_1h` score `0.5978` n `103` status `ready` deltaP `9.6593` edge `0.0504` maxDD `-2.5318`
- `market_context_high->metal_4h` score `0.4354` n `96` status `ready` deltaP `13.0589` edge `0.0068` maxDD `-1.273`
- `market_context_high->index_1h` score `0.3984` n `103` status `ready` deltaP `10.7116` edge `0.0052` maxDD `-0.4726`
- `market_context_high->index_4h` score `0.1582` n `96` status `ready` deltaP `8.562` edge `0.0216` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.0048` n `96` status `ready` deltaP `5.5556` edge `0.1469` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0676` n `96` status `ready` deltaP `5.8181` edge `0.0028` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1421` n `103` status `ready` deltaP `3.5478` edge `0.0032` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.1735` n `103` status `ready` deltaP `1.4607` edge `0.0039` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.2975` n `103` status `ready` deltaP `7.1144` edge `-0.0495` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4073` n `103` status `ready` deltaP `1.747` edge `0.0163` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.4597` n `103` status `ready` deltaP `3.1713` edge `0.0044` maxDD `-2.7581`
- `market_context_high->unknown_24h` score `-0.8109` n `96` status `ready` deltaP `17.7083` edge `-0.135` maxDD `-1.0505`
- `market_context_high->commodity_1h` score `-0.8337` n `103` status `ready` deltaP `-7.2132` edge `-0.0022` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.9588` n `96` status `ready` deltaP `-4.9034` edge `-0.0052` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-2.3604` n `96` status `ready` deltaP `3.6585` edge `-0.0941` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.7111` n `96` status `ready` deltaP `5.6656` edge `-0.1616` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.4559` n `96` status `ready` deltaP `-18.4027` edge `-0.007` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7591` n `96` status `ready` deltaP `-0.5209` edge `-0.0617` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.633` n `96` status `ready` deltaP `-18.4028` edge `-0.1405` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
