# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T19:22:26.844370+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12779`

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

- `market_context_high->unknown_24h` score `9708.4899` n `78` status `ready` deltaP `12.8873` edge `808.9601` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `7661.1565` n `38` status `ready` deltaP `15.4514` edge `638.3267` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `7661.1565` n `38` status `ready` deltaP `15.4514` edge `638.3267` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.4615` n `82` status `ready` deltaP `-5.2505` edge `32.0323` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.6512` n `69` status `ready` deltaP `45.8031` edge `1.5352` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.17` n `69` status `ready` deltaP `29.8837` edge `1.2804` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `15.6743` n `38` status `ready` deltaP `37.0157` edge `1.0824` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.6743` n `38` status `ready` deltaP `37.0157` edge `1.0824` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.8696` n `78` status `ready` deltaP `29.6608` edge `1.0408` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.9467` n `38` status `ready` deltaP `42.0139` edge `0.5488` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.9467` n `38` status `ready` deltaP `42.0139` edge `0.5488` maxDD `0.0`
- `market_context_high->equity_24h` score `9.5519` n `78` status `ready` deltaP `42.0139` edge `0.5159` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.2605` n `69` status `ready` deltaP `24.6226` edge `0.6883` maxDD `-3.1258`
- `risk_on_high->crypto_alt_4h` score `7.1219` n `47` status `ready` deltaP `34.0393` edge `0.4079` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.1219` n `47` status `ready` deltaP `34.0393` edge `0.4079` maxDD `-1.9733`
- `news_risk_high->index_24h` score `6.6973` n `69` status `ready` deltaP `43.9009` edge `0.2831` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.3997` n `69` status `ready` deltaP `40.6023` edge `0.3067` maxDD `-0.526`
- `risk_on_high->index_24h` score `4.916` n `38` status `ready` deltaP `49.0497` edge `0.0869` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.916` n `38` status `ready` deltaP `49.0497` edge `0.0869` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.2349` n `78` status `ready` deltaP `35.1495` edge `0.0746` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
