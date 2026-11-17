# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T19:56:06.553914+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4041`

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

- `market_context_high->unknown_24h` score `1491.1062` n `98` status `ready` deltaP `3.4722` edge `124.2357` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.6387` n `38` status `ready` deltaP `67.023` edge `4.3437` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.0858` n `38` status `ready` deltaP `55.4878` edge `1.3039` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.4974` n `38` status `ready` deltaP `32.0541` edge `2.0157` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `15.3421` n `98` status `ready` deltaP `46.0176` edge `1.9872` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.5326` n `98` status `ready` deltaP `32.2527` edge `1.8605` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.1176` n `38` status `ready` deltaP `58.3424` edge `0.4012` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.9385` n `38` status `ready` deltaP `54.8611` edge `0.2958` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.5999` n `38` status `ready` deltaP `31.611` edge `0.4993` maxDD `-4.137`
- `news_risk_high->metal_4h` score `6.7545` n `38` status `ready` deltaP `55.4477` edge `0.1977` maxDD `-0.0246`
- `news_risk_high->crypto_alt_24h` score `6.2626` n `38` status `ready` deltaP `14.1539` edge `1.1591` maxDD `-29.0448`
- `news_risk_high->crypto_major_4h` score `5.7351` n `38` status `ready` deltaP `23.8688` edge `0.3615` maxDD `-1.7491`
- `news_risk_high->equity_1h` score `5.7137` n `38` status `ready` deltaP `26.3788` edge `0.3221` maxDD `-0.4122`
- `news_risk_high->index_4h` score `4.3624` n `38` status `ready` deltaP `37.7567` edge `0.1343` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `2.6712` n `38` status `ready` deltaP `17.7356` edge `0.1395` maxDD `-1.4777`
- `news_risk_high->metal_1h` score `2.6706` n `38` status `ready` deltaP `28.5613` edge `0.0539` maxDD `-0.0743`
- `news_risk_high->commodity_4h` score `2.628` n `38` status `ready` deltaP `28.2975` edge `0.0557` maxDD `-0.3611`
- `news_risk_high->crypto_alt_1h` score `2.1481` n `38` status `ready` deltaP `16.4513` edge `0.122` maxDD `-2.5469`
- `news_risk_high->index_1h` score `2.0513` n `38` status `ready` deltaP `24.0466` edge `0.0324` maxDD `-0.0751`
- `news_risk_high->commodity_1h` score `0.0721` n `38` status `ready` deltaP `2.2455` edge `0.0245` maxDD `-0.3438`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
