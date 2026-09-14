# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T02:52:32.416564+00:00`
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

- `news_risk_high->unknown_1h` score `444.454` n `82` status `ready` deltaP `-5.5499` edge `37.117` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.422` n `82` status `ready` deltaP `37.7544` edge `1.4156` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.364` n `82` status `ready` deltaP `38.0236` edge `1.4239` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.0727` n `82` status `ready` deltaP `32.9605` edge `0.881` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.8462` n `82` status `ready` deltaP `56.7325` edge `0.2933` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.3638` n `62` status `ready` deltaP `39.8276` edge `0.2648` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1742` n `39` status `ready` deltaP `39.8276` edge `0.249` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1742` n `39` status `ready` deltaP `39.8276` edge `0.249` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.6089` n `39` status `ready` deltaP `61.7462` edge `0.06` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.6089` n `39` status `ready` deltaP `61.7462` edge `0.06` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.2618` n `82` status `ready` deltaP `31.1396` edge `0.2763` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8485` n `62` status `ready` deltaP `54.6329` edge `0.0614` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9877` n `52` status `ready` deltaP `26.7472` edge `0.0223` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9877` n `52` status `ready` deltaP `26.7472` edge `0.0223` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.709` n `131` status `ready` deltaP `21.1541` edge `0.0432` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6963` n `137` status `ready` deltaP `12.0635` edge `0.0153` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.573` n `82` status `ready` deltaP `14.939` edge `0.0367` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3581` n `131` status `ready` deltaP `12.2859` edge `0.0116` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
