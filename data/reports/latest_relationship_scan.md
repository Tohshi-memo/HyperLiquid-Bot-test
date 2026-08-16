# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T06:37:26.628343+00:00`
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

- `market_context_high->unknown_24h` score `184.4681` n `88` status `ready` deltaP `-22.619` edge `24.0689` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.3786` n `36` status `ready` deltaP `22.1548` edge `0.9218` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5708` n `36` status `ready` deltaP `38.4146` edge `0.3748` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.395` n `88` status `ready` deltaP `41.0549` edge `0.3483` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.663` n `36` status `ready` deltaP `30.5026` edge `0.1019` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.135` n `102` status `ready` deltaP `19.1744` edge `0.0972` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7877` n `36` status `ready` deltaP `20.5284` edge `0.0253` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6999` n `36` status `ready` deltaP `7.8344` edge `0.1213` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.1257` n `108` status `ready` deltaP `3.9643` edge `0.0243` maxDD `-0.5536`
- `market_context_high->fx_4h` score `0.0151` n `102` status `ready` deltaP `7.8461` edge `0.0101` maxDD `-0.504`
- `news_risk_high->fx_4h` score `-0.0029` n `36` status `ready` deltaP `4.2513` edge `-0.0068` maxDD `-0.0863`
- `market_context_high->fx_1h` score `-0.0163` n `108` status `ready` deltaP `3.6095` edge `0.002` maxDD `-0.2527`
- `news_risk_high->index_1h` score `-0.1282` n `36` status `ready` deltaP `-0.2827` edge `0.0138` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2113` n `36` status `ready` deltaP `0.8317` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5883` n `108` status `ready` deltaP `0.5323` edge `-0.0074` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.7002` n `36` status `ready` deltaP `-7.8011` edge `-0.0109` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.8294` n `108` status `ready` deltaP `-7.6902` edge `-0.0029` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0007` n `36` status `ready` deltaP `-1.6768` edge `-0.0278` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1225` n `36` status `ready` deltaP `-6.2209` edge `-0.0213` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.3062` n `102` status `ready` deltaP `1.2644` edge `-0.0185` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
