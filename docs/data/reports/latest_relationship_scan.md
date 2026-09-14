# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T04:52:29.545249+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11598`

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

- `news_risk_high->unknown_1h` score `443.7376` n `82` status `ready` deltaP `-5.8493` edge `37.0593` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.707` n `82` status `ready` deltaP `38.9613` edge `1.4313` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.1396` n `82` status `ready` deltaP `37.3339` edge `1.4098` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.5275` n `82` status `ready` deltaP `34.3398` edge `0.9097` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.0406` n `82` status `ready` deltaP `58.1118` edge `0.3003` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.6998` n `70` status `ready` deltaP `39.8276` edge `0.2928` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2906` n `41` status `ready` deltaP `39.8276` edge `0.2587` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2906` n `41` status `ready` deltaP `39.8276` edge `0.2587` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.4714` n `41` status `ready` deltaP `60.492` edge `0.0569` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.4714` n `41` status `ready` deltaP `60.492` edge `0.0569` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.4417` n `82` status `ready` deltaP `32.519` edge `0.2821` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.7847` n `70` status `ready` deltaP `54.3596` edge `0.0579` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0059` n `52` status `ready` deltaP `26.8996` edge `0.0228` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0059` n `52` status `ready` deltaP `26.8996` edge `0.0228` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8062` n `137` status `ready` deltaP `22.3095` edge `0.0436` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7107` n `137` status `ready` deltaP `12.2132` edge `0.0155` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5927` n `82` status `ready` deltaP `15.2439` edge `0.0372` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3387` n `137` status `ready` deltaP `11.9881` edge `0.0111` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.231` n `137` status `ready` deltaP `6.2601` edge `0.0033` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1953` n `52` status `ready` deltaP `6.5984` edge `0.0075` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
