# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T00:22:25.601925+00:00`
- Price records: `672`
- Market context records: `2405`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `20.6809` n `43` status `ready` deltaP `47.6057` edge `1.4649` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1486` n `43` status `ready` deltaP `49.2369` edge `1.2281` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2911` n `43` status `ready` deltaP `29.7925` edge `1.1071` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.1592` n `43` status `ready` deltaP `18.8993` edge `0.862` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2235` n `43` status `ready` deltaP `27.9877` edge `0.5213` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.4569` n `113` status `ready` deltaP `22.9044` edge `0.3432` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3918` n `43` status `ready` deltaP `12.7504` edge `0.4062` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8942` n `136` status `ready` deltaP `23.9778` edge `0.429` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `3.8633` n `136` status `ready` deltaP `19.4764` edge `0.46` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6055` n `43` status `ready` deltaP `37.924` edge `0.0661` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2615` n `43` status `ready` deltaP `30.1758` edge `0.2841` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.0966` n `113` status `ready` deltaP `14.6186` edge `0.6888` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.5035` n `136` status `ready` deltaP `13.4684` edge `0.1798` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1536` n `43` status `ready` deltaP `27.2794` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6645` n `43` status `ready` deltaP `15.2297` edge `0.1095` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.4797` n `113` status `ready` deltaP `9.7868` edge `0.1058` maxDD `-1.1522`
- `market_context_high->crypto_major_1h` score `1.4348` n `136` status `ready` deltaP `13.3322` edge `0.1501` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1337` n `43` status `ready` deltaP `20.2966` edge `0.0061` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9552` n `136` status `ready` deltaP `8.8103` edge `0.1396` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.7672` n `136` status `ready` deltaP `13.3967` edge `0.0572` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
