# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T11:07:30.519324+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `197.437` n `88` status `ready` deltaP `-21.512` edge `25.7242` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `15.2096` n `32` status `ready` deltaP `27.2569` edge `1.1077` maxDD `-0.756`
- `news_risk_high->equity_4h` score `7.9904` n `32` status `ready` deltaP `37.1951` edge `0.4179` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5097` n `88` status `ready` deltaP `41.3037` edge `0.3562` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.8916` n `32` status `ready` deltaP `30.5556` edge `0.1206` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.0322` n `32` status `ready` deltaP `9.4686` edge `0.1381` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.9142` n `114` status `ready` deltaP `18.3488` edge `0.0843` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8131` n `32` status `ready` deltaP `20.3506` edge `0.0286` maxDD `-0.0546`
- `news_risk_high->fx_4h` score `0.1882` n `32` status `ready` deltaP `7.8506` edge `-0.0063` maxDD `-0.0863`
- `news_risk_high->index_1h` score `0.1607` n `32` status `ready` deltaP `2.9379` edge `0.0164` maxDD `-0.141`
- `market_context_high->fx_4h` score `-0.0365` n `114` status `ready` deltaP `7.1379` edge `0.0082` maxDD `-0.504`
- `market_context_high->commodity_1h` score `-0.0603` n `125` status `ready` deltaP `2.3557` edge `0.0204` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.1721` n `125` status `ready` deltaP `0.7042` edge `0.0014` maxDD `-0.2527`
- `news_risk_high->fx_1h` score `-0.2026` n `32` status `ready` deltaP `1.0292` edge `-0.0019` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5354` n `125` status `ready` deltaP `1.3545` edge `-0.0061` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.5808` n `32` status `ready` deltaP `-5.3705` edge `-0.0118` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7858` n `125` status `ready` deltaP `-6.8371` edge `-0.003` maxDD `-0.5064`
- `news_risk_high->commodity_1h` score `-0.8368` n `32` status `ready` deltaP `-2.8443` edge `-0.0208` maxDD `-0.7313`
- `market_context_high->metal_4h` score `-1.1128` n `114` status `ready` deltaP `4.5785` edge `-0.0158` maxDD `-4.5909`
- `news_risk_high->metal_4h` score `-1.2403` n `32` status `ready` deltaP `-5.564` edge `-0.0326` maxDD `-2.4791`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
