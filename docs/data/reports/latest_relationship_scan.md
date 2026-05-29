# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T02:52:17.646523+00:00`
- Price records: `672`
- Market context records: `2204`
- Flow alert records: `8236`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.6869` n `132` status `ready` deltaP `36.3868` edge `0.9083` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.687` n `132` status `ready` deltaP `41.6713` edge `0.7491` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4659` n `132` status `ready` deltaP `21.3738` edge `0.3809` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8182` n `43` status `ready` deltaP `31.7002` edge `0.3453` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3649` n `132` status `ready` deltaP `22.9583` edge `0.2368` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.241` n `132` status `ready` deltaP `17.7146` edge `0.1997` maxDD `-1.817`
- `market_context_high->unknown_24h` score `3.1655` n `132` status `ready` deltaP `27.4622` edge `0.5622` maxDD `-32.8525`
- `market_context_high->index_4h` score `3.1346` n `132` status `ready` deltaP `25.7068` edge `0.1582` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9135` n `132` status `ready` deltaP `15.7594` edge `0.2241` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.4608` n `132` status `ready` deltaP `10.9059` edge `0.2552` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1988` n `43` status `ready` deltaP `27.8892` edge `0.0157` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.0484` n `132` status `ready` deltaP `18.4974` edge `0.9675` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4323` n `43` status `ready` deltaP `21.3445` edge `0.024` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3023` n `43` status `ready` deltaP `14.4675` edge `0.0844` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.2577` n `132` status `ready` deltaP `16.5235` edge `0.1334` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.2047` n `43` status `ready` deltaP `-3.7507` edge `0.3002` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.765` n `43` status `ready` deltaP `10.9142` edge `0.0933` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3628` n `132` status `ready` deltaP `9.6398` edge `0.0448` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.2095` n `43` status `ready` deltaP `5.0063` edge `0.0455` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
