# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T10:22:12.774295+00:00`
- Price records: `672`
- Market context records: `1621`
- Flow alert records: `6574`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8824`

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

- `market_context_high->metal_24h` score `10.3397` n `191` status `ready` deltaP `25.7917` edge `0.9323` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.0145` n `191` status `ready` deltaP `17.971` edge `0.2692` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4215` n `191` status `ready` deltaP `11.6867` edge `0.15` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.5585` n `191` status `ready` deltaP `14.113` edge `0.3043` maxDD `-19.4759`
- `market_context_high->crypto_major_4h` score `0.3357` n `191` status `ready` deltaP `10.1432` edge `0.2463` maxDD `-13.3376`
- `market_context_high->equity_24h` score `0.0724` n `191` status `ready` deltaP `16.5712` edge `0.3854` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.239` n `195` status `ready` deltaP `1.3235` edge `0.0629` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.252` n `191` status `ready` deltaP `7.9207` edge `0.0311` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.4018` n `195` status `ready` deltaP `2.2156` edge `0.0326` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6598` n `195` status `ready` deltaP `0.7186` edge `0.0034` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7978` n `195` status `ready` deltaP `-0.0238` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8223` n `191` status `ready` deltaP `0.6257` edge `0.0362` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.9082` n `195` status `ready` deltaP `-1.4318` edge `0.0288` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.0315` n `195` status `ready` deltaP `0.747` edge `0.0012` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2449` n `195` status `ready` deltaP `3.8016` edge `0.0045` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3828` n `191` status `ready` deltaP `-10.5279` edge `-0.0142` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3851` n `191` status `ready` deltaP `8.9636` edge `0.094` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-1.7078` n `191` status `ready` deltaP `21.9696` edge `0.5698` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `-3.6598` n `191` status `ready` deltaP `21.9941` edge `0.7293` maxDD `-88.8062`
- `market_context_high->commodity_4h` score `-5.1873` n `191` status `ready` deltaP `-13.8808` edge `-0.1098` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
