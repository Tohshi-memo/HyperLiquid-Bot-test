# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T07:07:35.488408+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7918`

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

- `market_context_high->unknown_4h` score `47.0536` n `100` status `ready` deltaP `0.8354` edge `3.9491` maxDD `-1.016`
- `market_context_high->unknown_1h` score `14.2332` n `112` status `ready` deltaP `4.1542` edge `1.2073` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `10.5583` n `36` status `ready` deltaP `29.5139` edge `0.7439` maxDD `-4.1975`
- `market_context_high->crypto_major_24h` score `2.9111` n `36` status `ready` deltaP `18.2291` edge `0.227` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.6278` n `36` status `ready` deltaP `12.6736` edge `0.0869` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.0787` n `112` status `ready` deltaP `3.2881` edge `0.0029` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.1152` n `36` status `ready` deltaP `8.6806` edge `0.006` maxDD `-0.958`
- `market_context_high->fx_4h` score `-0.1202` n `100` status `ready` deltaP `5.4207` edge `0.0083` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.6134` n `112` status `ready` deltaP `-1.358` edge `0.008` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6419` n `112` status `ready` deltaP `-1.7697` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6605` n `112` status `ready` deltaP `4.3413` edge `-0.0048` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.8992` n `100` status `ready` deltaP `-3.7927` edge `0.0329` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.4121` n `112` status `ready` deltaP `1.3259` edge `-0.0318` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.9323` n `100` status `ready` deltaP `4.7378` edge `-0.0216` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0165` n `100` status `ready` deltaP `-4.9329` edge `-0.0382` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.4133` n `36` status `ready` deltaP `-3.2986` edge `-0.0346` maxDD `-6.2283`
- `market_context_high->crypto_alt_1h` score `-2.9646` n `112` status `ready` deltaP `-1.62` edge `-0.0572` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7284` n `112` status `ready` deltaP `0.6202` edge `-0.0875` maxDD `-12.1865`
- `market_context_high->crypto_major_4h` score `-5.8518` n `100` status `ready` deltaP `-9.1707` edge `-0.1894` maxDD `-33.3092`
- `market_context_high->index_24h` score `-6.6303` n `36` status `ready` deltaP `-33.507` edge `-0.199` maxDD `-5.078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
