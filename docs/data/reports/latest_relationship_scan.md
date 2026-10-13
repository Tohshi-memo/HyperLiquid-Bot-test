# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T05:07:30.412857+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9726`

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

- `market_context_high->crypto_alt_4h` score `6.091` n `108` status `ready` deltaP `17.0054` edge `0.5391` maxDD `-9.2574`
- `risk_on_high->crypto_alt_4h` score `5.8058` n `52` status `ready` deltaP `20.6379` edge `0.391` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.8058` n `52` status `ready` deltaP `20.6379` edge `0.391` maxDD `-1.9151`
- `market_context_high->crypto_major_4h` score `5.7561` n `108` status `ready` deltaP `20.7712` edge `0.4971` maxDD `-7.4722`
- `risk_on_high->commodity_24h` score `5.3266` n `48` status `ready` deltaP `30.087` edge `0.2433` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3266` n `48` status `ready` deltaP `30.087` edge `0.2433` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.882` n `52` status `ready` deltaP `35.7997` edge `0.4725` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.882` n `52` status `ready` deltaP `35.7997` edge `0.4725` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.2297` n `108` status `ready` deltaP `-3.7432` edge `0.2754` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.8947` n `117` status `ready` deltaP `13.5665` edge `0.1742` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5402` n `117` status `ready` deltaP `8.057` edge `0.1552` maxDD `-3.7781`
- `risk_on_high->crypto_major_1h` score `-0.1552` n `54` status `ready` deltaP `3.4986` edge `0.029` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1552` n `54` status `ready` deltaP `3.4986` edge `0.029` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2939` n `117` status `ready` deltaP `1.6979` edge `0.0022` maxDD `-0.3742`
- `market_context_high->metal_4h` score `-0.3387` n `108` status `ready` deltaP `9.1069` edge `0.0156` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.5017` n `54` status `ready` deltaP `3.3101` edge `0.0162` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5017` n `54` status `ready` deltaP `3.3101` edge `0.0162` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.5321` n `117` status `ready` deltaP `1.2243` edge `-0.0016` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5519` n `117` status `ready` deltaP `5.4686` edge `0.0045` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5731` n `54` status `ready` deltaP `0.0555` edge `-0.0007` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
