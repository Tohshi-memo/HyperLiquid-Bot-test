# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T08:37:30.479090+00:00`
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

- `news_risk_high->unknown_1h` score `443.3945` n `82` status `ready` deltaP `-5.999` edge `37.0317` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.1655` n `82` status `ready` deltaP `41.3033` edge `1.4539` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.5383` n `82` status `ready` deltaP `35.368` edge `1.3728` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.0867` n `82` status `ready` deltaP `35.6607` edge `0.9475` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2519` n `82` status `ready` deltaP `59.4485` edge `0.309` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.9501` n `84` status `ready` deltaP `39.8964` edge `0.3132` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1785` n `41` status `ready` deltaP `39.8964` edge `0.2489` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1785` n `41` status `ready` deltaP `39.8964` edge `0.2489` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.7892` n `82` status `ready` deltaP `35.0331` edge `0.2943` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.19` n `41` status `ready` deltaP `58.0101` edge `0.05` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.19` n `41` status `ready` deltaP `58.0101` edge `0.05` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.6572` n `84` status `ready` deltaP `53.3062` edge `0.0543` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9343` n `52` status `ready` deltaP `26.2899` edge `0.0209` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9343` n `52` status `ready` deltaP `26.2899` edge `0.0209` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7346` n `137` status `ready` deltaP `21.6998` edge `0.0417` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6915` n `137` status `ready` deltaP `12.2132` edge `0.0139` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6599` n `82` status `ready` deltaP `16.311` edge `0.0387` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3152` n `137` status `ready` deltaP `11.8357` edge `0.0091` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1866` n `137` status `ready` deltaP `5.811` edge `0.0026` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1761` n `52` status `ready` deltaP `6.5984` edge `0.0059` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
