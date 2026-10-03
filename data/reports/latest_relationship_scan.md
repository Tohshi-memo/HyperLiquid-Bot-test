# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T14:37:28.475583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4742`

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

- `market_context_high->unknown_1h` score `367.7097` n `50` status `ready` deltaP `11.3234` edge `30.5719` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `296.1276` n `50` status `ready` deltaP `12.1951` edge `24.596` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.2827` n `50` status `ready` deltaP `29.9792` edge `1.1607` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.7763` n `50` status `ready` deltaP `37.6326` edge `0.8721` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `11.1201` n `62` status `ready` deltaP `39.0146` edge `0.6869` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.5662` n `62` status `ready` deltaP `29.2643` edge `0.7339` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.7563` n `62` status `ready` deltaP `27.3555` edge `0.5984` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4615` n `50` status `ready` deltaP `18.3049` edge `0.5701` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.4241` n `50` status `ready` deltaP `18.3232` edge `0.5421` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.633` n `62` status `ready` deltaP `33.9828` edge `0.1754` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0544` n `62` status `ready` deltaP `27.3801` edge `0.2166` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3261` n `50` status `ready` deltaP `14.9521` edge `0.2438` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.1739` n `62` status `ready` deltaP `34.289` edge `0.0621` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0602` n `50` status `ready` deltaP `34.3659` edge `0.0394` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `3.0314` n `68` status `ready` deltaP `13.9574` edge `0.1951` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9665` n `50` status `ready` deltaP `13.2515` edge `0.2039` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3915` n `62` status `ready` deltaP `19.3302` edge `0.112` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0474` n `68` status `ready` deltaP `25.2466` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6708` n `68` status `ready` deltaP `6.305` edge `0.1491` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.6076` n `50` status `ready` deltaP `22.2874` edge `0.0118` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
