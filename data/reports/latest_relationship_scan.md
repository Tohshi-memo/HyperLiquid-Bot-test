# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T16:52:24.014964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11276`

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

- `news_risk_high->unknown_24h` score `38.9561` n `63` status `ready` deltaP `9.0774` edge `3.2832` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `18.3635` n `63` status `ready` deltaP `30.7292` edge `1.663` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `9.8291` n `104` status `ready` deltaP `20.4327` edge `0.7561` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2128` n `77` status `ready` deltaP `10.6114` edge `0.506` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6366` n `104` status `ready` deltaP `33.7206` edge `0.2635` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7178` n `77` status `ready` deltaP `4.5572` edge `0.2318` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.572` n `124` status `ready` deltaP `18.8435` edge `0.1319` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `1.6292` n `77` status `ready` deltaP `36.2271` edge `0.0223` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.0299` n `36` status `ready` deltaP `14.7206` edge `0.0091` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.0299` n `36` status `ready` deltaP `14.7206` edge `0.0091` maxDD `-0.0463`
- `risk_on_high->crypto_alt_1h` score `0.9485` n `36` status `ready` deltaP `17.0492` edge `0.0555` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.9485` n `36` status `ready` deltaP `17.0492` edge `0.0555` maxDD `-2.1381`
- `market_context_high->unknown_1h` score `0.7945` n `136` status `ready` deltaP `8.1763` edge `0.0598` maxDD `-1.5148`
- `news_risk_high->equity_24h` score `0.6874` n `63` status `ready` deltaP `16.8155` edge `0.2669` maxDD `-18.9364`
- `news_risk_high->fx_1h` score `0.6811` n `77` status `ready` deltaP `13.5314` edge `0.0054` maxDD `-0.108`
- `market_context_high->crypto_major_4h` score `0.5823` n `124` status `ready` deltaP `20.2498` edge `0.2586` maxDD `-20.9394`
- `news_risk_high->commodity_1h` score `0.3407` n `77` status `ready` deltaP `10.7396` edge `0.0041` maxDD `-0.5618`
- `market_context_high->crypto_alt_4h` score `0.1815` n `124` status `ready` deltaP `22.5364` edge `0.3495` maxDD `-31.4361`
- `news_risk_high->metal_24h` score `0.0184` n `63` status `ready` deltaP `25.9673` edge `-0.0044` maxDD `-7.9756`
- `news_risk_high->index_24h` score `-0.0414` n `63` status `ready` deltaP `11.2848` edge `0.0057` maxDD `-2.2325`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
