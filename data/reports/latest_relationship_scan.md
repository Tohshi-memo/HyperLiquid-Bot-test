# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T03:07:33.483953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11376`

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

- `news_risk_high->unknown_1h` score `444.442` n `82` status `ready` deltaP `-5.5499` edge `37.116` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.479` n `82` status `ready` deltaP `37.9268` edge `1.4192` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3616` n `82` status `ready` deltaP `38.0236` edge `1.4237` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.1285` n `82` status `ready` deltaP `33.1329` edge `0.8845` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.8696` n `82` status `ready` deltaP `56.9049` edge `0.2941` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.4142` n `63` status `ready` deltaP `39.8276` edge `0.269` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2654` n `40` status `ready` deltaP `39.8276` edge `0.2566` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2654` n `40` status `ready` deltaP `39.8276` edge `0.2566` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.6074` n `40` status `ready` deltaP `61.6379` edge `0.0606` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.6074` n `40` status `ready` deltaP `61.6379` edge `0.0606` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.2852` n `82` status `ready` deltaP `31.3121` edge `0.2771` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.847` n `63` status `ready` deltaP `54.6141` edge `0.0614` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9901` n `52` status `ready` deltaP `26.7472` edge `0.0225` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9901` n `52` status `ready` deltaP `26.7472` edge `0.0225` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7253` n `132` status `ready` deltaP `21.3276` edge `0.0434` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6831` n `137` status `ready` deltaP `11.9138` edge `0.0152` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.573` n `82` status `ready` deltaP `14.939` edge `0.0367` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3669` n `132` status `ready` deltaP `12.44` edge `0.0117` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1783` n `137` status `ready` deltaP `5.6613` edge `0.0029` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1677` n `52` status `ready` deltaP `6.299` edge `0.0072` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
