# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T14:37:25.360179+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `764.3292` n `136` status `ready` deltaP `1.2153` edge `63.686` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.3672` n `40` status `ready` deltaP `10.2246` edge `12.9671` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `58.0147` n `36` status `ready` deltaP `29.8611` edge `4.6706` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.992` n `36` status `ready` deltaP `35.5903` edge `2.3768` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `29.8121` n `36` status `ready` deltaP `14.5833` edge `2.4251` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.5964` n `36` status `ready` deltaP `33.1597` edge `0.5041` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `5.2138` n `40` status `ready` deltaP `20.2134` edge `0.354` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.4468` n `36` status `ready` deltaP `39.9306` edge `0.1282` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.0565` n `40` status `ready` deltaP `25.4573` edge `0.2018` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.2549` n `40` status `ready` deltaP `35.7012` edge `0.0403` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.7565` n `40` status `ready` deltaP `10.8537` edge `0.2478` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.8174` n `40` status `ready` deltaP `19.9102` edge `0.059` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.6696` n `40` status `ready` deltaP `11.6617` edge `0.1503` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.5162` n `40` status `ready` deltaP `12.006` edge `0.1321` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.1026` n `40` status `ready` deltaP `15.2096` edge `0.01` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9389` n `40` status `ready` deltaP `15.8383` edge `0.0083` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.9277` n `136` status `ready` deltaP `16.8199` edge `0.0347` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4611` n `136` status `ready` deltaP `15.2574` edge `0.1222` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.4325` n `40` status `ready` deltaP `7.8354` edge `0.0217` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.0887` n `139` status `ready` deltaP `2.7636` edge `0.0032` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
