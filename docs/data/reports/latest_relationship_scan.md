# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T05:22:31.784635+00:00`
- Price records: `672`
- Market context records: `7638`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->index_1h` score `0.0523` n `146` status `ready` deltaP `6.512` edge `0.0112` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1261` n `146` status `ready` deltaP `8.3053` edge `0.0245` maxDD `-4.0162`
- `market_context_high->equity_24h` score `-0.1626` n `145` status `ready` deltaP `16.8029` edge `0.3577` maxDD `-34.5784`
- `market_context_high->crypto_alt_1h` score `-0.1812` n `146` status `ready` deltaP `2.5039` edge `0.0233` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3515` n `145` status `ready` deltaP `9.2803` edge `0.0176` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3538` n `146` status `ready` deltaP `2.1288` edge `-0.0025` maxDD `-1.5641`
- `market_context_high->commodity_24h` score `-0.4251` n `145` status `ready` deltaP `11.1486` edge `0.0486` maxDD `-7.0012`
- `market_context_high->equity_1h` score `-0.476` n `146` status `ready` deltaP `5.5268` edge `0.0535` maxDD `-7.7764`
- `market_context_high->commodity_4h` score `-0.6181` n `146` status `ready` deltaP `2.3711` edge `0.0072` maxDD `-2.2943`
- `market_context_high->unknown_24h` score `-0.6335` n `146` status `ready` deltaP `8.0599` edge `0.0115` maxDD `-4.775`
- `market_context_high->index_4h` score `-0.6604` n `146` status `ready` deltaP `8.6045` edge `0.0281` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6769` n `146` status `ready` deltaP `0.6398` edge `0.0135` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.7134` n `146` status `ready` deltaP `-1.1724` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.8733` n `146` status `ready` deltaP `3.8068` edge `0.0616` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0462` n `146` status `ready` deltaP `9.589` edge `0.0697` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4739` n `146` status `ready` deltaP `-0.5352` edge `-0.0569` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.5` n `146` status `ready` deltaP `2.214` edge `0.2073` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7301` n `146` status `ready` deltaP `-2.5852` edge `0.0411` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.117` n `146` status `ready` deltaP `-3.2772` edge `0.0761` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.574` n `146` status `ready` deltaP `-6.3529` edge `-0.0037` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
