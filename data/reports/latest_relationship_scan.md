# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T05:22:29.905533+00:00`
- Price records: `672`
- Market context records: `5321`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9648`

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

- `market_context_high->unknown_24h` score `19.0269` n `153` status `ready` deltaP `22.8247` edge `1.4424` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.0251` n `153` status `ready` deltaP `24.6937` edge `0.8358` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.0949` n `153` status `ready` deltaP `18.9236` edge `0.8613` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.0245` n `194` status `ready` deltaP `11.8839` edge `0.3369` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.0029` n `194` status `ready` deltaP `13.1836` edge `0.3916` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.1912` n `194` status `ready` deltaP `11.7692` edge `0.268` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5434` n `194` status `ready` deltaP `8.6117` edge `0.0844` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.5133` n `153` status `ready` deltaP `13.3068` edge `0.0436` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.5072` n `153` status `ready` deltaP `22.0384` edge `0.0816` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.0626` n `194` status `ready` deltaP `2.3952` edge `0.0854` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.037` n `194` status `ready` deltaP `6.218` edge `0.012` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0047` n `194` status `ready` deltaP `4.6407` edge `0.094` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.2867` n `194` status `ready` deltaP `2.994` edge `0.0108` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3368` n `194` status `ready` deltaP `0.8643` edge `0.0` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4236` n `194` status `ready` deltaP `5.4595` edge `0.0252` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6019` n `194` status `ready` deltaP `3.2027` edge `0.0044` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.0313` n `194` status `ready` deltaP `9.5848` edge `-0.0316` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4084` n `194` status `ready` deltaP `-2.8767` edge `-0.0064` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.27` n `194` status `ready` deltaP `-5.3951` edge `-0.0026` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.25` n `153` status `ready` deltaP `12.8268` edge `0.3388` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
