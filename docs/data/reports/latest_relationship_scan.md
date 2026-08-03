# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T23:22:32.501045+00:00`
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

- `market_context_high->unknown_24h` score `39.4119` n `44` status `ready` deltaP `27.0676` edge `3.1082` maxDD `-0.0128`
- `market_context_high->unknown_4h` score `12.526` n `66` status `ready` deltaP `11.7424` edge `1.0128` maxDD `-1.4466`
- `market_context_high->crypto_alt_24h` score `10.4566` n `44` status `ready` deltaP `48.2165` edge `0.5673` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `9.1306` n `44` status `ready` deltaP `43.6869` edge `0.4824` maxDD `-0.3544`
- `news_risk_high->fx_24h` score `1.0361` n `31` status `ready` deltaP `12.192` edge `0.0703` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9046` n `31` status `ready` deltaP `19.3886` edge `0.0079` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.6129` n `66` status `ready` deltaP `9.4051` edge `0.073` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.445` n `78` status `ready` deltaP `10.9397` edge `-0.001` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.4143` n `66` status `ready` deltaP `19.7709` edge `0.0073` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.1934` n `78` status `ready` deltaP `5.4929` edge `0.0211` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0987` n `31` status `ready` deltaP `4.1306` edge `0.0354` maxDD `-0.356`
- `news_risk_high->equity_4h` score `-0.0277` n `31` status `ready` deltaP `-9.8692` edge `0.1319` maxDD `-2.8064`
- `news_risk_high->commodity_4h` score `-0.1166` n `31` status `ready` deltaP `9.8938` edge `-0.0256` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.142` n `31` status `ready` deltaP `1.2459` edge `-0.0067` maxDD `-0.5845`
- `news_risk_high->index_4h` score `-0.1944` n `31` status `ready` deltaP `-2.9603` edge `0.0416` maxDD `-0.3783`
- `news_risk_high->crypto_alt_1h` score `-0.2095` n `31` status `ready` deltaP `9.7933` edge `-0.0281` maxDD `-3.1233`
- `market_context_high->index_1h` score `-0.286` n `78` status `ready` deltaP `4.0995` edge `-0.0106` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.3416` n `31` status `ready` deltaP `-2.2117` edge `0.0021` maxDD `-0.1588`
- `news_risk_high->unknown_4h` score `-0.5095` n `31` status `ready` deltaP `-1.2097` edge `-0.0086` maxDD `-1.5591`
- `market_context_high->metal_1h` score `-0.5579` n `78` status `ready` deltaP `-1.9461` edge `-0.0091` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
