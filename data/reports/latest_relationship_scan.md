# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T05:52:27.816185+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8814`

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

- `market_context_high->equity_24h` score `9.9536` n `32` status `ready` deltaP `16.4931` edge `0.9568` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.5452` n `32` status `ready` deltaP `7.9861` edge `0.2176` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3943` n `32` status `ready` deltaP `16.6667` edge `0.1139` maxDD `-2.3671`
- `market_context_high->commodity_4h` score `0.9399` n `67` status `ready` deltaP `6.6208` edge `0.0814` maxDD `-1.1102`
- `market_context_high->metal_4h` score `0.9269` n `67` status `ready` deltaP `13.4806` edge `0.0815` maxDD `-1.2025`
- `market_context_high->metal_1h` score `0.7998` n `79` status `ready` deltaP `10.4601` edge `0.0297` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.6892` n `32` status `ready` deltaP `10.7639` edge `-0.0055` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.2892` n `67` status `ready` deltaP `14.2996` edge `0.0346` maxDD `-2.4279`
- `market_context_high->equity_1h` score `0.013` n `79` status `ready` deltaP `-0.6197` edge `0.1255` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `-0.0454` n `79` status `ready` deltaP `5.9691` edge `0.0152` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.3453` n `79` status `ready` deltaP `-0.47` edge `0.0172` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.9211` n `79` status `ready` deltaP `7.4376` edge `0.0216` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.0803` n `79` status `ready` deltaP `-14.0529` edge `-0.0045` maxDD `-0.5586`
- `market_context_high->equity_4h` score `-1.3369` n `67` status `ready` deltaP `10.648` edge `0.1356` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.6424` n `32` status `ready` deltaP `-0.1736` edge `-0.1541` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-1.939` n `67` status `ready` deltaP `-10.7117` edge `-0.0094` maxDD `-1.7556`
- `market_context_high->crypto_major_1h` score `-2.061` n `79` status `ready` deltaP `0.5779` edge `-0.0582` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.6438` n `32` status `ready` deltaP `-4.8611` edge `0.0097` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.6189` n `67` status `ready` deltaP `6.3297` edge `-0.1269` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.163` n `32` status `ready` deltaP `-18.75` edge `-0.1807` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
