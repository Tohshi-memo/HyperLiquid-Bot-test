# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T04:22:25.989970+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5068`

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

- `market_context_high->unknown_4h` score `322.4108` n `50` status `ready` deltaP `11.872` edge `26.7957` maxDD `-0.249`
- `market_context_high->unknown_1h` score `259.3243` n `62` status `ready` deltaP `1.8013` edge `21.6398` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `13.473` n `49` status `ready` deltaP `29.0631` edge `1.0825` maxDD `-10.2806`
- `news_risk_high->equity_24h` score `11.7972` n `59` status `ready` deltaP `30.8286` edge `0.7876` maxDD `-0.1353`
- `market_context_high->crypto_major_24h` score `11.4662` n `49` status `ready` deltaP `34.9733` edge `0.8409` maxDD `-7.8161`
- `news_risk_high->crypto_major_4h` score `10.9764` n `65` status `ready` deltaP `40.1736` edge `0.6672` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4714` n `65` status `ready` deltaP `24.6646` edge `0.5926` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.7948` n `50` status `ready` deltaP `15.8659` edge `0.5308` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.2314` n `50` status `ready` deltaP `14.6646` edge `0.4671` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.9899` n `59` status `ready` deltaP `34.4887` edge `0.1859` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9193` n `65` status `ready` deltaP `27.1318` edge `0.207` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1148` n `65` status `ready` deltaP `33.8954` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9723` n `65` status `ready` deltaP `13.3095` edge `0.1945` maxDD `-1.5096`
- `market_context_high->fx_4h` score `2.8472` n `50` status `ready` deltaP `32.3659` edge `0.0392` maxDD `-0.0834`
- `news_risk_high->metal_4h` score `2.5646` n `65` status `ready` deltaP `21.9747` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.5372` n `62` status `ready` deltaP `13.2847` edge `0.1679` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.1201` n `65` status `ready` deltaP `26.0663` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.1004` n `62` status `ready` deltaP `9.1607` edge `0.1886` maxDD `-3.6376`
- `market_context_high->equity_24h` score `1.6097` n `49` status `ready` deltaP `6.9961` edge `0.323` maxDD `-10.3952`
- `news_risk_high->crypto_alt_1h` score `1.4851` n `65` status `ready` deltaP `4.719` edge `0.1442` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
