# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T10:47:57.753005+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11572`

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

- `market_context_high->equity_24h` score `6.1068` n `81` status `ready` deltaP `1.9483` edge `0.8019` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.834` n `81` status `ready` deltaP `13.4838` edge `0.2872` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7147` n `81` status `ready` deltaP `33.6034` edge `0.0658` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.4312` n `103` status `ready` deltaP `13.5241` edge `0.0964` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1688` n `81` status `ready` deltaP `7.0216` edge `0.2019` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.9938` n `103` status `ready` deltaP `11.5371` edge `0.0402` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.3885` n `103` status `ready` deltaP `4.1975` edge `0.0225` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.496` n `103` status `ready` deltaP `-3.3341` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5106` n `103` status `ready` deltaP `1.9054` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5772` n `103` status `ready` deltaP `-0.5091` edge `-0.0101` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.681` n `103` status `ready` deltaP `-4.7584` edge `-0.006` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8895` n `103` status `ready` deltaP `0.8702` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0819` n `103` status `ready` deltaP `-3.6778` edge `-0.0133` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7219` n `103` status `ready` deltaP `4.2653` edge `-0.0382` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.8163` n `103` status `ready` deltaP `-9.8308` edge `-0.0229` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.3379` n `103` status `ready` deltaP `-6.8368` edge `-0.0496` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6598` n `81` status `ready` deltaP `6.6937` edge `-0.1362` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.8029` n `81` status `ready` deltaP `-23.1674` edge `-0.1888` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.8745` n `103` status `ready` deltaP `-9.207` edge `-0.0963` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.5336` n `103` status `ready` deltaP `-11.8148` edge `-0.2099` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
