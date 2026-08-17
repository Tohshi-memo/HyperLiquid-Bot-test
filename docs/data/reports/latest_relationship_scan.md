# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T06:37:48.918870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11803`

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

- `risk_on_high->unknown_1h` score `6.3267` n `35` status `ready` deltaP `2.4893` edge `0.5501` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `6.3267` n `35` status `ready` deltaP `2.4893` edge `0.5501` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.3261` n `79` status `ready` deltaP `6.1951` edge `0.2902` maxDD `-5.6792`
- `market_context_high->commodity_24h` score `2.1341` n `79` status `ready` deltaP `25.6022` edge `0.1077` maxDD `-2.3762`
- `market_context_high->index_24h` score `1.4829` n `79` status `ready` deltaP `21.7014` edge `-0.0211` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2731` n `79` status `ready` deltaP `15.4954` edge `0.0237` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.0983` n `35` status `ready` deltaP `12.1086` edge `0.0414` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0983` n `35` status `ready` deltaP `12.1086` edge `0.0414` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `1.0043` n `35` status `ready` deltaP `14.4055` edge `0.042` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `1.0043` n `35` status `ready` deltaP `14.4055` edge `0.042` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.868` n `35` status `ready` deltaP `14.5424` edge `0.0129` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.868` n `35` status `ready` deltaP `14.5424` edge `0.0129` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.4653` n `110` status `ready` deltaP `10.5876` edge `0.0479` maxDD `-1.7064`
- `risk_on_high->fx_1h` score `0.0617` n `35` status `ready` deltaP `4.2857` edge `0.0021` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0617` n `35` status `ready` deltaP `4.2857` edge `0.0021` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.1379` n `110` status `ready` deltaP `17.1037` edge `0.0152` maxDD `-4.5909`
- `risk_on_high->commodity_1h` score `-0.2229` n `35` status `ready` deltaP `-0.5175` edge `0.0118` maxDD `-0.4871`
- `risk_on_and_context->commodity_1h` score `-0.2229` n `35` status `ready` deltaP `-0.5175` edge `0.0118` maxDD `-0.4871`
- `market_context_high->crypto_major_4h` score `-0.3084` n `110` status `ready` deltaP `5.4545` edge `0.0449` maxDD `-4.6638`
- `market_context_high->fx_1h` score `-0.3394` n `122` status `ready` deltaP `-0.8197` edge `-0.001` maxDD `-0.2968`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
