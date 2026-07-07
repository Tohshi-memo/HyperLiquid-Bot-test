# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T09:22:30.958244+00:00`
- Price records: `672`
- Market context records: `5967`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11242`

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

- `news_risk_high->fx_24h` score `7.1055` n `30` status `ready` deltaP `65.1042` edge `0.1581` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.1285` n `30` status `ready` deltaP `37.1875` edge `0.2` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8564` n `30` status `ready` deltaP `40.0` edge `0.0593` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.134` n `30` status `ready` deltaP `25.7285` edge `0.0202` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.502` n `235` status `ready` deltaP `9.4662` edge `0.1715` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8598` n `30` status `ready` deltaP `10.489` edge `0.087` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2247` n `30` status `ready` deltaP `5.6188` edge `0.0375` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.112` n `30` status `ready` deltaP `7.5` edge `0.0228` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3822` n `30` status `ready` deltaP `1.986` edge `-0.0256` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4097` n `245` status `ready` deltaP `3.9173` edge `0.0342` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4476` n `245` status `ready` deltaP `2.9384` edge `0.0029` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5306` n `245` status `ready` deltaP `-1.9046` edge `0.0004` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6547` n `245` status `ready` deltaP `0.4216` edge `0.0046` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6751` n `245` status `ready` deltaP `-0.666` edge `-0.0007` maxDD `-0.756`
- `market_context_high->equity_24h` score `-0.8162` n `216` status `ready` deltaP `21.1805` edge `0.3109` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.1178` n `30` status `ready` deltaP `-10.5988` edge `-0.0212` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1304` n `245` status `ready` deltaP `1.8496` edge `0.0195` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.161` n `245` status `ready` deltaP `1.6052` edge `0.0157` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4126` n `235` status `ready` deltaP `-0.9555` edge `-0.0034` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.5425` n `235` status `ready` deltaP `-1.6547` edge `-0.0235` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
