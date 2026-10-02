# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T18:07:38.042959+00:00`
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

- `market_context_high->unknown_1h` score `359.041` n `50` status `ready` deltaP `10.8743` edge `29.8525` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.5879` n `50` status `ready` deltaP `10.5183` edge `24.3122` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.6204` n `73` status `ready` deltaP `39.795` edge `1.0573` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.2951` n `50` status `ready` deltaP `16.5347` edge `0.8347` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `8.9658` n `50` status `ready` deltaP `31.8264` edge `0.6766` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.9652` n `73` status `ready` deltaP `32.2322` edge `0.5807` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.1413` n `50` status `ready` deltaP `17.5427` edge `0.5485` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.127` n `50` status `ready` deltaP `15.5793` edge `0.4523` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.948` n `116` status `ready` deltaP `21.4414` edge `0.4038` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.1006` n `50` status `ready` deltaP `14.503` edge `0.228` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.0348` n `50` status `ready` deltaP `14.2994` edge `0.2026` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7653` n `50` status `ready` deltaP `30.8598` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4591` n `116` status `ready` deltaP `22.0984` edge `0.1272` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.654` n `50` status `ready` deltaP `8.4514` edge `0.3419` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.4926` n `73` status `ready` deltaP `5.9908` edge `0.4668` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.41` n `50` status `ready` deltaP `19.8922` edge `0.0113` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3371` n `73` status `ready` deltaP `13.009` edge `0.2121` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.2113` n `116` status `ready` deltaP `14.1979` edge `0.2916` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.9532` n `116` status `ready` deltaP `5.3996` edge `0.0995` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.77` n `50` status `ready` deltaP `16.8611` edge `0.0881` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
