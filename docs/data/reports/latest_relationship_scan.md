# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T14:22:36.281458+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `371.9474` n `75` status `ready` deltaP `5.1458` edge `30.9754` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.4943` n `53` status `ready` deltaP `31.0633` edge `2.5714` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.2607` n `75` status `ready` deltaP `25.6041` edge `2.0052` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.2599` n `75` status `ready` deltaP `51.2292` edge `1.4316` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2001` n `53` status `ready` deltaP `42.0434` edge `1.7368` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.0979` n `53` status `ready` deltaP `33.4963` edge `0.7312` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.6364` n `53` status `ready` deltaP `36.2847` edge `0.2278` maxDD `0.0`
- `market_context_high->index_24h` score `4.6913` n `75` status `ready` deltaP `24.8681` edge `0.2343` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.5828` n `53` status `ready` deltaP `43.8047` edge `0.1275` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0103` n `53` status `ready` deltaP `22.8806` edge `0.212` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.8084` n `75` status `ready` deltaP `37.8611` edge `0.325` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.2615` n `53` status `ready` deltaP `17.4161` edge `0.2187` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9581` n `53` status `ready` deltaP `27.4736` edge `0.0887` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.8547` n `53` status `ready` deltaP `18.4567` edge `0.2636` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.6631` n `53` status `ready` deltaP `18.0719` edge `0.6715` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0852` n `53` status `ready` deltaP `24.6921` edge `0.0346` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.8942` n `53` status `ready` deltaP `19.5266` edge `0.0713` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7458` n `53` status `ready` deltaP `25.7363` edge `0.2161` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1603` n `53` status `ready` deltaP `15.9784` edge `0.0203` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5309` n `53` status `ready` deltaP `16.3964` edge `0.0567` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
