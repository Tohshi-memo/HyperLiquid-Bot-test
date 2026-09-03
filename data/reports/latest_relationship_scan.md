# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T08:07:25.852621+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11563`

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

- `risk_on_high->unknown_4h` score `37.2637` n `122` status `ready` deltaP `15.8462` edge `3.0615` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `37.2637` n `122` status `ready` deltaP `15.8462` edge `3.0615` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.6255` n `162` status `ready` deltaP `12.6788` edge `2.2038` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.8422` n `133` status `ready` deltaP `2.6889` edge `1.6933` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.8422` n `133` status `ready` deltaP `2.6889` edge `1.6933` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.622` n `174` status `ready` deltaP `1.0685` edge `1.1911` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.6182` n `107` status `ready` deltaP `21.445` edge `0.6564` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.6182` n `107` status `ready` deltaP `21.445` edge `0.6564` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3467` n `107` status `ready` deltaP `21.6041` edge `0.8472` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3467` n `107` status `ready` deltaP `21.6041` edge `0.8472` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3178` n `59` status `ready` deltaP `21.5249` edge `0.4471` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.6769` n `59` status `ready` deltaP `14.6952` edge `0.4801` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.6183` n `59` status `ready` deltaP `7.3946` edge `0.3323` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.551` n `145` status `ready` deltaP `18.1836` edge `0.545` maxDD `-23.3898`
- `risk_on_high->crypto_major_24h` score `0.9376` n `107` status `ready` deltaP `21.0313` edge `0.8544` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.9376` n `107` status `ready` deltaP `21.0313` edge `0.8544` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.6222` n `145` status `ready` deltaP `23.5321` edge `0.8693` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.4918` n `145` status `ready` deltaP `15.0491` edge `0.7126` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2384` n `67` status `ready` deltaP `5.3376` edge `0.0309` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0696` n `133` status `ready` deltaP `11.5146` edge `0.0034` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
