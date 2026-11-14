# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T13:07:28.301661+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `573.3995` n `66` status `ready` deltaP `4.5139` edge `47.7532` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.869` n `53` status `ready` deltaP `38.7022` edge `3.0517` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.1154` n `66` status `ready` deltaP `33.7279` edge `2.8556` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `22.9322` n `66` status `ready` deltaP `57.7652` edge `1.6336` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.3771` n `53` status `ready` deltaP `42.0434` edge `2.0159` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.1854` n `53` status `ready` deltaP `35.6304` edge `0.8076` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.0382` n `53` status `ready` deltaP `48.4375` edge `0.2636` maxDD `0.0`
- `market_context_high->index_24h` score `6.9681` n `66` status `ready` deltaP `39.9936` edge `0.3232` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.6101` n `53` status `ready` deltaP `36.2486` edge `0.2562` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2064` n `66` status `ready` deltaP `51.5152` edge `0.4132` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8442` n `53` status `ready` deltaP `45.4815` edge `0.1381` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.9902` n `53` status `ready` deltaP `20.5908` edge `0.344` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6068` n `53` status `ready` deltaP `19.0628` edge `0.2365` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2369` n `53` status `ready` deltaP `29.6077` edge `0.0977` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2321` n `53` status `ready` deltaP `22.8802` edge `0.0771` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1954` n `53` status `ready` deltaP `25.5903` edge `0.0378` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `2.1699` n `53` status `ready` deltaP `26.4985` edge `0.2654` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `2.0648` n `53` status `ready` deltaP `14.4261` edge `0.6191` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2502` n `53` status `ready` deltaP `16.8766` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7429` n `53` status `ready` deltaP `17.594` edge `0.0759` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
