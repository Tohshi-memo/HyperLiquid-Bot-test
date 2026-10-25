# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T07:52:25.872486+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7926`

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

- `market_context_high->unknown_4h` score `44.0806` n `103` status `ready` deltaP `0.5121` edge `3.7035` maxDD `-1.016`
- `market_context_high->unknown_1h` score `12.7475` n `114` status `ready` deltaP `4.4831` edge `1.0813` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `7.6339` n `39` status `ready` deltaP `23.531` edge `0.5696` maxDD `-5.8917`
- `market_context_high->crypto_major_24h` score `1.8378` n `39` status `ready` deltaP `12.6736` edge `0.1746` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.7796` n `39` status `ready` deltaP `15.2778` edge `0.089` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.0494` n `114` status `ready` deltaP `3.8502` edge `0.0029` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0674` n `103` status `ready` deltaP `6.3906` edge `0.0086` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.3744` n `39` status `ready` deltaP `5.6891` edge `0.006` maxDD `-1.0212`
- `market_context_high->commodity_1h` score `-0.5517` n `114` status `ready` deltaP `-0.6618` edge `0.0085` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6203` n `114` status `ready` deltaP `4.7694` edge `-0.0043` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6534` n `114` status `ready` deltaP `-1.9908` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8849` n `103` status `ready` deltaP `-3.5179` edge `0.0329` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.4333` n `114` status `ready` deltaP `1.1136` edge `-0.0331` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.7791` n `103` status `ready` deltaP `6.398` edge `-0.0199` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0169` n `103` status `ready` deltaP `-5.0912` edge `-0.0372` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.6288` n `39` status `ready` deltaP `-5.008` edge `-0.0262` maxDD `-6.4249`
- `market_context_high->crypto_alt_1h` score `-3.1837` n `114` status `ready` deltaP `-2.5686` edge `-0.0608` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8007` n `114` status `ready` deltaP `-0.3441` edge `-0.0871` maxDD `-12.1865`
- `market_context_high->index_24h` score `-6.0478` n `39` status `ready` deltaP `-27.8312` edge `-0.1883` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-9.1255` n `103` status `ready` deltaP `-9.8493` edge `-0.1951` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
