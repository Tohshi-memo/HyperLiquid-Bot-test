# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T12:37:26.226986+00:00`
- Price records: `672`
- Market context records: `7669`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14689`

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

- `market_context_high->index_1h` score `0.018` n `146` status `ready` deltaP `5.9114` edge `0.0108` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1807` n `146` status `ready` deltaP `8.0059` edge `0.0195` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2482` n `146` status `ready` deltaP `2.0548` edge `0.0177` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3232` n `145` status `ready` deltaP `9.4545` edge `0.0188` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4327` n `146` status `ready` deltaP `0.7774` edge `-0.0036` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5603` n `146` status `ready` deltaP `4.6259` edge `0.0487` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6403` n `146` status `ready` deltaP `1.0889` edge `0.0152` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.7543` n `146` status `ready` deltaP `-1.6229` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.7593` n `146` status `ready` deltaP `7.2284` edge `0.0246` maxDD `-3.2774`
- `market_context_high->commodity_4h` score `-0.7773` n `146` status `ready` deltaP `0.995` edge `0.0031` maxDD `-2.2943`
- `market_context_high->crypto_alt_4h` score `-1.0493` n `146` status `ready` deltaP `2.2824` edge `0.0492` maxDD `-9.5815`
- `market_context_high->commodity_24h` score `-1.1404` n `145` status `ready` deltaP `8.0128` edge `0.0099` maxDD `-7.0012`
- `market_context_high->crypto_major_4h` score `-1.1995` n `146` status `ready` deltaP `9.1317` edge `0.0531` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5373` n `146` status `ready` deltaP `-1.5831` edge `-0.0552` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7115` n `146` status `ready` deltaP `-2.7376` edge `0.0445` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.9467` n `146` status `ready` deltaP `-0.6912` edge `0.1694` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.2964` n `146` status `ready` deltaP `-3.2772` edge `0.0531` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6618` n `146` status `ready` deltaP `-7.2703` edge `-0.0049` maxDD `-2.1425`
- `market_context_high->equity_24h` score `-2.7211` n `145` status `ready` deltaP `11.9248` edge `0.0622` maxDD `-34.5784`
- `market_context_high->index_24h` score `-3.672` n `145` status `ready` deltaP `-21.7818` edge `-0.0408` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
