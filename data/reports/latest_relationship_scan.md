# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T08:37:29.236733+00:00`
- Price records: `672`
- Market context records: `6266`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11096`

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

- `news_risk_high->crypto_alt_24h` score `14.9589` n `32` status `ready` deltaP `42.8879` edge `0.9754` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9398` n `32` status `ready` deltaP `50.5172` edge `0.1582` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1769` n `32` status `ready` deltaP `43.8262` edge `0.0605` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.8681` n `32` status `ready` deltaP `16.3147` edge `0.4651` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4498` n `32` status `ready` deltaP `25.7543` edge `0.053` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.314` n `32` status `ready` deltaP `27.8443` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.1126` n `197` status `ready` deltaP `2.8299` edge `0.258` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3564` n `32` status `ready` deltaP `13.9783` edge `0.1274` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.3483` n `192` status `ready` deltaP `-1.2322` edge `0.3738` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7951` n `32` status `ready` deltaP `10.5726` edge `0.0776` maxDD `-1.6923`
- `market_context_high->equity_4h` score `-0.1177` n `192` status `ready` deltaP `4.8018` edge `0.0499` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1423` n `32` status `ready` deltaP `9.5259` edge `0.0054` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2689` n `197` status `ready` deltaP `1.5753` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3276` n `192` status `ready` deltaP `17.4964` edge `0.0982` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.4922` n `192` status `ready` deltaP `4.281` edge `0.0271` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.5772` n `197` status `ready` deltaP `-0.6117` edge `0.002` maxDD `-0.682`
- `news_risk_high->metal_1h` score `-0.7006` n `32` status `ready` deltaP `-2.3952` edge `-0.0241` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7809` n `197` status `ready` deltaP `6.0199` edge `0.035` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.8719` n `197` status `ready` deltaP `1.4119` edge `-0.0022` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9049` n `197` status `ready` deltaP `4.1909` edge `0.0328` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
