# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T12:37:31.112437+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_4h` score `1107.1653` n `82` status `ready` deltaP `-20.5793` edge `92.4903` maxDD `-4.1464`
- `news_risk_high->unknown_1h` score `682.4886` n `82` status `ready` deltaP `-6.7475` edge `56.9612` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.4516` n `82` status `ready` deltaP `41.9546` edge `1.4734` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `16.6606` n `82` status `ready` deltaP `32.9015` edge `1.3161` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.2785` n `82` status `ready` deltaP `35.658` edge `0.9635` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2776` n `82` status `ready` deltaP `59.3199` edge `0.312` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `7.1671` n `97` status `ready` deltaP `40.1042` edge `0.3299` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1735` n `41` status `ready` deltaP `40.1042` edge `0.2471` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1735` n `41` status `ready` deltaP `40.1042` edge `0.2471` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.0818` n `82` status `ready` deltaP `36.7251` edge `0.3074` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.9474` n `41` status `ready` deltaP `55.5471` edge `0.0462` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.9474` n `41` status `ready` deltaP `55.5471` edge `0.0462` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.5115` n `97` status `ready` deltaP `51.8005` edge `0.0522` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0117` n `52` status `ready` deltaP `26.7472` edge `0.0243` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0117` n `52` status `ready` deltaP `26.7472` edge `0.0243` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.812` n `137` status `ready` deltaP `22.1571` edge `0.0451` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7203` n `137` status `ready` deltaP `12.3629` edge `0.0153` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7041` n `82` status `ready` deltaP `16.9207` edge `0.0403` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3167` n `137` status `ready` deltaP `11.8357` edge `0.0093` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2048` n `52` status `ready` deltaP `6.7481` edge `0.0073` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
