# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T08:22:28.197534+00:00`
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

- `risk_on_high->unknown_1h` score `7.2999` n `35` status `ready` deltaP `2.4893` edge `0.6312` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2999` n `35` status `ready` deltaP `2.4893` edge `0.6312` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.7687` n `86` status `ready` deltaP `8.2768` edge `0.3132` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4164` n `86` status `ready` deltaP `20.6597` edge `-0.0197` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2692` n `33` status `ready` deltaP `17.4104` edge `0.0038` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2692` n `33` status `ready` deltaP `17.4104` edge `0.0038` maxDD `-0.1285`
- `market_context_high->equity_24h` score `1.145` n `86` status `ready` deltaP `14.8983` edge `0.017` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.1139` n `35` status `ready` deltaP `12.2583` edge `0.0417` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.1139` n `35` status `ready` deltaP `12.2583` edge `0.0417` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.9887` n `35` status `ready` deltaP `14.2558` edge `0.0417` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.9887` n `35` status `ready` deltaP `14.2558` edge `0.0417` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.868` n `35` status `ready` deltaP `14.5424` edge `0.0129` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.868` n `35` status `ready` deltaP `14.5424` edge `0.0129` maxDD `-0.3343`
- `market_context_high->commodity_24h` score `0.6602` n `86` status `ready` deltaP `20.6355` edge `0.0966` maxDD `-3.9619`
- `risk_on_high->crypto_major_4h` score `0.5495` n `33` status `ready` deltaP `6.8136` edge `0.0962` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.5495` n `33` status `ready` deltaP `6.8136` edge `0.0962` maxDD `-2.0278`
- `risk_on_high->commodity_4h` score `0.4191` n `33` status `ready` deltaP `2.5638` edge `0.0763` maxDD `-1.3437`
- `risk_on_and_context->commodity_4h` score `0.4191` n `33` status `ready` deltaP `2.5638` edge `0.0763` maxDD `-1.3437`
- `market_context_high->commodity_4h` score `0.1031` n `117` status `ready` deltaP `7.8474` edge `0.0415` maxDD `-2.4478`
- `risk_on_high->fx_1h` score `0.0858` n `35` status `ready` deltaP `4.7348` edge `0.0022` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
