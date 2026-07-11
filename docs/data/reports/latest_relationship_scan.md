# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T03:52:28.117500+00:00`
- Price records: `672`
- Market context records: `6352`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.0455` n `32` status `ready` deltaP `41.8403` edge `0.9896` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1641` n `32` status `ready` deltaP `51.0417` edge `0.1734` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4447` n `32` status `ready` deltaP `17.5347` edge `0.5309` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.09` n `32` status `ready` deltaP `42.4543` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7072` n `32` status `ready` deltaP `32.2917` edge `0.1142` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3512` n `32` status `ready` deltaP `28.2934` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5029` n `32` status `ready` deltaP `14.7268` edge `0.1412` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8862` n `32` status `ready` deltaP `11.3211` edge `0.0843` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.6844` n `198` status `ready` deltaP `14.1429` edge `0.0424` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `-0.0043` n `210` status `ready` deltaP `-7.552` edge `0.1508` maxDD `-3.7317`
- `market_context_high->index_4h` score `-0.0148` n `198` status `ready` deltaP `6.6149` edge `0.0223` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.593` n `210` status `ready` deltaP `3.8765` edge `0.0025` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.5934` n `129` status `ready` deltaP `-4.7965` edge `0.1423` maxDD `-6.2457`
- `market_context_high->commodity_1h` score `-0.6476` n `210` status `ready` deltaP `-2.0274` edge `-0.0012` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.6929` n `129` status `ready` deltaP `14.0423` edge `0.0744` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.7059` n `210` status `ready` deltaP `-0.5161` edge `-0.002` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7132` n `32` status `ready` deltaP `0.3472` edge `-0.0066` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7683` n `32` status `ready` deltaP `5.6325` edge `-0.0671` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.7815` n `32` status `ready` deltaP `-3.7425` edge `-0.0255` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.9723` n `210` status `ready` deltaP `5.2794` edge `0.0154` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
