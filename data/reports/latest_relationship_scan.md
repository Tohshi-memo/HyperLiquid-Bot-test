# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T17:22:31.687203+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4888`

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

- `market_context_high->unknown_1h` score `359.029` n `50` status `ready` deltaP `11.024` edge `29.8505` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.7419` n `50` status `ready` deltaP `10.8232` edge `24.323` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4801` n `73` status `ready` deltaP `39.795` edge `1.0456` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.1547` n `50` status `ready` deltaP `16.5347` edge `0.823` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.0501` n `73` status `ready` deltaP `32.753` edge `0.5843` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9821` n `50` status `ready` deltaP `32.0` edge `0.6768` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.9943` n `50` status `ready` deltaP `17.0854` edge `0.5393` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9656` n `50` status `ready` deltaP `15.122` edge `0.4419` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.7866` n `116` status `ready` deltaP `20.9841` edge `0.3934` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `2.9915` n `50` status `ready` deltaP `14.0539` edge `0.2219` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9616` n `50` status `ready` deltaP `13.8503` edge `0.1995` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7909` n `50` status `ready` deltaP `31.1646` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4291` n `116` status `ready` deltaP `22.0984` edge `0.1247` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.7091` n `50` status `ready` deltaP `8.9722` edge `0.3455` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5032` n `73` status `ready` deltaP `6.1644` edge `0.467` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3164` n `73` status `ready` deltaP `12.8354` edge `0.2106` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.1157` n `116` status `ready` deltaP `13.7406` edge `0.2824` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.844` n `116` status `ready` deltaP `4.9505` edge `0.0934` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.739` n `50` status `ready` deltaP `16.3403` edge `0.0876` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
