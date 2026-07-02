# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T10:07:28.581943+00:00`
- Price records: `672`
- Market context records: `5444`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->equity_24h` score `4.2543` n `185` status `ready` deltaP `11.8694` edge `0.629` maxDD `-21.6219`
- `market_context_high->crypto_major_4h` score `3.4905` n `196` status `ready` deltaP `16.3079` edge `0.4114` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.4771` n `185` status `ready` deltaP `17.9383` edge `0.6242` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.8779` n `196` status `ready` deltaP `13.4239` edge `0.3142` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.6787` n `196` status `ready` deltaP `11.3707` edge `0.3115` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5838` n `197` status `ready` deltaP `8.7267` edge `0.087` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2664` n `185` status `ready` deltaP `11.3447` edge `0.0361` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1781` n `197` status `ready` deltaP `7.0025` edge `0.0175` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3058` n `197` status `ready` deltaP `1.2105` edge `0.0626` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.3098` n `197` status `ready` deltaP `3.5404` edge `0.0181` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.4112` n `197` status `ready` deltaP `2.2326` edge `0.0754` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5498` n `197` status `ready` deltaP `0.4293` edge `0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7419` n `196` status `ready` deltaP `8.1446` edge `0.0448` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.1142` n `185` status `ready` deltaP `16.1627` edge `0.098` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1698` n `196` status `ready` deltaP `0.2894` edge `0.0031` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4816` n `197` status `ready` deltaP `-3.2668` edge `-0.0069` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6853` n `196` status `ready` deltaP `-8.7326` edge `-0.0336` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3073` n `196` status `ready` deltaP `-7.1273` edge `-0.0476` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-7.2281` n `185` status `ready` deltaP `8.6505` edge `0.2097` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4767` n `185` status `ready` deltaP `-5.7742` edge `-0.1823` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
