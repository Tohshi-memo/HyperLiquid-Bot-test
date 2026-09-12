# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T05:22:29.268147+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11385`

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

- `market_context_high->unknown_24h` score `1263.3776` n `134` status `ready` deltaP `13.9589` edge `105.1936` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.4097` n `82` status `ready` deltaP `-3.6038` edge `32.017` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `23.8466` n `59` status `ready` deltaP `54.505` edge `1.7139` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `23.4785` n `82` status `ready` deltaP `42.5135` edge `1.6961` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.4785` n `82` status `ready` deltaP `42.5135` edge `1.6961` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.7704` n `134` status `ready` deltaP `36.6708` edge `1.4858` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.3758` n `59` status `ready` deltaP `29.967` edge `1.297` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.097` n `59` status `ready` deltaP `33.5894` edge `0.794` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0423` n `82` status `ready` deltaP `36.9792` edge `0.507` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0423` n `82` status `ready` deltaP `36.9792` edge `0.507` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7231` n `134` status `ready` deltaP `36.9792` edge `0.4804` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.2618` n `82` status `ready` deltaP `43.5976` edge `0.435` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.2618` n `82` status `ready` deltaP `43.5976` edge `0.435` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1609` n `59` status `ready` deltaP `51.0417` edge `0.3398` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9381` n `59` status `ready` deltaP `51.4713` edge `0.3277` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.2154` n `82` status `ready` deltaP `30.1829` edge `0.4026` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.2154` n `82` status `ready` deltaP `30.1829` edge `0.4026` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.1088` n `82` status `ready` deltaP `21.0408` edge `1.0497` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.1088` n `82` status `ready` deltaP `21.0408` edge `1.0497` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.171` n `82` status `ready` deltaP `51.2026` edge `0.0938` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
