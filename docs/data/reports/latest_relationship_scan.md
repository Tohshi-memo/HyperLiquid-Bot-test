# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T04:52:31.999058+00:00`
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

- `market_context_high->unknown_4h` score `320.1008` n `50` status `ready` deltaP `10.0244` edge `26.6226` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `241.1443` n `62` status `ready` deltaP `1.8013` edge `20.1248` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.672` n `47` status `ready` deltaP `31.9296` edge `1.1422` maxDD `-8.592`
- `market_context_high->crypto_major_24h` score `13.0107` n `47` status `ready` deltaP `38.1872` edge `0.91` maxDD `-5.4287`
- `news_risk_high->equity_24h` score `11.7023` n `59` status `ready` deltaP `30.482` edge `0.782` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.0148` n `65` status `ready` deltaP `40.1736` edge `0.6704` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.517` n `65` status `ready` deltaP `24.6646` edge `0.5964` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.3388` n `50` status `ready` deltaP `15.8659` edge `0.4928` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.9562` n `59` status `ready` deltaP `34.1421` edge `0.1854` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9229` n `65` status `ready` deltaP `27.1318` edge `0.2073` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1404` n `65` status `ready` deltaP `34.2003` edge `0.0599` maxDD `-0.4296`
- `market_context_high->crypto_alt_4h` score `3.0393` n `50` status `ready` deltaP `14.6646` edge `0.4208` maxDD `-7.6465`
- `news_risk_high->crypto_major_1h` score `2.9771` n `65` status `ready` deltaP `13.3095` edge `0.1949` maxDD `-1.5096`
- `market_context_high->fx_4h` score `2.5977` n `50` status `ready` deltaP `30.5183` edge `0.0391` maxDD `-0.0864`
- `news_risk_high->metal_4h` score `2.5646` n `65` status `ready` deltaP `21.9747` edge `0.1088` maxDD `-0.993`
- `market_context_high->equity_24h` score `2.5474` n `47` status `ready` deltaP `9.6021` edge `0.3836` maxDD `-7.6822`
- `market_context_high->crypto_major_1h` score `2.494` n `62` status `ready` deltaP `13.2847` edge `0.1643` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.1333` n `65` status `ready` deltaP `26.216` edge `0.018` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.05` n `62` status `ready` deltaP `9.1607` edge `0.1844` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.4911` n `65` status `ready` deltaP `4.719` edge `0.1447` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
