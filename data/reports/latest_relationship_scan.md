# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T21:07:31.764140+00:00`
- Price records: `672`
- Market context records: `6540`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `news_risk_high->crypto_alt_24h` score `13.5826` n `30` status `ready` deltaP `37.3541` edge `0.8976` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6326` n `30` status `ready` deltaP `55.1127` edge `0.1853` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3667` n `144` status `ready` deltaP `11.8934` edge `0.7813` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.6634` n `30` status `ready` deltaP `20.1791` edge `0.5413` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7223` n `36` status `ready` deltaP `39.1938` edge `0.0535` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.6203` n `30` status `ready` deltaP `26.9151` edge `0.0484` maxDD `-0.0911`
- `news_risk_high->fx_1h` score `2.1232` n `36` status `ready` deltaP `26.4138` edge `0.0189` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.974` n `196` status `ready` deltaP `-6.4493` edge `0.2976` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4193` n `144` status `ready` deltaP `13.304` edge `0.2164` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6349` n `186` status `ready` deltaP `13.867` edge `0.0281` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5911` n `36` status `ready` deltaP `6.2375` edge `0.0879` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3626` n `186` status `ready` deltaP `10.079` edge `0.1184` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `-0.0955` n `36` status `ready` deltaP `-0.2994` edge `0.0407` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.2935` n `186` status `ready` deltaP `10.6724` edge `0.0611` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.3383` n `30` status `ready` deltaP `6.1929` edge `0.0025` maxDD `-2.3058`
- `market_context_high->crypto_major_4h` score `-0.3901` n `186` status `ready` deltaP `12.6065` edge `0.095` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.429` n `196` status `ready` deltaP `-0.4002` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4521` n `196` status `ready` deltaP `1.7475` edge `-0.0013` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5356` n `196` status `ready` deltaP `6.3333` edge `0.0204` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5525` n `196` status `ready` deltaP `6.0675` edge `0.0153` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
