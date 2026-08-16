# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T11:22:27.795283+00:00`
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

- `market_context_high->unknown_24h` score `198.2068` n `88` status `ready` deltaP `-21.512` edge `25.8229` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `16.2317` n `31` status `ready` deltaP `30.0067` edge `1.1684` maxDD `-0.5979`
- `news_risk_high->equity_4h` score `8.1622` n `31` status `ready` deltaP `37.3476` edge `0.4312` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5181` n `88` status `ready` deltaP `41.3037` edge `0.3569` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.96` n `31` status `ready` deltaP `30.5556` edge `0.1263` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.0236` n `31` status `ready` deltaP `8.6102` edge `0.1431` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.9071` n `115` status `ready` deltaP `18.4252` edge `0.0832` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7981` n `31` status `ready` deltaP `19.999` edge `0.0297` maxDD `-0.0546`
- `news_risk_high->index_1h` score `0.3103` n `31` status `ready` deltaP `4.7035` edge `0.0171` maxDD `-0.141`
- `news_risk_high->fx_4h` score `0.1297` n `31` status `ready` deltaP `6.7417` edge `-0.0064` maxDD `-0.0863`
- `market_context_high->fx_4h` score `-0.0222` n `115` status `ready` deltaP `7.443` edge `0.008` maxDD `-0.504`
- `market_context_high->commodity_1h` score `-0.0615` n `125` status `ready` deltaP `2.3557` edge `0.0203` maxDD `-0.624`
- `news_risk_high->fx_1h` score `-0.1205` n `31` status `ready` deltaP `2.5932` edge `-0.0018` maxDD `-0.1414`
- `market_context_high->fx_1h` score `-0.1799` n `125` status `ready` deltaP `0.5545` edge `0.0014` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5276` n `125` status `ready` deltaP `1.5042` edge `-0.0061` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6653` n `31` status `ready` deltaP `-6.9345` edge `-0.0122` maxDD `-0.8156`
- `news_risk_high->commodity_1h` score `-0.6729` n `31` status `ready` deltaP `-1.2314` edge `-0.0185` maxDD `-0.6824`
- `market_context_high->index_1h` score `-0.7936` n `125` status `ready` deltaP `-6.9868` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-1.0918` n `115` status `ready` deltaP `4.9523` edge `-0.0156` maxDD `-4.5909`
- `market_context_high->index_4h` score `-1.2685` n `115` status `ready` deltaP `-10.8285` edge `-0.0092` maxDD `-0.8328`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
