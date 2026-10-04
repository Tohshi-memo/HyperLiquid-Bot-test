# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T14:22:27.931949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5032`

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

- `market_context_high->unknown_4h` score `107.4611` n `87` status `ready` deltaP `2.7526` edge `8.9679` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `95.6084` n `97` status `ready` deltaP `-0.6096` edge `8.0129` maxDD `-0.9839`
- `market_context_high->crypto_alt_24h` score `10.6837` n `46` status `ready` deltaP `27.1362` edge `0.8367` maxDD `-8.1838`
- `news_risk_high->crypto_major_4h` score `10.5349` n `65` status `ready` deltaP `37.4297` edge `0.6487` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.3788` n `46` status `ready` deltaP `33.5748` edge `0.7063` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.6535` n `65` status `ready` deltaP `24.5754` edge `0.5673` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.2911` n `65` status `ready` deltaP `24.3598` edge `0.5796` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.4069` n `87` status `ready` deltaP `23.2829` edge `0.3657` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.0167` n `65` status `ready` deltaP `27.6042` edge `0.1507` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8116` n `65` status `ready` deltaP `25.9123` edge `0.2059` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0916` n `65` status `ready` deltaP `33.5906` edge `0.0599` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8992` n `65` status `ready` deltaP `12.561` edge `0.1934` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5756` n `65` status `ready` deltaP `22.1271` edge `0.1087` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.1608` n `97` status `ready` deltaP `15.4794` edge `0.1219` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.1122` n `46` status `ready` deltaP `4.6422` edge `0.2442` maxDD `-6.264`
- `news_risk_high->index_1h` score `2.0842` n `65` status `ready` deltaP `25.6172` edge `0.0179` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.539` n `65` status `ready` deltaP `5.1681` edge `0.1457` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.4474` n `87` status `ready` deltaP `4.1299` edge `0.272` maxDD `-7.6465`
- `market_context_high->fx_24h` score `1.3599` n `46` status `ready` deltaP `25.536` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_4h` score `1.3593` n `87` status `ready` deltaP `24.2763` edge `0.0271` maxDD `-0.3868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
