# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T22:52:25.342874+00:00`
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

- `market_context_high->unknown_24h` score `41.6844` n `42` status `ready` deltaP `26.9593` edge `3.2983` maxDD `-0.0128`
- `market_context_high->unknown_4h` score `13.0403` n `64` status `ready` deltaP `10.9375` edge `1.061` maxDD `-1.4448`
- `market_context_high->crypto_alt_24h` score `10.5316` n `42` status `ready` deltaP `48.239` edge `0.5734` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `9.8151` n `42` status `ready` deltaP `48.0159` edge `0.5099` maxDD `-0.2995`
- `news_risk_high->fx_24h` score `1.0277` n `31` status `ready` deltaP `12.192` edge `0.0696` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9054` n `31` status `ready` deltaP `19.3886` edge `0.008` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.8156` n `64` status `ready` deltaP `11.2043` edge `0.0779` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.5482` n `76` status `ready` deltaP `12.2597` edge `-0.0012` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.5219` n `64` status `ready` deltaP `18.5976` edge `0.0055` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2039` n `76` status `ready` deltaP `5.5941` edge `0.0213` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.1082` n `31` status `ready` deltaP `4.2831` edge `0.0356` maxDD `-0.356`
- `news_risk_high->equity_4h` score `0.0687` n `31` status `ready` deltaP `-9.5643` edge `0.1379` maxDD `-2.8064`
- `news_risk_high->commodity_4h` score `-0.1082` n `31` status `ready` deltaP `9.8938` edge `-0.0249` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.1241` n `31` status `ready` deltaP `1.5453` edge `-0.0064` maxDD `-0.5845`
- `news_risk_high->index_4h` score `-0.1544` n `31` status `ready` deltaP `-2.6554` edge `0.0429` maxDD `-0.3783`
- `news_risk_high->crypto_alt_1h` score `-0.2056` n `31` status `ready` deltaP `9.7933` edge `-0.0276` maxDD `-3.1233`
- `market_context_high->index_1h` score `-0.3307` n `76` status `ready` deltaP `3.2855` edge `-0.0109` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.358` n `31` status `ready` deltaP `-2.5111` edge `0.002` maxDD `-0.1588`
- `news_risk_high->unknown_4h` score `-0.515` n `31` status `ready` deltaP `-1.2097` edge `-0.0093` maxDD `-1.5591`
- `market_context_high->metal_1h` score `-0.6146` n `76` status `ready` deltaP `-2.9625` edge `-0.0096` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
