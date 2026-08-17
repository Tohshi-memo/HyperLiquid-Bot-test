# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T07:07:27.187329+00:00`
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

- `risk_on_high->unknown_1h` score `7.2975` n `35` status `ready` deltaP `2.4893` edge `0.631` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2975` n `35` status `ready` deltaP `2.4893` edge `0.631` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.5248` n `81` status `ready` deltaP `6.848` edge `0.3024` maxDD `-5.6792`
- `market_context_high->commodity_24h` score `1.7946` n `81` status `ready` deltaP `24.0741` edge `0.1036` maxDD `-2.8299`
- `market_context_high->index_24h` score `1.4786` n `81` status `ready` deltaP `21.5278` edge `-0.0203` maxDD `0.0`
- `market_context_high->equity_24h` score `1.24` n `81` status `ready` deltaP `15.3357` edge `0.022` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.0923` n `35` status `ready` deltaP `12.1086` edge `0.0409` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0923` n `35` status `ready` deltaP `12.1086` edge `0.0409` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `1.0031` n `35` status `ready` deltaP `14.4055` edge `0.0419` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `1.0031` n `35` status `ready` deltaP `14.4055` edge `0.0419` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8668` n `35` status `ready` deltaP `14.5424` edge `0.0128` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8668` n `35` status `ready` deltaP `14.5424` edge `0.0128` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.3822` n `112` status `ready` deltaP `9.7561` edge `0.0456` maxDD `-1.9309`
- `risk_on_high->fx_1h` score `0.078` n `35` status `ready` deltaP `4.5851` edge `0.0022` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.078` n `35` status `ready` deltaP `4.5851` edge `0.0022` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.1195` n `112` status `ready` deltaP `17.3345` edge `0.0152` maxDD `-4.5909`
- `risk_on_high->commodity_1h` score `-0.1941` n `35` status `ready` deltaP `-0.2181` edge `0.0122` maxDD `-0.4871`
- `risk_on_and_context->commodity_1h` score `-0.1941` n `35` status `ready` deltaP `-0.2181` edge `0.0122` maxDD `-0.4871`
- `market_context_high->crypto_major_4h` score `-0.2571` n `112` status `ready` deltaP `5.9451` edge `0.0482` maxDD `-4.6638`
- `market_context_high->unknown_1h` score `-0.3505` n `124` status `ready` deltaP `2.2359` edge `-0.0044` maxDD `-0.8437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
