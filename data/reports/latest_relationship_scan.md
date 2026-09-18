# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T09:22:28.797433+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8314`

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

- `market_context_high->unknown_4h` score `39.78` n `149` status `ready` deltaP `-0.311` edge `3.3404` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.6587` n `52` status `ready` deltaP `-7.5516` edge `1.2111` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.6587` n `52` status `ready` deltaP `-7.5516` edge `1.2111` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8732` n `52` status `ready` deltaP `50.0` edge `0.4061` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8732` n `52` status `ready` deltaP `50.0` edge `0.4061` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5741` n `149` status `ready` deltaP `43.2886` edge `0.3951` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8535` n `52` status `ready` deltaP `32.8447` edge `0.0538` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8535` n `52` status `ready` deltaP `32.8447` edge `0.0538` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7532` n `149` status `ready` deltaP `29.347` edge `0.0756` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.7476` n `81` status `ready` deltaP `18.7537` edge `0.4423` maxDD `-12.8718`
- `news_risk_high->equity_4h` score `1.2462` n `81` status `ready` deltaP `15.3248` edge `0.1413` maxDD `-3.3619`
- `market_context_high->commodity_1h` score `1.1696` n `149` status `ready` deltaP `16.66` edge `0.0241` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `1.0302` n `52` status `ready` deltaP `19.2575` edge `-0.0383` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.0302` n `52` status `ready` deltaP `19.2575` edge `-0.0383` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.8953` n `149` status `ready` deltaP `16.4826` edge `-0.0137` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5464` n `52` status `ready` deltaP `9.7421` edge `0.0158` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5464` n `52` status `ready` deltaP `9.7421` edge `0.0158` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.3825` n `93` status `ready` deltaP `11.0859` edge `0.0273` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2562` n `81` status `ready` deltaP `8.2675` edge `0.0224` maxDD `-0.2398`
- `news_risk_high->index_1h` score `-0.0201` n `93` status `ready` deltaP `4.2125` edge `0.0009` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
