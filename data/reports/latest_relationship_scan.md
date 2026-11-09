# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T09:22:28.543344+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9226`

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

- `market_context_high->equity_24h` score `8.8952` n `32` status `ready` deltaP `16.4931` edge `0.8686` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4077` n `32` status `ready` deltaP `7.8125` edge `0.2073` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3475` n `32` status `ready` deltaP `16.6667` edge `0.1079` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8423` n `32` status `ready` deltaP `12.1528` edge `-0.002` maxDD `-0.0397`
- `market_context_high->metal_1h` score `-0.2982` n `88` status `ready` deltaP `4.3958` edge `0.0135` maxDD `-1.4122`
- `market_context_high->metal_4h` score `-0.4626` n `81` status `ready` deltaP `3.0563` edge `0.0243` maxDD `-3.3188`
- `market_context_high->commodity_1h` score `-0.4774` n `88` status `ready` deltaP `0.7417` edge `0.0021` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7491` n `81` status `ready` deltaP `3.5588` edge `0.0067` maxDD `-2.4279`
- `market_context_high->commodity_4h` score `-0.7691` n `81` status `ready` deltaP `-2.8737` edge `0.0258` maxDD `-4.0861`
- `market_context_high->index_1h` score `-0.8531` n `88` status `ready` deltaP `-5.2599` edge `0.0088` maxDD `-0.9814`
- `market_context_high->equity_1h` score `-1.2049` n `88` status `ready` deltaP `-5.4096` edge `0.0652` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.3047` n `88` status `ready` deltaP `-13.9085` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.7222` n `88` status `ready` deltaP `1.9801` edge `-0.0361` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.8944` n `32` status `ready` deltaP `-2.6042` edge `-0.1702` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.4325` n `81` status `ready` deltaP `-11.9881` edge `-0.0138` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.038` n `88` status `ready` deltaP `-4.0623` edge `-0.1001` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.159` n `32` status `ready` deltaP `-4.8611` edge `0.0501` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.9533` n `81` status `ready` deltaP `1.5018` edge `-0.0448` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-9.156` n `81` status `ready` deltaP `-0.4328` edge `-0.2483` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-9.2026` n `32` status `ready` deltaP `-18.75` edge `-0.184` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
