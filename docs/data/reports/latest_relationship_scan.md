# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-29T00:07:27.642125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7822`

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

- `market_context_high->fx_1h` score `0.7895` n `72` status `ready` deltaP `12.9491` edge `0.0016` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.3642` n `72` status `ready` deltaP `9.231` edge `0.0084` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2043` n `72` status `ready` deltaP `6.7947` edge `0.004` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0732` n `72` status `ready` deltaP `2.6281` edge `0.0077` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2399` n `72` status `ready` deltaP `5.6387` edge `-0.0081` maxDD `-2.1532`
- `market_context_high->index_1h` score `-0.4543` n `72` status `ready` deltaP `-0.8982` edge `-0.0029` maxDD `-0.2813`
- `market_context_high->metal_4h` score `-0.4811` n `72` status `ready` deltaP `3.7094` edge `0.0074` maxDD `-0.4441`
- `market_context_high->crypto_major_1h` score `-1.2376` n `72` status `ready` deltaP `-4.6158` edge `-0.0004` maxDD `-7.5329`
- `market_context_high->commodity_4h` score `-2.2629` n `72` status `ready` deltaP `-20.0881` edge `0.0016` maxDD `-2.9572`
- `market_context_high->equity_4h` score `-3.5457` n `72` status `ready` deltaP `-14.956` edge `-0.1512` maxDD `-6.9605`
- `market_context_high->index_4h` score `-4.0101` n `72` status `ready` deltaP `-20.8164` edge `-0.0206` maxDD `-0.984`
- `market_context_high->crypto_alt_1h` score `-4.4138` n `72` status `ready` deltaP `-9.506` edge `-0.1091` maxDD `-11.9607`
- `market_context_high->crypto_major_4h` score `-9.1375` n `72` status `ready` deltaP `-8.7229` edge `-0.2528` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-19.2872` n `72` status `ready` deltaP `-31.0637` edge `-0.6407` maxDD `-49.4247`
- `market_context_high->unknown_4h` score `-570.4144` n `72` status `ready` deltaP `3.3198` edge `-47.55` maxDD `-0.2001`
- `market_context_high->unknown_1h` score `-1280.8459` n `72` status `ready` deltaP `1.4388` edge `-106.7351` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2898.5105` n `23` status `thin_sample` deltaP `8.3832` edge `314.9996` maxDD `0.0`
- `news_risk_high->unknown_4h` score `203.6949` n `23` status `thin_sample` deltaP `6.0976` edge `22.1001` maxDD `0.0`
- `risk_on_high->unknown_4h` score `28.7783` n `2` status `thin_sample` deltaP `6.0976` edge `35.9322` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `28.7783` n `2` status `thin_sample` deltaP `6.0976` edge `35.9322` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
