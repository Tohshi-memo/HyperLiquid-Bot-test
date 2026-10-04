# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T15:22:26.804992+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5032`

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

- `market_context_high->unknown_1h` score `96.116` n `97` status `ready` deltaP `-0.6096` edge `8.0552` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `95.1972` n `91` status `ready` deltaP `3.3084` edge `7.9422` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.5759` n `65` status `ready` deltaP `37.5821` edge `0.6511` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `10.2358` n `46` status `ready` deltaP `26.4417` edge `0.804` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `10.0568` n `46` status `ready` deltaP `32.8804` edge `0.6841` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.2979` n `65` status `ready` deltaP `23.8809` edge `0.5423` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.3463` n `65` status `ready` deltaP `24.3598` edge `0.5842` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.1569` n `91` status `ready` deltaP `22.1975` edge `0.3521` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.9324` n `65` status `ready` deltaP `26.9097` edge `0.1483` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8212` n `65` status `ready` deltaP `25.9123` edge `0.2067` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1428` n `65` status `ready` deltaP `34.2003` edge `0.0601` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8717` n `65` status `ready` deltaP `12.4113` edge `0.1921` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.589` n `65` status `ready` deltaP `22.2796` edge `0.1088` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1333` n `65` status `ready` deltaP `26.216` edge `0.018` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1332` n `97` status `ready` deltaP `15.3297` edge `0.1206` maxDD `-2.2692`
- `market_context_high->equity_24h` score `1.7566` n `46` status `ready` deltaP `3.9477` edge `0.2192` maxDD `-6.264`
- `market_context_high->crypto_alt_4h` score `1.6141` n `91` status `ready` deltaP `5.8983` edge `0.2741` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.4774` n `91` status `ready` deltaP `25.8426` edge `0.0265` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.4671` n `65` status `ready` deltaP `4.719` edge `0.1427` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3615` n `46` status `ready` deltaP `25.536` edge `0.1061` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
