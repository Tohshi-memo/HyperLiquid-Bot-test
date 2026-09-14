# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T02:07:30.982556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11352`

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

- `news_risk_high->unknown_1h` score `442.2892` n `82` status `ready` deltaP `-5.5499` edge `36.9366` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.2726` n `82` status `ready` deltaP `37.2371` edge `1.4066` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3604` n `82` status `ready` deltaP `38.0236` edge `1.4236` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.9041` n `82` status `ready` deltaP `32.4432` edge `0.8704` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.7785` n `82` status `ready` deltaP `56.2153` edge `0.2911` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.2342` n `59` status `ready` deltaP `39.8276` edge `0.254` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.9258` n `36` status `ready` deltaP `39.8276` edge `0.2283` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9258` n `36` status `ready` deltaP `39.8276` edge `0.2283` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.6068` n `36` status `ready` deltaP `62.0498` edge `0.0578` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.6068` n `36` status `ready` deltaP `62.0498` edge `0.0578` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.1952` n `82` status `ready` deltaP `30.6224` edge `0.2742` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.841` n `59` status `ready` deltaP `54.6581` edge `0.0606` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9561` n `52` status `ready` deltaP `26.4423` edge `0.0217` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9561` n `52` status `ready` deltaP `26.4423` edge `0.0217` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7787` n `128` status `ready` deltaP `21.875` edge `0.0442` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6676` n `137` status `ready` deltaP `11.7641` edge `0.0149` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5563` n `82` status `ready` deltaP `14.6341` edge `0.0366` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3064` n `128` status `ready` deltaP `11.3377` edge `0.0113` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1747` n `137` status `ready` deltaP `5.6613` edge `0.0026` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1521` n `52` status `ready` deltaP `6.1493` edge `0.0069` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
