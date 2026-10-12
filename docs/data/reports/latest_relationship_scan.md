# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T11:07:27.065892+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_major_24h` score `23.9826` n `42` status `ready` deltaP `35.3919` edge `1.861` maxDD `-4.5384`
- `market_context_high->crypto_alt_24h` score `23.7789` n `42` status `ready` deltaP `23.7599` edge `1.9566` maxDD `-7.3403`
- `market_context_high->unknown_4h` score `12.1316` n `109` status `ready` deltaP `-3.8698` edge `1.1014` maxDD `-1.8373`
- `risk_on_high->crypto_alt_4h` score `3.8076` n `48` status `ready` deltaP `18.1911` edge `0.2408` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.8076` n `48` status `ready` deltaP `18.1911` edge `0.2408` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4457` n `48` status `ready` deltaP `32.6728` edge `0.3092` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4457` n `48` status `ready` deltaP `32.6728` edge `0.3092` maxDD `-4.1548`
- `market_context_high->unknown_1h` score `3.3225` n `109` status `ready` deltaP `-3.6436` edge `0.3348` maxDD `-1.024`
- `market_context_high->equity_24h` score `2.404` n `42` status `ready` deltaP `-0.0744` edge `0.449` maxDD `-7.5571`
- `market_context_high->crypto_major_4h` score `2.0287` n `109` status `ready` deltaP `14.0566` edge `0.2604` maxDD `-9.1372`
- `market_context_high->metal_24h` score `1.7689` n `42` status `ready` deltaP `19.0724` edge `0.0743` maxDD `-1.3233`
- `market_context_high->index_24h` score `1.6299` n `42` status `ready` deltaP `23.6111` edge `0.1076` maxDD `-0.4833`
- `market_context_high->crypto_alt_4h` score `1.3807` n `109` status `ready` deltaP `7.6597` edge `0.2679` maxDD `-11.9789`
- `market_context_high->crypto_alt_1h` score `1.1738` n `109` status `ready` deltaP `9.6907` edge `0.1283` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.8076` n `48` status `ready` deltaP `5.6387` edge `0.0894` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8076` n `48` status `ready` deltaP `5.6387` edge `0.0894` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.4235` n `109` status `ready` deltaP `3.5104` edge `0.0882` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.3197` n `48` status `ready` deltaP `4.4661` edge `0.0765` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3197` n `48` status `ready` deltaP `4.4661` edge `0.0765` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.1143` n `109` status `ready` deltaP `2.4625` edge `0.002` maxDD `-0.3122`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
