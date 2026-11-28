# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T22:52:24.403981+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7512`

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

- `market_context_high->fx_1h` score `0.8506` n `72` status `ready` deltaP `13.6976` edge `0.0017` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.4709` n `71` status `ready` deltaP `10.4904` edge `0.0089` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.1911` n `72` status `ready` deltaP `6.645` edge `0.0039` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0646` n `72` status `ready` deltaP `2.7778` edge `0.0078` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2422` n `72` status `ready` deltaP `5.6387` edge `-0.0084` maxDD `-2.1532`
- `market_context_high->metal_4h` score `-0.2988` n `71` status `ready` deltaP `3.826` edge `0.0084` maxDD `-0.4441`
- `market_context_high->index_1h` score `-0.4628` n `72` status `ready` deltaP `-1.0479` edge `-0.003` maxDD `-0.2813`
- `market_context_high->crypto_major_1h` score `-1.2384` n `72` status `ready` deltaP `-4.6158` edge `-0.0005` maxDD `-7.5329`
- `market_context_high->commodity_4h` score `-2.2801` n `71` status `ready` deltaP `-20.3431` edge `0.0011` maxDD `-2.9572`
- `market_context_high->equity_4h` score `-3.5381` n `71` status `ready` deltaP `-15.0936` edge `-0.1493` maxDD `-6.9605`
- `market_context_high->index_4h` score `-4.0238` n `71` status `ready` deltaP `-21.0323` edge `-0.0203` maxDD `-0.984`
- `market_context_high->crypto_alt_1h` score `-4.3946` n `72` status `ready` deltaP `-9.3563` edge `-0.1085` maxDD `-11.9607`
- `market_context_high->crypto_major_4h` score `-9.0936` n `71` status `ready` deltaP `-8.8801` edge `-0.2481` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-19.3313` n `71` status `ready` deltaP `-31.4948` edge `-0.6415` maxDD `-49.4247`
- `market_context_high->unknown_4h` score `-571.9561` n `71` status `ready` deltaP `4.5366` edge `-47.6883` maxDD `-0.063`
- `market_context_high->unknown_1h` score `-1295.3731` n `72` status `ready` deltaP `1.4388` edge `-107.9457` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2916.2469` n `25` status `thin_sample` deltaP `8.3832` edge `291.5688` maxDD `0.0`
- `news_risk_high->unknown_4h` score `241.1483` n `25` status `thin_sample` deltaP `5.9451` edge `24.0752` maxDD `0.0`
- `risk_on_high->unknown_4h` score `27.8908` n `2` status `thin_sample` deltaP `5.9451` edge `34.8239` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `27.8908` n `2` status `thin_sample` deltaP `5.9451` edge `34.8239` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
