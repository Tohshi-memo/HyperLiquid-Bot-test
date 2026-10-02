# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T22:22:31.603724+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4790`

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

- `market_context_high->unknown_1h` score `364.0546` n `50` status `ready` deltaP `10.7246` edge `30.2713` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.4791` n `50` status `ready` deltaP `10.5183` edge `24.2198` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.8099` n `73` status `ready` deltaP `42.5728` edge `1.1379` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.4845` n `50` status `ready` deltaP `19.3125` edge `0.9153` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0894` n `50` status `ready` deltaP `31.8264` edge `0.6869` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.5436` n `73` status `ready` deltaP `30.3225` edge `0.5583` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.9518` n `50` status `ready` deltaP `19.8293` edge `0.6008` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.4537` n `50` status `ready` deltaP `18.0183` edge `0.5466` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `6.2747` n `116` status `ready` deltaP `23.8804` edge `0.4981` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3957` n `50` status `ready` deltaP `15.4012` edge `0.2466` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1811` n `50` status `ready` deltaP `14.5988` edge `0.2128` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7519` n `50` status `ready` deltaP `30.7073` edge `0.0381` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4367` n `116` status `ready` deltaP `21.4886` edge `0.1294` maxDD `-2.9013`
- `news_risk_high->crypto_major_4h` score `1.7381` n `116` status `ready` deltaP `16.4845` edge `0.3439` maxDD `-10.477`
- `news_risk_high->crypto_major_24h` score `1.5729` n `73` status `ready` deltaP `5.9908` edge `0.4771` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3839` n `73` status `ready` deltaP `13.009` edge `0.2181` maxDD `-2.192`
- `market_context_high->equity_24h` score `1.3799` n `50` status `ready` deltaP `6.5417` edge `0.3195` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.2482` n `116` status `ready` deltaP `6.2978` edge `0.1181` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.9585` n `50` status `ready` deltaP `19.8125` edge `0.0926` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
