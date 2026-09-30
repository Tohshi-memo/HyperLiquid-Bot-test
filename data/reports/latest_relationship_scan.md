# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T09:22:36.938348+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `news_risk_high->unknown_24h` score `672.094` n `135` status `ready` deltaP `1.9097` edge `55.9951` maxDD `0.0`
- `market_context_high->unknown_1h` score `510.8346` n `43` status `ready` deltaP `7.5546` edge `42.5241` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `445.2621` n `31` status `ready` deltaP `8.2317` edge `37.0503` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.4928` n `135` status `ready` deltaP `28.0324` edge `1.2918` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.594` n `135` status `ready` deltaP `26.6435` edge `0.6901` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.2909` n `135` status `ready` deltaP `23.9931` edge `0.763` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.6155` n `135` status `ready` deltaP `32.8356` edge `0.1302` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.2237` n `135` status `ready` deltaP `25.0116` edge `0.2293` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.7949` n `135` status `ready` deltaP `28.7138` edge `0.2016` maxDD `-9.143`
- `market_context_high->fx_4h` score `2.5252` n `31` status `ready` deltaP `29.1748` edge `0.029` maxDD `-0.0449`
- `market_context_high->crypto_alt_1h` score `1.9916` n `43` status `ready` deltaP `11.8925` edge `0.153` maxDD `-3.6387`
- `news_risk_high->crypto_alt_4h` score `1.6371` n `135` status `ready` deltaP `10.1976` edge `0.3344` maxDD `-15.9436`
- `market_context_high->crypto_major_4h` score `1.5794` n `31` status `ready` deltaP `1.2834` edge `0.1934` maxDD `-3.294`
- `market_context_high->crypto_major_1h` score `1.4211` n `43` status `ready` deltaP `9.2571` edge `0.1177` maxDD `-3.546`
- `news_risk_high->crypto_alt_1h` score `1.0418` n `135` status `ready` deltaP `9.1018` edge `0.1172` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.9492` n `43` status `ready` deltaP `14.6567` edge `0.0078` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8948` n `135` status `ready` deltaP `9.2515` edge `0.0752` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.6059` n `43` status `ready` deltaP `9.7166` edge `0.0596` maxDD `-2.4027`
- `news_risk_high->index_1h` score `0.4814` n `135` status `ready` deltaP `8.6682` edge `0.0111` maxDD `-0.302`
- `market_context_high->metal_1h` score `0.1447` n `43` status `ready` deltaP `4.3065` edge `0.0161` maxDD `-0.4338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
