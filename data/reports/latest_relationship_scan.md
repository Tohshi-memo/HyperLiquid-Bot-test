# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T15:37:34.699925+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4822`

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

- `market_context_high->unknown_1h` score `359.3985` n `50` status `ready` deltaP `11.1737` edge `29.8803` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.585` n `50` status `ready` deltaP `11.128` edge `24.3079` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3288` n `73` status `ready` deltaP `39.795` edge `1.033` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.365` n `73` status `ready` deltaP `33.7947` edge `0.6036` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.1335` n `50` status `ready` deltaP `32.3472` edge `0.6871` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0035` n `50` status `ready` deltaP `16.5347` edge `0.8104` maxDD `-11.6271`
- `market_context_high->crypto_major_4h` score `6.7054` n `50` status `ready` deltaP `16.3232` edge `0.5203` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7052` n `50` status `ready` deltaP `14.2073` edge `0.4263` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.5262` n `116` status `ready` deltaP `20.0694` edge `0.3778` maxDD `-6.4195`
- `market_context_high->crypto_major_1h` score `2.934` n `50` status `ready` deltaP `13.8503` edge `0.1972` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9195` n `50` status `ready` deltaP `13.7545` edge `0.2179` maxDD `-3.6376`
- `market_context_high->fx_4h` score `2.8627` n `50` status `ready` deltaP `31.9268` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4631` n `116` status `ready` deltaP `22.4033` edge `0.1255` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.9138` n `50` status `ready` deltaP `10.0139` edge `0.3648` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.6016` n `73` status `ready` deltaP `6.5116` edge `0.4773` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2855` n `73` status `ready` deltaP `12.6618` edge `0.2078` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.9279` n `116` status `ready` deltaP `12.9784` edge `0.2634` maxDD `-10.477`
- `market_context_high->index_24h` score `0.7941` n `50` status `ready` deltaP `14.4444` edge `0.0626` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.7721` n `116` status `ready` deltaP `4.6511` edge `0.0894` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
