# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T07:06:35.331704+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_1h` score `443.5709` n `82` status `ready` deltaP `-5.999` edge `37.0464` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.0267` n `82` status `ready` deltaP `40.513` edge `1.4476` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.8289` n `82` status `ready` deltaP `36.2995` edge `1.3908` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.9702` n `82` status `ready` deltaP `35.7191` edge `0.9374` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2325` n `82` status `ready` deltaP `59.4911` edge `0.3071` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.8042` n `79` status `ready` deltaP `39.8276` edge `0.3015` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.209` n `41` status `ready` deltaP `39.8276` edge `0.2519` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.209` n `41` status `ready` deltaP `39.8276` edge `0.2519` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.6618` n `82` status `ready` deltaP `34.0707` edge `0.2901` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.2884` n `41` status `ready` deltaP `58.9403` edge `0.052` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.2884` n `41` status `ready` deltaP `58.9403` edge `0.052` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7063` n `79` status `ready` deltaP `53.7844` edge `0.0552` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9611` n `52` status `ready` deltaP `26.5947` edge `0.0211` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9611` n `52` status `ready` deltaP `26.5947` edge `0.0211` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7614` n `137` status `ready` deltaP `22.0046` edge `0.0419` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7742` n `137` status `ready` deltaP `12.9617` edge `0.0158` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6481` n `82` status `ready` deltaP `16.1585` edge `0.0382` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3262` n `137` status `ready` deltaP `11.9881` edge `0.0095` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2587` n `52` status `ready` deltaP `7.3469` edge `0.0078` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2587` n `52` status `ready` deltaP `7.3469` edge `0.0078` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
