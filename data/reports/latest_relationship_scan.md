# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T08:07:21.236990+00:00`
- Price records: `672`
- Market context records: `1824`
- Flow alert records: `7148`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

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

- `market_context_high->crypto_alt_4h` score `6.8404` n `187` status `ready` deltaP `22.1248` edge `0.537` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8301` n `178` status `ready` deltaP `27.4169` edge `0.629` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.5268` n `30` status `ready` deltaP `29.4106` edge `0.4133` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.4298` n `187` status `ready` deltaP `25.953` edge `0.4874` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.5731` n `187` status `ready` deltaP `16.9322` edge `0.4706` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6214` n `178` status `ready` deltaP `17.8683` edge `0.3055` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2123` n `30` status `ready` deltaP `24.4212` edge `0.1366` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0038` n `187` status `ready` deltaP `16.1797` edge `0.2519` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.5535` n `178` status `ready` deltaP `13.8655` edge `0.6524` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.4452` n `178` status `ready` deltaP `16.7564` edge `0.5819` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.9042` n `30` status `ready` deltaP `21.6362` edge `-0.0011` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8206` n `187` status `ready` deltaP `11.7419` edge `0.099` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4554` n `195` status `ready` deltaP `6.4295` edge `0.0937` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3212` n `195` status `ready` deltaP `6.4709` edge `0.095` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.229` n `30` status `ready` deltaP `8.6077` edge `0.0443` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0299` n `195` status `ready` deltaP `4.9931` edge `0.0436` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.103` n `178` status `ready` deltaP `18.1648` edge `0.7289` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1682` n `178` status `ready` deltaP `11.6086` edge `0.0135` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.39` n `195` status `ready` deltaP `0.1451` edge `0.0122` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.4315` n `187` status `ready` deltaP `12.7893` edge `0.1286` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
