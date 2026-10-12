# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T03:07:24.920910+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `654.0844` n `52` status `ready` deltaP `-16.8002` edge `54.6554` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `35.5075` n `117` status `ready` deltaP `-7.4682` edge `3.0793` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.8383` n `52` status `ready` deltaP `27.6175` edge `0.5953` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.9419` n `52` status `ready` deltaP `50.6811` edge `0.1616` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.3799` n `38` status `ready` deltaP `30.5841` edge `0.3297` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.3799` n `38` status `ready` deltaP `30.5841` edge `0.3297` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.1051` n `38` status `ready` deltaP `24.3742` edge `0.3077` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.1051` n `38` status `ready` deltaP `24.3742` edge `0.3077` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `4.2474` n `52` status `ready` deltaP `-2.0165` edge `0.8728` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `3.3067` n `38` status `ready` deltaP `30.0545` edge `0.0984` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.3067` n `38` status `ready` deltaP `30.0545` edge `0.0984` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.5059` n `50` status `ready` deltaP `10.1078` edge `0.1178` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.5059` n `50` status `ready` deltaP `10.1078` edge `0.1178` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.473` n `50` status `ready` deltaP `13.4012` edge `0.0987` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.473` n `50` status `ready` deltaP `13.4012` edge `0.0987` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.4214` n `50` status `ready` deltaP `17.6048` edge `0.025` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.4214` n `50` status `ready` deltaP `17.6048` edge `0.025` maxDD `-0.2466`
- `market_context_high->fx_24h` score `0.5078` n `52` status `ready` deltaP `12.2996` edge `0.0164` maxDD `-0.4866`
- `market_context_high->metal_4h` score `0.4234` n `117` status `ready` deltaP `11.7235` edge `0.0294` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `0.304` n `129` status `ready` deltaP `5.7977` edge `0.0901` maxDD `-4.9401`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
