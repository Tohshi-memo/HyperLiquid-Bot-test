# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T08:52:27.241142+00:00`
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

- `market_context_high->equity_24h` score `9.044` n `32` status `ready` deltaP `16.4931` edge `0.881` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4221` n `32` status `ready` deltaP `7.8125` edge `0.2085` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3537` n `32` status `ready` deltaP `16.6667` edge `0.1087` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8097` n `32` status `ready` deltaP `11.8056` edge `-0.0024` maxDD `-0.0397`
- `market_context_high->metal_4h` score `-0.2417` n `79` status `ready` deltaP `4.3377` edge `0.0305` maxDD `-2.8988`
- `market_context_high->metal_1h` score `-0.2718` n `88` status `ready` deltaP `4.6952` edge `0.0137` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4564` n `88` status `ready` deltaP `1.0411` edge `0.0028` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.5686` n `79` status `ready` deltaP `-1.561` edge `0.0298` maxDD `-3.7162`
- `market_context_high->index_4h` score `-0.6309` n `79` status `ready` deltaP `4.7816` edge `0.0084` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.8515` n `88` status `ready` deltaP `-5.2599` edge `0.009` maxDD `-0.9814`
- `market_context_high->equity_1h` score `-1.194` n `88` status `ready` deltaP `-5.4096` edge `0.0666` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.3047` n `88` status `ready` deltaP `-13.9085` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.6973` n `88` status `ready` deltaP `1.9801` edge `-0.0329` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.8576` n `32` status `ready` deltaP `-2.2569` edge `-0.1678` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.5166` n `79` status `ready` deltaP `-13.4571` edge `-0.0148` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0248` n `88` status `ready` deltaP `-4.0623` edge `-0.0984` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.2166` n `32` status `ready` deltaP `-4.8611` edge `0.0453` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.7935` n `79` status `ready` deltaP `2.5683` edge `-0.0386` maxDD `-24.9053`
- `market_context_high->crypto_alt_24h` score `-9.169` n `32` status `ready` deltaP `-18.75` edge `-0.1812` maxDD `-29.9639`
- `market_context_high->crypto_alt_4h` score `-9.3129` n `79` status `ready` deltaP `-0.6985` edge `-0.2596` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
