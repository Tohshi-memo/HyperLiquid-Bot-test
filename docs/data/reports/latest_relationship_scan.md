# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T07:37:24.799587+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5004`

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

- `market_context_high->unknown_4h` score `235.4331` n `60` status `ready` deltaP `7.6626` edge `19.5827` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `184.6745` n `72` status `ready` deltaP `1.9794` edge `15.4178` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.0816` n `46` status `ready` deltaP `31.7346` edge `1.0892` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `12.9226` n `46` status `ready` deltaP `38.1772` edge `0.8876` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `11.1252` n `65` status `ready` deltaP `40.1736` edge `0.6796` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `11.0866` n `59` status `ready` deltaP `28.5756` edge `0.7434` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.5542` n `65` status `ready` deltaP `24.6646` edge `0.5995` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.2278` n `60` status `ready` deltaP `21.1992` edge `0.448` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.3326` n `60` status `ready` deltaP `19.6646` edge `0.4422` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.7593` n `59` status `ready` deltaP `32.2357` edge `0.1817` maxDD `0.0`
- `market_context_high->equity_24h` score `4.1124` n `46` status `ready` deltaP `9.2683` edge `0.3806` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9433` n `65` status `ready` deltaP `27.1318` edge `0.209` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1952` n `65` status `ready` deltaP `34.8101` edge `0.0604` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.0287` n `65` status `ready` deltaP `13.3095` edge `0.1992` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6116` n `72` status `ready` deltaP `16.6001` edge `0.152` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5768` n `65` status `ready` deltaP `22.1271` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_alt_1h` score `2.2035` n `72` status `ready` deltaP `13.0739` edge `0.1711` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.1693` n `65` status `ready` deltaP `26.6651` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5739` n `65` status `ready` deltaP `4.8687` edge `0.1506` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4617` n `60` status `ready` deltaP `20.3659` edge `0.031` maxDD `-0.2636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
