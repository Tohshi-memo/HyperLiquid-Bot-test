# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T21:37:30.691113+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4886`

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

- `market_context_high->unknown_1h` score `363.9995` n `50` status `ready` deltaP `10.4251` edge `30.2687` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.4931` n `50` status `ready` deltaP `10.2134` edge `24.223` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.6254` n `73` status `ready` deltaP `42.052` edge `1.126` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.3001` n `50` status `ready` deltaP `18.7917` edge `0.9034` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0714` n `50` status `ready` deltaP `31.8264` edge `0.6854` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.6357` n `73` status `ready` deltaP `30.8433` edge `0.5625` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.8277` n `50` status `ready` deltaP `19.372` edge `0.5935` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.2779` n `50` status `ready` deltaP `17.561` edge `0.535` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `6.0989` n `116` status `ready` deltaP `23.4231` edge `0.4865` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3609` n `50` status `ready` deltaP `15.4012` edge `0.2437` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1571` n `50` status `ready` deltaP `14.5988` edge `0.2108` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7263` n `50` status `ready` deltaP `30.4024` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4719` n `116` status `ready` deltaP `21.7935` edge `0.1303` maxDD `-2.9013`
- `news_risk_high->crypto_major_4h` score `1.6574` n `116` status `ready` deltaP `16.0272` edge `0.3366` maxDD `-10.477`
- `news_risk_high->crypto_major_24h` score `1.5612` n `73` status `ready` deltaP `5.9908` edge `0.4756` maxDD `-15.8971`
- `market_context_high->equity_24h` score `1.4398` n `50` status `ready` deltaP `7.0625` edge `0.3237` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.434` n `50` status `ready` deltaP `20.1916` edge `0.0113` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3761` n `73` status `ready` deltaP `13.009` edge `0.2171` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.2134` n `116` status `ready` deltaP `6.2978` edge `0.1152` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.9244` n `50` status `ready` deltaP `19.2917` edge `0.0917` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
