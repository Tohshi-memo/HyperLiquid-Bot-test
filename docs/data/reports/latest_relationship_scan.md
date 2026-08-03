# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T19:22:25.317000+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `market_context_high->unknown_24h` score `45.6936` n `39` status `ready` deltaP `29.3403` edge `3.6122` maxDD `0.0`
- `market_context_high->unknown_4h` score `18.8452` n `50` status `ready` deltaP `16.7378` edge `1.483` maxDD `-0.5988`
- `market_context_high->crypto_alt_24h` score `11.2615` n `39` status `ready` deltaP `49.773` edge `0.624` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.1629` n `39` status `ready` deltaP `53.6458` edge `0.5726` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9737` n `31` status `ready` deltaP `12.192` edge `0.0651` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8703` n `31` status `ready` deltaP `18.7898` edge `0.0075` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.7086` n `31` status `ready` deltaP `-7.4302` edge `0.177` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.5067` n `62` status `ready` deltaP `10.7253` edge `0.0309` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.4413` n `50` status `ready` deltaP `7.2012` edge `0.0932` maxDD `-2.7703`
- `news_risk_high->fx_4h` score `0.1051` n `31` status `ready` deltaP `4.2831` edge `0.0352` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.104` n `31` status `ready` deltaP `-0.5212` edge `0.0502` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `0.0255` n `31` status `ready` deltaP `11.2657` edge `-0.0229` maxDD `-1.6728`
- `market_context_high->fx_1h` score `-0.0504` n `62` status `ready` deltaP `5.4375` edge `-0.0056` maxDD `-0.7878`
- `news_risk_high->index_1h` score `-0.0563` n `31` status `ready` deltaP `2.7429` edge `-0.0057` maxDD `-0.5845`
- `market_context_high->fx_4h` score `-0.092` n `50` status `ready` deltaP `12.3476` edge `-0.0043` maxDD `-1.8545`
- `market_context_high->crypto_alt_1h` score `-0.1408` n `62` status `ready` deltaP `4.8049` edge `0.0168` maxDD `-3.0178`
- `news_risk_high->crypto_alt_1h` score `-0.1447` n `31` status `ready` deltaP `9.6436` edge `-0.0188` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.277` n `31` status `ready` deltaP `-1.0141` edge `0.0024` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.5201` n `50` status `ready` deltaP `1.6768` edge `0.0127` maxDD `-4.9116`
- `market_context_high->fx_24h` score `-0.5631` n `39` status `ready` deltaP `1.1084` edge `0.0421` maxDD `-2.3798`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
