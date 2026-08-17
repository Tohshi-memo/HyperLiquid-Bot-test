# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T05:46:58.304271+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `risk_on_high->unknown_1h` score `3.2667` n `35` status `ready` deltaP `2.4893` edge `0.2951` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `3.2667` n `35` status `ready` deltaP `2.4893` edge `0.2951` maxDD `-0.8243`
- `market_context_high->commodity_24h` score `2.6887` n `76` status `ready` deltaP `28.0793` edge `0.1157` maxDD `-1.6405`
- `market_context_high->crypto_major_24h` score `2.0539` n `76` status `ready` deltaP `5.1169` edge `0.2747` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4685` n `76` status `ready` deltaP `21.7014` edge `-0.0223` maxDD `0.0`
- `market_context_high->equity_24h` score `1.3292` n `76` status `ready` deltaP `15.7164` edge `0.0269` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.0684` n `35` status `ready` deltaP `11.9589` edge `0.0399` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0684` n `35` status `ready` deltaP `11.9589` edge `0.0399` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.9839` n `35` status `ready` deltaP `14.4055` edge `0.0403` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.9839` n `35` status `ready` deltaP `14.4055` edge `0.0403` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8668` n `35` status `ready` deltaP `14.5424` edge `0.0128` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8668` n `35` status `ready` deltaP `14.5424` edge `0.0128` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.6408` n `107` status `ready` deltaP `11.9145` edge `0.0536` maxDD `-1.0704`
- `risk_on_high->fx_1h` score `0.043` n `35` status `ready` deltaP `3.9863` edge `0.0017` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.043` n `35` status `ready` deltaP `3.9863` edge `0.0017` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.1808` n `107` status `ready` deltaP `16.5674` edge `0.0152` maxDD `-4.5909`
- `risk_on_high->commodity_1h` score `-0.2238` n `35` status `ready` deltaP `-0.6672` edge `0.0123` maxDD `-0.4533`
- `risk_on_and_context->commodity_1h` score `-0.2238` n `35` status `ready` deltaP `-0.6672` edge `0.0123` maxDD `-0.4533`
- `market_context_high->fx_1h` score `-0.3365` n `119` status `ready` deltaP `-0.7196` edge `-0.0013` maxDD `-0.2968`
- `market_context_high->crypto_major_4h` score `-0.4465` n `107` status `ready` deltaP `4.358` edge `0.0345` maxDD `-4.6638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
