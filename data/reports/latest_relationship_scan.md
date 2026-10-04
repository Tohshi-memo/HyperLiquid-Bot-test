# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T04:37:32.742033+00:00`
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

- `market_context_high->unknown_4h` score `321.1004` n `50` status `ready` deltaP `10.0244` edge `26.7059` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `241.3891` n `62` status `ready` deltaP `1.8013` edge `20.1452` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.0665` n `48` status `ready` deltaP `30.4628` edge `1.1118` maxDD `-9.4143`
- `market_context_high->crypto_major_24h` score `12.2593` n `48` status `ready` deltaP `36.5432` edge `0.8763` maxDD `-6.5318`
- `news_risk_high->equity_24h` score `11.7497` n `59` status `ready` deltaP `30.6553` edge `0.7848` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `10.9932` n `65` status `ready` deltaP `40.1736` edge `0.6686` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.493` n `65` status `ready` deltaP `24.6646` edge `0.5944` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.5908` n `50` status `ready` deltaP `15.8659` edge `0.5138` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.9736` n `59` status `ready` deltaP `34.3154` edge `0.1857` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.965` n `50` status `ready` deltaP `14.6646` edge `0.4449` maxDD `-7.6465`
- `news_risk_high->equity_4h` score `3.9217` n `65` status `ready` deltaP `27.1318` edge `0.2072` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1282` n `65` status `ready` deltaP `34.0479` edge `0.0599` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9699` n `65` status `ready` deltaP `13.3095` edge `0.1943` maxDD `-1.5096`
- `market_context_high->fx_4h` score `2.7968` n `50` status `ready` deltaP `32.3659` edge `0.0392` maxDD `-0.0855`
- `market_context_high->crypto_major_1h` score `2.5648` n `62` status `ready` deltaP `13.2847` edge `0.1702` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5646` n `65` status `ready` deltaP `21.9747` edge `0.1088` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1333` n `65` status `ready` deltaP `26.216` edge `0.018` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.1016` n `62` status `ready` deltaP `9.1607` edge `0.1887` maxDD `-3.6376`
- `market_context_high->equity_24h` score `2.0678` n `48` status `ready` deltaP `8.2683` edge `0.3523` maxDD `-9.0519`
- `news_risk_high->crypto_alt_1h` score `1.4851` n `65` status `ready` deltaP `4.719` edge `0.1442` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
