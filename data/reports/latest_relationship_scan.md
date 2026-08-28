# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T17:22:32.629262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `54.0936` n `50` status `ready` deltaP `12.825` edge `4.4223` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.3051` n `50` status `ready` deltaP `43.487` edge `2.4463` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.117` n `56` status `ready` deltaP `23.5845` edge `0.7834` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.6815` n `50` status `ready` deltaP `30.1005` edge `0.3656` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `5.1523` n `50` status `ready` deltaP `22.6482` edge `0.3277` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.3242` n `50` status `ready` deltaP `43.4073` edge `0.0752` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0662` n `56` status `ready` deltaP `47.2778` edge `0.0327` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.5416` n `64` status `ready` deltaP `12.7246` edge `0.246` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `3.4023` n `120` status `ready` deltaP `6.1583` edge `0.3157` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.1414` n `120` status `ready` deltaP `28.7406` edge `0.1721` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.6832` n `120` status `ready` deltaP `18.4655` edge `0.1412` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3686` n `50` status `ready` deltaP `26.9948` edge `0.0325` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.1503` n `64` status `ready` deltaP `16.5232` edge `0.007` maxDD `-0.0372`
- `market_context_high->unknown_1h` score `0.9911` n `120` status `ready` deltaP `9.3913` edge `0.065` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.9329` n `56` status `ready` deltaP `20.0566` edge `0.0622` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.7667` n `56` status `ready` deltaP `14.46` edge `0.0206` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.5241` n `64` status `ready` deltaP `13.8473` edge `0.0069` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1389` n `56` status `ready` deltaP `7.5566` edge `0.0011` maxDD `-0.1919`
- `market_context_high->metal_4h` score `-0.0137` n `120` status `ready` deltaP `13.1504` edge `0.0023` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3333` n `64` status `ready` deltaP `1.3941` edge `-0.0095` maxDD `-0.7353`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
