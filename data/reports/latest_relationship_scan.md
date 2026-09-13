# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T23:28:24.992219+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `2445.7524` n `56` status `ready` deltaP `10.2093` edge `203.7648` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `435.7564` n `82` status `ready` deltaP `-5.4002` edge `36.3912` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.9534` n `82` status `ready` deltaP `36.8923` edge `1.3823` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.334` n `82` status `ready` deltaP `38.0236` edge `1.4214` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.2628` n `82` status `ready` deltaP `30.5467` edge `0.8296` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.5223` n `82` status `ready` deltaP `54.3187` edge `0.2824` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.3018` n `56` status `ready` deltaP `39.8276` edge `0.1763` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.9847` n `82` status `ready` deltaP `28.7259` edge `0.2693` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.9682` n `30` status `ready` deltaP `39.8276` edge `0.1485` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9682` n `30` status `ready` deltaP `39.8276` edge `0.1485` maxDD `0.0`
- `risk_on_high->fx_24h` score `3.4084` n `30` status `ready` deltaP `60.0574` edge `0.0471` maxDD `-0.1745`
- `risk_on_and_context->fx_24h` score `3.4084` n `30` status `ready` deltaP `60.0574` edge `0.0471` maxDD `-0.1745`
- `risk_on_high->crypto_alt_24h` score `1.9977` n `30` status `ready` deltaP `0.6322` edge `0.382` maxDD `-6.7415`
- `risk_on_and_context->crypto_alt_24h` score `1.9977` n `30` status `ready` deltaP `0.6322` edge `0.382` maxDD `-6.7415`
- `market_context_high->fx_24h` score `1.7984` n `56` status `ready` deltaP `41.7241` edge `0.0271` maxDD `-1.6423`
- `risk_on_high->commodity_4h` score `1.7966` n `52` status `ready` deltaP `24.8241` edge `0.0192` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7966` n `52` status `ready` deltaP `24.8241` edge `0.0192` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.4896` n `128` status `ready` deltaP `20.6174` edge `0.0285` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.4655` n `82` status `ready` deltaP `13.2622` edge `0.0341` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.3671` n `137` status `ready` deltaP `8.5635` edge `0.0112` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
