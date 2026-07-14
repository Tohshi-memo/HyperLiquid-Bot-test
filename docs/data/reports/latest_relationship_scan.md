# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T18:07:32.750013+00:00`
- Price records: `672`
- Market context records: `6733`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_24h` score `1.3447` n `176` status `ready` deltaP `2.7935` edge `0.529` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0384` n `176` status `ready` deltaP `8.2506` edge `0.0359` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.074` n `176` status `ready` deltaP `5.6478` edge `0.0326` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.3262` n `176` status `ready` deltaP `7.9704` edge `0.1065` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3306` n `176` status `ready` deltaP `0.7825` edge `0.0009` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5915` n `176` status `ready` deltaP `0.296` edge `-0.0095` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6162` n `176` status `ready` deltaP `-1.167` edge `0.0002` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.684` n `176` status `ready` deltaP `-4.9912` edge `-0.0019` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1136` n `176` status `ready` deltaP `3.5554` edge `-0.0138` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2082` n `176` status `ready` deltaP `6.5964` edge `-0.0109` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2161` n `176` status `ready` deltaP `7.5388` edge `0.0002` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4758` n `176` status `ready` deltaP `-1.7738` edge `-0.0284` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.8568` n `176` status `ready` deltaP `-7.9239` edge `-0.0118` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.1372` n `176` status `ready` deltaP `6.0976` edge `0.0168` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.3473` n `176` status `ready` deltaP `3.7416` edge `0.0143` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.605` n `176` status `ready` deltaP `-6.3193` edge `-0.0058` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.9141` n `176` status `ready` deltaP `5.4462` edge `-0.1112` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-3.9448` n `176` status `ready` deltaP `-17.6968` edge `0.0258` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3611` n `176` status `ready` deltaP `-8.7437` edge `-0.0015` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.7158` n `176` status `ready` deltaP `-9.6433` edge `-0.0764` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
