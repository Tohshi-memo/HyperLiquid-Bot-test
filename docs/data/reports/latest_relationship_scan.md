# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T06:52:23.760019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8724`

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

- `market_context_high->equity_24h` score `9.6128` n `32` status `ready` deltaP `16.4931` edge `0.9284` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4797` n `32` status `ready` deltaP `7.8125` edge `0.2133` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3764` n `32` status `ready` deltaP `16.6667` edge `0.1116` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.7464` n `32` status `ready` deltaP `11.2847` edge `-0.0042` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.6378` n `71` status `ready` deltaP `10.1855` edge `0.0664` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.6338` n `71` status `ready` deltaP `4.4293` edge `0.0705` maxDD `-1.1102`
- `market_context_high->metal_1h` score `0.4601` n `83` status `ready` deltaP `7.8313` edge `0.0234` maxDD `-0.6481`
- `market_context_high->index_4h` score `0.0352` n `71` status `ready` deltaP `10.5998` edge `0.0267` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.2052` n `83` status `ready` deltaP `3.6397` edge `0.0082` maxDD `-1.7019`
- `market_context_high->equity_1h` score `-0.3407` n `83` status `ready` deltaP `-2.7271` edge `0.1067` maxDD `-5.5762`
- `market_context_high->index_1h` score `-0.4798` n `83` status `ready` deltaP `-2.5774` edge `0.014` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-1.1635` n `83` status `ready` deltaP `4.9365` edge `0.0072` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.3186` n `83` status `ready` deltaP `-15.4949` edge `-0.0063` maxDD `-0.7566`
- `market_context_high->metal_24h` score `-1.7167` n `32` status `ready` deltaP `-0.8681` edge `-0.159` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.2175` n `71` status `ready` deltaP `-12.6245` edge `-0.0121` maxDD `-2.0427`
- `market_context_high->crypto_major_1h` score `-2.3746` n `83` status `ready` deltaP `-1.6792` edge `-0.0707` maxDD `-12.8036`
- `market_context_high->equity_4h` score `-2.9297` n `71` status `ready` deltaP `7.5211` edge `0.0837` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.5574` n `32` status `ready` deltaP `-4.8611` edge `0.0169` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.3423` n `71` status `ready` deltaP `3.723` edge `-0.1698` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.2254` n `32` status `ready` deltaP `-18.75` edge `-0.1859` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
