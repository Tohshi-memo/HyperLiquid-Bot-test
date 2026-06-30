# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T15:22:32.477317+00:00`
- Price records: `672`
- Market context records: `5260`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `26.7994` n `146` status `ready` deltaP `30.4009` edge `2.0396` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `10.6927` n `146` status `ready` deltaP `28.9003` edge `1.0588` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.0596` n `158` status `ready` deltaP `14.0669` edge `0.4086` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8191` n `158` status `ready` deltaP `14.2656` edge `0.4524` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.2996` n `146` status `ready` deltaP `19.4326` edge `0.7083` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.9403` n `158` status `ready` deltaP `17.1311` edge `0.1497` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.6301` n `158` status `ready` deltaP `8.7412` edge `0.1581` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5132` n `146` status `ready` deltaP `12.5547` edge `0.0486` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.503` n `168` status `ready` deltaP `4.4803` edge `0.1082` maxDD `-5.0257`
- `market_context_high->crypto_alt_24h` score `0.4033` n `146` status `ready` deltaP `15.7605` edge `0.5513` maxDD `-37.0395`
- `market_context_high->crypto_major_1h` score `0.241` n `168` status `ready` deltaP `5.3892` edge `0.1087` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.216` n `146` status `ready` deltaP `20.8476` edge `0.0522` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0128` n `168` status `ready` deltaP `5.9346` edge `0.0559` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.1022` n `168` status `ready` deltaP `4.598` edge `0.0112` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1313` n `168` status `ready` deltaP `4.7762` edge `0.0164` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2464` n `168` status `ready` deltaP `1.9176` edge `0.0004` maxDD `-0.5823`
- `market_context_high->unknown_1h` score `-0.4875` n `168` status `ready` deltaP `7.4138` edge `-0.0259` maxDD `-2.7986`
- `market_context_high->index_4h` score `-0.7024` n `158` status `ready` deltaP `4.9803` edge `0.02` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.788` n `158` status `ready` deltaP `0.1949` edge `0.0006` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.2411` n `168` status `ready` deltaP `-2.0887` edge `-0.0054` maxDD `-2.728`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
