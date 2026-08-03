# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T23:16:40.912172+00:00`
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

- `market_context_high->unknown_24h` score `39.4227` n `44` status `ready` deltaP `27.0676` edge `3.1091` maxDD `-0.0128`
- `market_context_high->unknown_4h` score `12.5308` n `66` status `ready` deltaP `11.7424` edge `1.0132` maxDD `-1.4466`
- `market_context_high->crypto_alt_24h` score `10.4638` n `44` status `ready` deltaP `48.2165` edge `0.5679` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `9.1419` n `44` status `ready` deltaP `43.6869` edge `0.483` maxDD `-0.3268`
- `news_risk_high->fx_24h` score `1.0361` n `31` status `ready` deltaP `12.192` edge `0.0703` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8968` n `31` status `ready` deltaP `19.2389` edge `0.0079` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.6165` n `66` status `ready` deltaP `9.4051` edge `0.0733` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.4438` n `78` status `ready` deltaP `10.9397` edge `-0.0011` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.4135` n `66` status `ready` deltaP `19.7709` edge `0.0072` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2888` n `78` status `ready` deltaP `6.6252` edge `0.0215` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0987` n `31` status `ready` deltaP `4.1306` edge `0.0354` maxDD `-0.356`
- `news_risk_high->equity_4h` score `-0.0277` n `31` status `ready` deltaP `-9.8692` edge `0.1319` maxDD `-2.8064`
- `news_risk_high->commodity_4h` score `-0.1178` n `31` status `ready` deltaP `9.8938` edge `-0.0257` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.142` n `31` status `ready` deltaP `1.2459` edge `-0.0067` maxDD `-0.5845`
- `news_risk_high->index_4h` score `-0.1944` n `31` status `ready` deltaP `-2.9603` edge `0.0416` maxDD `-0.3783`
- `news_risk_high->crypto_alt_1h` score `-0.2102` n `31` status `ready` deltaP `9.7933` edge `-0.0282` maxDD `-3.1233`
- `market_context_high->index_1h` score `-0.2868` n `78` status `ready` deltaP `4.0995` edge `-0.0107` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.3416` n `31` status `ready` deltaP `-2.2117` edge `0.0021` maxDD `-0.1588`
- `news_risk_high->unknown_4h` score `-0.5095` n `31` status `ready` deltaP `-1.2097` edge `-0.0086` maxDD `-1.5591`
- `market_context_high->metal_1h` score `-0.6183` n `78` status `ready` deltaP `-3.0785` edge `-0.0093` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
