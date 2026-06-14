# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T15:37:32.424117+00:00`
- Price records: `672`
- Market context records: `3905`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `46.9783` n `72` status `ready` deltaP `4.3699` edge `6.2079` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `46.9783` n `72` status `ready` deltaP `4.3699` edge `6.2079` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `26.0464` n `38` status `ready` deltaP `20.815` edge `2.1308` maxDD `-5.5891`
- `risk_on_and_context->crypto_major_24h` score `26.0464` n `38` status `ready` deltaP `20.815` edge `2.1308` maxDD `-5.5891`
- `risk_on_high->equity_24h` score `23.7719` n `38` status `ready` deltaP `42.0139` edge `1.7009` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.7719` n `38` status `ready` deltaP `42.0139` edge `1.7009` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `14.4033` n `38` status `ready` deltaP `18.7317` edge `1.228` maxDD `-9.8751`
- `risk_on_and_context->crypto_alt_24h` score `14.4033` n `38` status `ready` deltaP `18.7317` edge `1.228` maxDD `-9.8751`
- `risk_on_high->index_24h` score `9.802` n `38` status `ready` deltaP `30.0347` edge `0.6166` maxDD `0.0`
- `risk_on_and_context->index_24h` score `9.802` n `38` status `ready` deltaP `30.0347` edge `0.6166` maxDD `0.0`
- `market_context_high->equity_24h` score `6.5076` n `165` status `ready` deltaP `20.8018` edge `0.7066` maxDD `-14.5715`
- `market_context_high->unknown_4h` score `6.2234` n `210` status `ready` deltaP `-2.0586` edge `1.3525` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `5.7748` n `72` status `ready` deltaP `20.5284` edge `0.4566` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.7748` n `72` status `ready` deltaP `20.5284` edge `0.4566` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.7964` n `165` status `ready` deltaP `25.7923` edge `0.3417` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.9907` n `165` status `ready` deltaP `20.1894` edge `0.2578` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5965` n `72` status `ready` deltaP `24.9492` edge `0.1635` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5965` n `72` status `ready` deltaP `24.9492` edge `0.1635` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.5888` n `210` status `ready` deltaP `16.3618` edge `0.2831` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `1.7751` n `165` status `ready` deltaP `3.4785` edge `0.5711` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
