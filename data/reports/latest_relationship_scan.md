# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T19:07:31.043368+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3144`

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

- `news_risk_high->unknown_1h` score `3219.2076` n `31` status `ready` deltaP `2.231` edge `268.27` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3212.7462` n `31` status `ready` deltaP `4.3962` edge `267.7052` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `30.286` n `31` status `ready` deltaP `39.4097` edge `2.2611` maxDD `0.0`
- `news_risk_high->equity_24h` score `27.7817` n `31` status `ready` deltaP `38.5417` edge `2.0582` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.1212` n `31` status `ready` deltaP `38.7153` edge `1.752` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.2375` n `31` status `ready` deltaP `25.3884` edge `0.7709` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.2069` n `31` status `ready` deltaP `37.5295` edge `0.5651` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.9574` n `31` status `ready` deltaP `25.0896` edge `0.44` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.6347` n `31` status `ready` deltaP `18.4549` edge `0.8693` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.8734` n `31` status `ready` deltaP `41.017` edge `0.1455` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.872` n `31` status `ready` deltaP `39.9306` edge `0.1398` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4759` n `31` status `ready` deltaP `19.9874` edge `0.1751` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2136` n `31` status `ready` deltaP `35.8527` edge `0.0548` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6686` n `31` status `ready` deltaP `31.8428` edge `0.0186` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3644` n `31` status `ready` deltaP `8.813` edge `0.2905` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1248` n `31` status `ready` deltaP `11.807` edge `0.2294` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4293` n `31` status `ready` deltaP `28.3851` edge `0.0219` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8649` n `31` status `ready` deltaP `14.4915` edge `0.07` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2819` n `31` status `ready` deltaP `10.3511` edge `0.0069` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4826` n `31` status `ready` deltaP `-3.1099` edge `0.0067` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
