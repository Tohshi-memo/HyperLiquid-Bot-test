# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T13:52:30.665122+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `45.0906` n `53` status `ready` deltaP `11.6319` edge `3.68` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.2112` n `53` status `ready` deltaP `24.9798` edge `0.861` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `10.8733` n `53` status `ready` deltaP `32.1639` edge `0.7358` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.8374` n `53` status `ready` deltaP `29.2453` edge `0.4679` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.009` n `53` status `ready` deltaP `39.9404` edge `0.083` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.968` n `53` status `ready` deltaP `35.7254` edge `0.0226` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.8443` n `136` status `ready` deltaP `23.2873` edge `0.1226` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7974` n `53` status `ready` deltaP `15.7129` edge `0.1639` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `1.8164` n `53` status `ready` deltaP `29.1896` edge `-0.039` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7079` n `53` status `ready` deltaP `19.7365` edge `0.0878` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.1099` n `137` status `ready` deltaP `11.9531` edge `0.0577` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.1033` n `53` status `ready` deltaP `15.47` edge `0.0058` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.414` n `53` status `ready` deltaP `10.5271` edge `-0.0044` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.41` n `53` status `ready` deltaP `12.7754` edge `0.0038` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1755` n `53` status `ready` deltaP `7.1186` edge `0.0069` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0729` n `53` status `ready` deltaP `3.8499` edge `0.0003` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.1028` n `53` status `ready` deltaP `7.1013` edge `-0.0028` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.2437` n `53` status `ready` deltaP `1.3332` edge `-0.0066` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4434` n `137` status `ready` deltaP `2.593` edge `-0.0009` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.932` n `136` status `ready` deltaP `4.618` edge `-0.029` maxDD `-2.6898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
