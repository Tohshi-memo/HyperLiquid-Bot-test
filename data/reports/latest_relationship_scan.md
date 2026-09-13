# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T10:07:30.659530+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12968`

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

- `market_context_high->unknown_24h` score `16666.224` n `59` status `ready` deltaP `13.6792` edge `1388.766` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `401.6679` n `82` status `ready` deltaP `-5.281` edge `33.5497` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `17.8162` n `82` status `ready` deltaP `37.8512` edge `1.3794` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.7842` n `82` status `ready` deltaP `32.582` edge `1.3136` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `10.0645` n `59` status `ready` deltaP `22.5366` edge `0.7712` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.7613` n `59` status `ready` deltaP `43.422` edge `0.5166` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.439` n `82` status `ready` deltaP `21.4088` edge `0.6552` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.5501` n `82` status `ready` deltaP `46.5601` edge `0.2531` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.584` n `82` status `ready` deltaP `24.2431` edge `0.2658` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.145` n `59` status `ready` deltaP `40.8621` edge `0.073` maxDD `0.0`
- `market_context_high->index_24h` score `3.7008` n `59` status `ready` deltaP `40.3799` edge `0.0813` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.9154` n `59` status `ready` deltaP `13.5155` edge `0.1147` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.4584` n `65` status `ready` deltaP `10.9091` edge `0.1535` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.4584` n `65` status `ready` deltaP `10.9091` edge `0.1535` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4133` n `82` status `ready` deltaP `12.4981` edge `0.0325` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1026` n `65` status `ready` deltaP `4.6246` edge `0.0033` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1026` n `65` status `ready` deltaP `4.6246` edge `0.0033` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0667` n `65` status `ready` deltaP `3.8335` edge `0.0019` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0667` n `65` status `ready` deltaP `3.8335` edge `0.0019` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1509` n `138` status `ready` deltaP `3.0415` edge `-0.0012` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
