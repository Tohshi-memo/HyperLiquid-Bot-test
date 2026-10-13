# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T04:52:28.645173+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9738`

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

- `risk_on_high->crypto_alt_4h` score `5.8598` n `52` status `ready` deltaP `20.6379` edge `0.3955` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.8598` n `52` status `ready` deltaP `20.6379` edge `0.3955` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `5.7718` n `107` status `ready` deltaP `16.7199` edge `0.5144` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `5.5085` n `107` status `ready` deltaP `20.4511` edge `0.4786` maxDD `-7.4722`
- `risk_on_high->commodity_24h` score `5.3266` n `48` status `ready` deltaP `30.087` edge `0.2433` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3266` n `48` status `ready` deltaP `30.087` edge `0.2433` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.9132` n `52` status `ready` deltaP `35.7997` edge `0.4765` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9132` n `52` status `ready` deltaP `35.7997` edge `0.4765` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.9043` n `117` status `ready` deltaP `13.5665` edge `0.175` maxDD `-5.8734`
- `market_context_high->unknown_4h` score `1.781` n `107` status `ready` deltaP `-3.7725` edge `0.2382` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `1.5438` n `117` status `ready` deltaP `8.057` edge `0.1555` maxDD `-3.7781`
- `risk_on_high->crypto_major_1h` score `-0.1529` n `54` status `ready` deltaP `3.4986` edge `0.0293` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1529` n `54` status `ready` deltaP `3.4986` edge `0.0293` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2807` n `117` status `ready` deltaP `1.848` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_4h` score `-0.3883` n `107` status `ready` deltaP `8.7261` edge `0.014` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.4954` n `54` status `ready` deltaP `3.3101` edge `0.017` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4954` n `54` status `ready` deltaP `3.3101` edge `0.017` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.5235` n `117` status `ready` deltaP `1.3744` edge `-0.0015` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5375` n `117` status `ready` deltaP `5.6183` edge `0.0047` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5637` n `54` status `ready` deltaP `0.2052` edge `-0.0005` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
