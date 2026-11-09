# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T09:07:27.823228+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9208`

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

- `market_context_high->equity_24h` score `8.9672` n `32` status `ready` deltaP `16.4931` edge `0.8746` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4161` n `32` status `ready` deltaP `7.8125` edge `0.208` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3498` n `32` status `ready` deltaP `16.6667` edge `0.1082` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.826` n `32` status `ready` deltaP `11.9792` edge `-0.0022` maxDD `-0.0397`
- `market_context_high->metal_1h` score `-0.285` n `88` status `ready` deltaP `4.5455` edge `0.0136` maxDD `-1.4122`
- `market_context_high->metal_4h` score `-0.349` n `80` status `ready` deltaP `3.689` edge `0.0276` maxDD `-3.0886`
- `market_context_high->commodity_1h` score `-0.4657` n `88` status `ready` deltaP `0.8914` edge `0.0026` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6899` n `80` status `ready` deltaP `-2.2256` edge `0.0265` maxDD `-4.0093`
- `market_context_high->index_4h` score `-0.6938` n `80` status `ready` deltaP `4.0854` edge `0.0078` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.8531` n `88` status `ready` deltaP `-5.2599` edge `0.0088` maxDD `-0.9814`
- `market_context_high->equity_1h` score `-1.2034` n `88` status `ready` deltaP `-5.4096` edge `0.0654` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.3047` n `88` status `ready` deltaP `-13.9085` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.716` n `88` status `ready` deltaP `1.9801` edge `-0.0353` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.8768` n `32` status `ready` deltaP `-2.4306` edge `-0.1691` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.4733` n `80` status `ready` deltaP `-12.7134` edge `-0.0142` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0365` n `88` status `ready` deltaP `-4.0623` edge `-0.0999` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.189` n `32` status `ready` deltaP `-4.8611` edge `0.0476` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.8705` n `80` status `ready` deltaP `1.9512` edge `-0.0409` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-9.1827` n `80` status `ready` deltaP `-0.0915` edge `-0.2528` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-9.187` n `32` status `ready` deltaP `-18.75` edge `-0.1827` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
