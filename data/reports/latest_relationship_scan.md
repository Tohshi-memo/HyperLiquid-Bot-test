# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T02:37:22.169386+00:00`
- Price records: `672`
- Market context records: `2203`
- Flow alert records: `8233`
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

- `market_context_high->crypto_alt_4h` score `12.6687` n `132` status `ready` deltaP `36.2343` edge `0.9078` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6822` n `132` status `ready` deltaP `41.6713` edge `0.7487` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4635` n `132` status `ready` deltaP `21.3738` edge `0.3807` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8158` n `43` status `ready` deltaP `31.7002` edge `0.345` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3625` n `132` status `ready` deltaP `22.9583` edge `0.2366` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.241` n `132` status `ready` deltaP `17.7146` edge `0.1997` maxDD `-1.817`
- `market_context_high->unknown_24h` score `3.2039` n `132` status `ready` deltaP `27.4622` edge `0.5654` maxDD `-32.8525`
- `market_context_high->index_4h` score `3.12` n `132` status `ready` deltaP `25.5543` edge `0.158` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9135` n `132` status `ready` deltaP `15.7594` edge `0.2241` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.4776` n `132` status `ready` deltaP `10.9059` edge `0.2566` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1976` n `43` status `ready` deltaP `27.8892` edge `0.0156` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.0851` n `132` status `ready` deltaP `18.4974` edge `0.9722` maxDD `-60.2561`
- `news_risk_high->unknown_1h` score `1.4263` n `43` status `ready` deltaP `21.3445` edge `0.0235` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.2999` n `43` status `ready` deltaP `14.4675` edge `0.0842` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.2771` n `132` status `ready` deltaP `16.6759` edge `0.134` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.2031` n `43` status `ready` deltaP `-3.7507` edge `0.3` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7557` n `43` status `ready` deltaP `10.7645` edge `0.0931` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4489` n `43` status `ready` deltaP `7.9898` edge `0.0098` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3628` n `132` status `ready` deltaP `9.6398` edge `0.0448` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.2095` n `43` status `ready` deltaP `5.0063` edge `0.0455` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
