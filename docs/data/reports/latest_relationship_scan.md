# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T17:37:26.985852+00:00`
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

- `news_risk_high->unknown_24h` score `54.1255` n `50` status `ready` deltaP `12.9983` edge `4.4238` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.409` n `50` status `ready` deltaP `43.6603` edge `2.4538` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.0952` n `56` status `ready` deltaP `23.432` edge `0.7826` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.7163` n `50` status `ready` deltaP `30.1005` edge `0.3685` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `5.2958` n `50` status `ready` deltaP `22.8215` edge `0.3385` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.3254` n `50` status `ready` deltaP `43.4073` edge `0.0753` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0784` n `56` status `ready` deltaP `47.4303` edge `0.0327` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.5388` n `65` status `ready` deltaP `13.1092` edge `0.2432` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `3.4342` n `120` status `ready` deltaP `6.3316` edge `0.3172` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.1426` n `120` status `ready` deltaP `28.7406` edge `0.1722` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.6614` n `120` status `ready` deltaP `18.313` edge `0.1404` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.371` n `50` status `ready` deltaP `26.9948` edge `0.0327` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.0268` n `65` status `ready` deltaP `15.6633` edge `0.0068` maxDD `-0.0525`
- `market_context_high->unknown_1h` score `0.9863` n `120` status `ready` deltaP `9.3913` edge `0.0646` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.9485` n `56` status `ready` deltaP `20.0566` edge `0.0642` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.7798` n `56` status `ready` deltaP `14.46` edge `0.0217` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.5572` n `65` status `ready` deltaP `14.4242` edge `0.0073` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1413` n `56` status `ready` deltaP `7.5566` edge `0.0013` maxDD `-0.1919`
- `market_context_high->metal_4h` score `-0.0051` n `120` status `ready` deltaP `13.1504` edge `0.0034` maxDD `-3.3377`
- `news_risk_high->metal_1h` score `-0.3101` n `65` status `ready` deltaP `4.2953` edge `-0.0188` maxDD `-1.9673`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
