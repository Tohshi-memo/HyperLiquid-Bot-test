# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T22:37:24.619166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `market_context_high->unknown_24h` score `41.6808` n `42` status `ready` deltaP `26.9593` edge `3.298` maxDD `-0.0128`
- `market_context_high->unknown_4h` score `13.3234` n `63` status `ready` deltaP `10.5159` edge `1.0874` maxDD `-1.4448`
- `market_context_high->crypto_alt_24h` score `10.5815` n `42` status `ready` deltaP `48.4127` edge `0.5764` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `9.8151` n `42` status `ready` deltaP `48.0159` edge `0.5099` maxDD `-0.2995`
- `news_risk_high->fx_24h` score `1.0253` n `31` status `ready` deltaP `12.192` edge `0.0694` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.9306` n `63` status `ready` deltaP `12.1468` edge `0.0812` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.896` n `31` status `ready` deltaP `19.2389` edge `0.0078` maxDD `-0.6947`
- `market_context_high->fx_1h` score `0.5065` n `75` status `ready` deltaP `11.7685` edge `-0.0014` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.4531` n `63` status `ready` deltaP `17.9032` edge `0.0044` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2639` n `75` status `ready` deltaP `6.1637` edge `0.0225` maxDD `-1.3282`
- `news_risk_high->equity_4h` score `0.1229` n `31` status `ready` deltaP `-9.4119` edge `0.1414` maxDD `-2.8064`
- `news_risk_high->fx_4h` score `0.1082` n `31` status `ready` deltaP `4.2831` edge `0.0356` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `-0.1082` n `31` status `ready` deltaP `9.8938` edge `-0.0249` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.1163` n `31` status `ready` deltaP `1.695` edge `-0.0064` maxDD `-0.5845`
- `news_risk_high->index_4h` score `-0.1338` n `31` status `ready` deltaP `-2.503` edge `0.0436` maxDD `-0.3783`
- `news_risk_high->crypto_alt_1h` score `-0.1931` n `31` status `ready` deltaP `9.7933` edge `-0.026` maxDD `-3.1233`
- `market_context_high->index_1h` score `-0.3577` n `75` status `ready` deltaP `2.8563` edge `-0.0115` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.358` n `31` status `ready` deltaP `-2.5111` edge `0.002` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.3862` n `63` status `ready` deltaP `5.708` edge `0.003` maxDD `-4.9116`
- `market_context_high->crypto_alt_1h` score `-0.501` n `75` status `ready` deltaP `0.503` edge `-0.0007` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
