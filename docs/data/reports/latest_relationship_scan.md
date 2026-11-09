# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T08:37:27.902683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9328`

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

- `market_context_high->equity_24h` score `9.1172` n `32` status `ready` deltaP `16.4931` edge `0.8871` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4281` n `32` status `ready` deltaP `7.8125` edge `0.209` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3569` n `32` status `ready` deltaP `16.6667` edge `0.1091` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8085` n `32` status `ready` deltaP `11.8056` edge `-0.0025` maxDD `-0.0397`
- `market_context_high->metal_4h` score `-0.1207` n `78` status `ready` deltaP `5.0031` edge `0.0343` maxDD `-2.6502`
- `market_context_high->metal_1h` score `-0.2694` n `88` status `ready` deltaP `4.6952` edge `0.0139` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.4304` n `78` status `ready` deltaP `-0.8794` edge `0.0342` maxDD `-3.3476`
- `market_context_high->commodity_1h` score `-0.4463` n `88` status `ready` deltaP `1.1908` edge `0.0031` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5703` n `78` status `ready` deltaP `5.3432` edge `0.0097` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.8499` n `88` status `ready` deltaP `-5.2599` edge `0.0092` maxDD `-0.9814`
- `market_context_high->equity_1h` score `-1.1831` n `88` status `ready` deltaP `-5.4096` edge `0.068` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.3039` n `88` status `ready` deltaP `-13.9085` edge `-0.006` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.6817` n `88` status `ready` deltaP `1.9801` edge `-0.0309` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.8392` n `32` status `ready` deltaP `-2.0833` edge `-0.1666` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.5594` n `78` status `ready` deltaP `-14.2198` edge `-0.0152` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0178` n `88` status `ready` deltaP `-4.0623` edge `-0.0975` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.255` n `32` status `ready` deltaP `-4.8611` edge `0.0421` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.6759` n `78` status `ready` deltaP `3.0488` edge `-0.032` maxDD `-24.9053`
- `market_context_high->crypto_alt_24h` score `-9.1654` n `32` status `ready` deltaP `-18.75` edge `-0.1809` maxDD `-29.9639`
- `market_context_high->crypto_alt_4h` score `-9.2388` n `78` status `ready` deltaP `-0.1954` edge `-0.2609` maxDD `-33.9494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
