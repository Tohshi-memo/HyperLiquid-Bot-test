# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T03:22:16.727084+00:00`
- Price records: `672`
- Market context records: `2003`
- Flow alert records: `7658`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7593`

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

- `market_context_high->crypto_major_4h` score `8.7508` n `216` status `ready` deltaP `30.4991` edge `0.5789` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.1665` n `216` status `ready` deltaP `24.1362` edge `0.6341` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.4822` n `216` status `ready` deltaP `18.4451` edge `0.4088` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.6294` n `216` status `ready` deltaP `15.4754` edge `0.2254` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.8739` n `185` status `ready` deltaP `15.6599` edge `0.5838` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.3959` n `216` status `ready` deltaP `11.7515` edge `0.1366` maxDD `-3.2225`
- `market_context_high->metal_24h` score `1.3549` n `185` status `ready` deltaP `16.0062` edge `0.2488` maxDD `-12.7414`
- `market_context_high->crypto_alt_1h` score `1.1207` n `216` status `ready` deltaP `9.5199` edge `0.1413` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.9947` n `216` status `ready` deltaP `9.773` edge `0.0861` maxDD `-1.8022`
- `market_context_high->equity_24h` score `0.9232` n `185` status `ready` deltaP `14.4715` edge `0.4703` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.68` n `185` status `ready` deltaP `16.2643` edge `0.0295` maxDD `-1.5009`
- `market_context_high->index_24h` score `0.0537` n `185` status `ready` deltaP `2.7472` edge `0.109` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0151` n `216` status `ready` deltaP `5.2617` edge `0.0425` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `-0.1364` n `185` status `ready` deltaP `19.6825` edge `0.716` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.5412` n `216` status `ready` deltaP `0.4408` edge `0.011` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.5588` n `216` status `ready` deltaP `-1.3612` edge `0.0002` maxDD `-0.3548`
- `market_context_high->unknown_1h` score `-0.749` n `216` status `ready` deltaP `3.0661` edge `-0.0109` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.7973` n `216` status `ready` deltaP `1.8934` edge `0.0039` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.6333` n `216` status `ready` deltaP `-6.8654` edge `-0.0022` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.7345` n `216` status `ready` deltaP `6.4984` edge `0.0744` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
