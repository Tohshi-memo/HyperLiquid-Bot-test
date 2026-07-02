# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T04:07:29.814942+00:00`
- Price records: `672`
- Market context records: `5418`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->crypto_major_4h` score `3.9876` n `204` status `ready` deltaP `16.8819` edge `0.449` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.7149` n `193` status `ready` deltaP `19.0801` edge `0.6364` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `3.143` n `204` status `ready` deltaP `12.3296` edge `0.3438` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.5172` n `204` status `ready` deltaP `12.4851` edge `0.2904` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4447` n `204` status `ready` deltaP `8.0222` edge `0.0801` maxDD `-5.0555`
- `market_context_high->equity_24h` score `0.2668` n `193` status `ready` deltaP `8.4413` edge `0.5024` maxDD `-36.2487`
- `market_context_high->index_1h` score `0.137` n `204` status `ready` deltaP `6.713` edge `0.016` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0486` n `193` status `ready` deltaP `9.3121` edge `0.0315` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.0411` n `204` status `ready` deltaP `4.083` edge `0.0939` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.102` n `204` status `ready` deltaP `1.6878` edge `0.0764` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4243` n `204` status `ready` deltaP `-0.7074` edge `-0.0008` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.5899` n `204` status `ready` deltaP `1.089` edge `0.0111` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9519` n `204` status `ready` deltaP `6.4802` edge `0.0384` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2603` n `204` status `ready` deltaP `-0.541` edge `0.0011` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4512` n `204` status `ready` deltaP `-2.9823` edge `-0.0066` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6058` n `193` status `ready` deltaP `13.1827` edge `0.0769` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.5862` n `204` status `ready` deltaP `-6.9613` edge `-0.0327` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2052` n `204` status `ready` deltaP `-6.3755` edge `-0.0441` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.5741` n `193` status `ready` deltaP `10.2853` edge `0.2533` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.1675` n `193` status `ready` deltaP `-5.077` edge `-0.1473` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
