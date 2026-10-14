# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T15:07:27.018245+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9234`

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

- `market_context_high->crypto_alt_4h` score `6.6679` n `117` status `ready` deltaP `17.5266` edge `0.5837` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.1924` n `54` status `ready` deltaP `32.0` edge `0.3027` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1924` n `54` status `ready` deltaP `32.0` edge `0.3027` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.9372` n `117` status `ready` deltaP `20.8151` edge `0.5119` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.2568` n `54` status `ready` deltaP `19.8058` edge `0.3508` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.2568` n `54` status `ready` deltaP `19.8058` edge `0.3508` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.399` n `54` status `ready` deltaP `33.9205` edge `0.4231` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.399` n `54` status `ready` deltaP `33.9205` edge `0.4231` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7831` n `117` status `ready` deltaP `13.7162` edge `0.1639` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2838` n `117` status `ready` deltaP `6.1109` edge `0.1468` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1976` n `117` status `ready` deltaP `13.1554` edge `0.0333` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.322` n `54` status `ready` deltaP `1.5525` edge `0.0206` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.322` n `54` status `ready` deltaP `1.5525` edge `0.0206` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.3733` n `117` status `ready` deltaP `7.265` edge `0.0074` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3912` n `117` status `ready` deltaP `0.4967` edge `0.0021` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.457` n `54` status `ready` deltaP `1.8519` edge `0.0022` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.457` n `54` status `ready` deltaP `1.8519` edge `0.0022` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.5742` n `54` status `ready` deltaP `3.4598` edge `0.0059` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5742` n `54` status `ready` deltaP `3.4598` edge `0.0059` maxDD `-5.8734`
- `risk_on_high->metal_4h` score `-0.6525` n `54` status `ready` deltaP `0.7622` edge `0.0158` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
