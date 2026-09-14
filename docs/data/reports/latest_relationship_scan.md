# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T03:52:28.622217+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11400`

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

- `news_risk_high->unknown_1h` score `444.2704` n `82` status `ready` deltaP `-5.5499` edge `37.1017` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.5714` n `82` status `ready` deltaP `38.2716` edge `1.4246` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.292` n `82` status `ready` deltaP `38.0236` edge `1.4179` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.2971` n `82` status `ready` deltaP `33.6501` edge `0.8951` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.9398` n `82` status `ready` deltaP `57.4222` edge `0.2965` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.5642` n `66` status `ready` deltaP `39.8276` edge `0.2815` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.3338` n `41` status `ready` deltaP `39.8276` edge `0.2623` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3338` n `41` status `ready` deltaP `39.8276` edge `0.2623` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.5565` n `41` status `ready` deltaP `61.1817` edge `0.0594` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.5565` n `41` status `ready` deltaP `61.1817` edge `0.0594` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.3469` n `82` status `ready` deltaP `31.8293` edge `0.2788` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8307` n `66` status `ready` deltaP `54.5298` edge `0.0606` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9925` n `52` status `ready` deltaP `26.7472` edge `0.0227` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9925` n `52` status `ready` deltaP `26.7472` edge `0.0227` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7705` n `135` status `ready` deltaP `21.8327` edge `0.0438` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6676` n `137` status `ready` deltaP `11.7641` edge `0.0149` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5912` n `82` status `ready` deltaP `15.2439` edge `0.037` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3895` n `135` status `ready` deltaP `12.8748` edge `0.0117` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.2034` n `137` status `ready` deltaP `5.9607` edge `0.003` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1521` n `52` status `ready` deltaP `6.1493` edge `0.0069` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
