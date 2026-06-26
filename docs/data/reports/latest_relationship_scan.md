# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T08:22:33.237478+00:00`
- Price records: `672`
- Market context records: `4809`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7578`

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

- `market_context_high->unknown_1h` score `11.4567` n `118` status `ready` deltaP `11.5625` edge `0.9194` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8582` n `117` status `ready` deltaP `18.1038` edge `0.6552` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.2137` n `111` status `ready` deltaP `12.6314` edge `0.1926` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.2405` n `117` status `ready` deltaP `9.4917` edge `0.1129` maxDD `-6.9604`
- `market_context_high->commodity_1h` score `0.1257` n `118` status `ready` deltaP `5.8865` edge `0.03` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.1198` n `117` status `ready` deltaP `12.4753` edge `0.0494` maxDD `-4.377`
- `market_context_high->fx_4h` score `-0.3069` n `117` status `ready` deltaP `5.1582` edge `0.0039` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.3266` n `117` status `ready` deltaP `7.4448` edge `0.0138` maxDD `-5.4242`
- `market_context_high->equity_1h` score `-0.6882` n `118` status `ready` deltaP `2.144` edge `0.0051` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9707` n `118` status `ready` deltaP `-1.941` edge `-0.003` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3992` n `118` status `ready` deltaP `-1.3473` edge `-0.0072` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.122` n `111` status `ready` deltaP `19.909` edge `0.1061` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3195` n `118` status `ready` deltaP `-1.4412` edge `-0.0702` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.7576` n `111` status `ready` deltaP `-12.0308` edge `-0.0186` maxDD `-3.1464`
- `market_context_high->crypto_major_1h` score `-3.055` n `118` status `ready` deltaP `-0.0964` edge `-0.082` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-3.1913` n `118` status `ready` deltaP `0.8982` edge `-0.0515` maxDD `-14.9676`
- `market_context_high->index_24h` score `-4.3767` n `111` status `ready` deltaP `-7.0899` edge `-0.123` maxDD `-23.2678`
- `market_context_high->crypto_alt_4h` score `-4.5329` n `117` status `ready` deltaP `6.5302` edge `-0.0168` maxDD `-43.2966`
- `market_context_high->crypto_major_4h` score `-8.3309` n `117` status `ready` deltaP `3.6286` edge `-0.1767` maxDD `-67.9107`
- `market_context_high->metal_4h` score `-8.6206` n `117` status `ready` deltaP `4.7503` edge `-0.3128` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
