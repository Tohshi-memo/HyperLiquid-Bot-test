# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T15:22:30.590703+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13438`

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

- `market_context_high->unknown_24h` score `17868.1829` n `56` status `ready` deltaP `8.596` edge `1488.9781` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `10511.3592` n `33` status `ready` deltaP `13.2497` edge `875.864` maxDD `-0.1252`
- `risk_on_and_context->unknown_24h` score `10511.3592` n `33` status `ready` deltaP `13.2497` edge `875.864` maxDD `-0.1252`
- `news_risk_high->unknown_1h` score `421.7607` n `82` status `ready` deltaP `-4.8014` edge `35.2209` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.3625` n `82` status `ready` deltaP `34.9958` edge `1.3457` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3352` n `82` status `ready` deltaP `38.0236` edge `1.4215` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.613` n `82` status `ready` deltaP `25.0294` edge `0.7289` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.8566` n `82` status `ready` deltaP `48.8015` edge `0.2637` maxDD `-0.0797`
- `risk_on_high->crypto_alt_24h` score `5.4113` n `33` status `ready` deltaP `21.766` edge `0.6032` maxDD `-2.6977`
- `risk_on_and_context->crypto_alt_24h` score `5.4113` n `33` status `ready` deltaP `21.766` edge `0.6032` maxDD `-2.6977`
- `market_context_high->crypto_alt_24h` score `4.9471` n `56` status `ready` deltaP `16.3547` edge `0.6248` maxDD `-5.2999`
- `news_risk_high->metal_24h` score `4.5576` n `82` status `ready` deltaP `24.2431` edge `0.2636` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.163` n `56` status `ready` deltaP `39.8276` edge `0.0814` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.1414` n `33` status `ready` deltaP `39.8276` edge `0.0796` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.1414` n `33` status `ready` deltaP `39.8276` edge `0.0796` maxDD `0.0`
- `market_context_high->metal_24h` score `2.2662` n `56` status `ready` deltaP `17.0567` edge `0.1318` maxDD `-0.8664`
- `risk_on_high->index_24h` score `1.6934` n `33` status `ready` deltaP `37.3825` edge `0.0354` maxDD `-2.4013`
- `risk_on_and_context->index_24h` score `1.6934` n `33` status `ready` deltaP `37.3825` edge `0.0354` maxDD `-2.4013`
- `market_context_high->index_24h` score `1.2992` n `56` status `ready` deltaP `36.0838` edge `0.0391` maxDD `-3.7145`
- `risk_on_high->equity_24h` score `0.9967` n `33` status `ready` deltaP `28.2445` edge `0.1691` maxDD `-15.3687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
