# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T05:52:19.866051+00:00`
- Price records: `672`
- Market context records: `1498`
- Flow alert records: `6224`
- Minimum samples: `30`
- Pattern count: `96`

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

- `market_context_high->metal_24h` score `12.8547` n `170` status `ready` deltaP `21.6258` edge `1.0271` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.2856` n `170` status `ready` deltaP `28.9645` edge `0.949` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.269` n `170` status `ready` deltaP `27.306` edge `0.7869` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8421` n `170` status `ready` deltaP `20.2369` edge `0.2939` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.027` n `170` status `ready` deltaP `13.5049` edge `0.3949` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.173` n `196` status `ready` deltaP `6.6669` edge `0.1363` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9939` n `170` status `ready` deltaP `19.6691` edge `0.0566` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.2688` n `196` status `ready` deltaP `1.1731` edge `0.0298` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2821` n `196` status `ready` deltaP `2.3097` edge `0.0076` maxDD `-1.7205`
- `market_context_high->crypto_alt_4h` score `-0.5518` n `196` status `ready` deltaP `9.9707` edge `0.2195` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.5521` n `196` status `ready` deltaP `-0.6538` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6108` n `196` status `ready` deltaP `1.2098` edge `0.0434` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.7519` n `196` status `ready` deltaP `5.5023` edge `0.0005` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.8555` n `196` status `ready` deltaP `5.6838` edge `0.1617` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-0.9687` n `196` status `ready` deltaP `-3.3008` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.0277` n `196` status `ready` deltaP `-2.3768` edge `0.0391` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-1.0409` n `196` status `ready` deltaP `-1.3137` edge `0.011` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.1274` n `196` status `ready` deltaP `11.8405` edge `0.0963` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.2064` n `196` status `ready` deltaP `-0.8096` edge `-0.003` maxDD `-4.7041`
- `market_context_high->commodity_4h` score `-4.4048` n `196` status `ready` deltaP `-15.0136` edge `-0.093` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
