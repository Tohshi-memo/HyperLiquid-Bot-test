# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T19:37:14.076686+00:00`
- Price records: `672`
- Market context records: `1044`
- Flow alert records: `4911`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8652`

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

- `market_context_high->crypto_major_24h` score `14.3004` n `182` status `ready` deltaP `33.0377` edge `1.0303` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5819` n `182` status `ready` deltaP `11.5084` edge `0.4285` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.0897` n `182` status `ready` deltaP `10.6357` edge `0.2654` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.3612` n `182` status `ready` deltaP `9.9254` edge `0.2114` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.6939` n `182` status `ready` deltaP `-6.9609` edge `0.3761` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0524` n `183` status `ready` deltaP `5.723` edge `0.0007` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4112` n `183` status `ready` deltaP `4.5785` edge `0.0132` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5985` n `183` status `ready` deltaP `0.0572` edge `0.0254` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6795` n `183` status `ready` deltaP `1.0291` edge `0.0173` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-1.0576` n `183` status `ready` deltaP `5.678` edge `-0.002` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.1153` n `182` status `ready` deltaP `0.7052` edge `0.002` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.3285` n `183` status `ready` deltaP `-0.0032` edge `-0.0021` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3484` n `182` status `ready` deltaP `-0.2144` edge `0.0367` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.5661` n `182` status `ready` deltaP `1.7991` edge `0.0727` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.8635` n `183` status `ready` deltaP `3.3801` edge `-0.033` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.7097` n `182` status `ready` deltaP `1.7254` edge `0.0405` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.1183` n `182` status `ready` deltaP `7.2066` edge `0.0627` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2015` n `182` status `ready` deltaP `2.6819` edge `-0.0207` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.6194` n `182` status `ready` deltaP `-5.2885` edge `0.0504` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9472` n `182` status `ready` deltaP `-0.8443` edge `-0.1571` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
