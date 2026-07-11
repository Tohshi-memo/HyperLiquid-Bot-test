# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T13:37:28.878433+00:00`
- Price records: `672`
- Market context records: `6395`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11075`

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

- `news_risk_high->crypto_alt_24h` score `13.8455` n `32` status `ready` deltaP `36.1111` edge `0.9278` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5803` n `32` status `ready` deltaP `55.2083` edge `0.1803` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.4225` n `32` status `ready` deltaP `38.3681` edge `0.1333` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.2412` n `32` status `ready` deltaP `17.5347` edge `0.5048` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.023` n `32` status `ready` deltaP `41.6921` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4087` n `32` status `ready` deltaP `29.0419` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.45` n `32` status `ready` deltaP `13.8286` edge `0.1404` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8239` n `32` status `ready` deltaP `10.2732` edge `0.0833` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5667` n `216` status `ready` deltaP `12.867` edge `0.0411` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2964` n `221` status `ready` deltaP `-5.9386` edge `0.1651` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1457` n `216` status `ready` deltaP `8.7568` edge `0.0214` maxDD `-0.4108`
- `market_context_high->metal_24h` score `-0.2117` n `146` status `ready` deltaP `19.6205` edge `0.0989` maxDD `-11.8809`
- `news_risk_high->unknown_1h` score `-0.2129` n `32` status `ready` deltaP `6.8301` edge `-0.0288` maxDD `-0.7581`
- `market_context_high->equity_4h` score `-0.4725` n `216` status `ready` deltaP `8.7003` edge `0.0513` maxDD `-8.2573`
- `market_context_high->metal_1h` score `-0.4799` n `221` status `ready` deltaP `2.0464` edge `0.0026` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6531` n `32` status `ready` deltaP `-1.3473` edge `-0.025` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.6792` n `221` status `ready` deltaP `-0.2567` edge `-0.0015` maxDD `-0.9376`
- `market_context_high->index_1h` score `-0.6937` n `221` status `ready` deltaP `-2.9378` edge `0.0026` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7471` n `32` status `ready` deltaP `0.5208` edge `-0.0121` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.7498` n `221` status `ready` deltaP `-3.6931` edge `-0.0032` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
