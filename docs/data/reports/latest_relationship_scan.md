# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T20:22:35.119440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5931`

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

- `market_context_high->unknown_24h` score `44.284` n `40` status `ready` deltaP `28.8194` edge `3.4982` maxDD `0.0`
- `market_context_high->unknown_4h` score `16.2788` n `54` status `ready` deltaP `12.8161` edge `1.3156` maxDD `-1.2244`
- `market_context_high->crypto_alt_24h` score `11.0869` n `40` status `ready` deltaP `49.2708` edge `0.6128` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `10.59` n `40` status `ready` deltaP `50.9722` edge `0.5487` maxDD `-0.1479`
- `news_risk_high->fx_24h` score `0.9881` n `31` status `ready` deltaP `12.192` edge `0.0663` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.8898` n `54` status `ready` deltaP `10.1513` edge `0.0911` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.8781` n `31` status `ready` deltaP `18.9395` edge `0.0075` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.5602` n `31` status `ready` deltaP `-8.0399` edge `0.1687` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.4494` n `66` status `ready` deltaP `7.2582` edge `0.0265` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1375` n `66` status `ready` deltaP `7.5758` edge `-0.0042` maxDD `-0.7878`
- `news_risk_high->fx_4h` score `0.1051` n `31` status `ready` deltaP `4.2831` edge `0.0352` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.0396` n `31` status `ready` deltaP `-1.131` edge `0.0489` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `-0.017` n `31` status `ready` deltaP `10.8084` edge `-0.0234` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.0727` n `31` status `ready` deltaP `2.4435` edge `-0.0058` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1026` n `31` status `ready` deltaP `10.2424` edge `-0.0174` maxDD `-3.1233`
- `market_context_high->fx_4h` score `-0.2295` n `54` status `ready` deltaP `10.4957` edge `-0.0031` maxDD `-1.8797`
- `market_context_high->crypto_alt_4h` score `-0.2781` n `54` status `ready` deltaP `4.7708` edge `0.0231` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.3089` n `31` status `ready` deltaP `-1.6129` edge `0.0023` maxDD `-0.1588`
- `market_context_high->crypto_alt_1h` score `-0.3157` n `66` status `ready` deltaP `1.9824` edge `0.0132` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.4233` n `66` status `ready` deltaP `2.1503` edge `-0.0152` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
