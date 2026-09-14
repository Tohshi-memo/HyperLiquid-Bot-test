# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T13:07:31.165371+00:00`
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

- `news_risk_high->unknown_4h` score `376.1864` n `81` status `ready` deltaP `-21.0611` edge `31.5786` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `20.6771` n `81` status `ready` deltaP `42.9784` edge `1.4851` maxDD `-2.2157`
- `news_risk_high->crypto_major_24h` score `16.8767` n `81` status `ready` deltaP `33.4876` edge `1.3302` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.4744` n `81` status `ready` deltaP `36.5162` edge `0.9741` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.4095` n `81` status `ready` deltaP `60.3588` edge `0.316` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1671` n `98` status `ready` deltaP `40.1042` edge `0.3299` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1615` n `41` status `ready` deltaP `40.1042` edge `0.2461` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1615` n `41` status `ready` deltaP `40.1042` edge `0.2461` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.1155` n `81` status `ready` deltaP `36.7863` edge `0.3098` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.9112` n `41` status `ready` deltaP `55.1999` edge `0.0455` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.9112` n `41` status `ready` deltaP `55.1999` edge `0.0455` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.4864` n `98` status `ready` deltaP `51.5165` edge `0.052` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9983` n `52` status `ready` deltaP `26.5947` edge `0.0242` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9983` n `52` status `ready` deltaP `26.5947` edge `0.0242` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7986` n `137` status `ready` deltaP `22.0046` edge `0.045` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7071` n `137` status `ready` deltaP `12.2132` edge `0.0152` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6988` n `81` status `ready` deltaP `16.7589` edge `0.0407` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2985` n `137` status `ready` deltaP `11.5308` edge `0.009` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1917` n `52` status `ready` deltaP `6.5984` edge `0.0072` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1917` n `52` status `ready` deltaP `6.5984` edge `0.0072` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
