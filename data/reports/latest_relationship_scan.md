# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T04:07:19.311936+00:00`
- Price records: `672`
- Market context records: `2006`
- Flow alert records: `7667`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9107`

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

- `market_context_high->crypto_major_4h` score `8.7883` n `213` status `ready` deltaP `30.4885` edge `0.5821` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.2168` n `213` status `ready` deltaP `24.3` edge `0.6372` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.6034` n `213` status `ready` deltaP `18.715` edge `0.4171` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.7063` n `213` status `ready` deltaP `15.8364` edge `0.2294` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.4719` n `185` status `ready` deltaP `15.6599` edge `0.5503` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.4224` n `213` status `ready` deltaP `11.8425` edge `0.1382` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.1006` n `213` status `ready` deltaP `9.2976` edge `0.1411` maxDD `-4.9097`
- `market_context_high->index_4h` score `1.0756` n `213` status `ready` deltaP `10.3794` edge `0.0888` maxDD `-1.8022`
- `market_context_high->metal_24h` score `0.9734` n `185` status `ready` deltaP `14.8982` edge `0.2244` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.6976` n `185` status `ready` deltaP `14.4715` edge `0.4515` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.6401` n `185` status `ready` deltaP `16.2643` edge `0.0289` maxDD `-1.7188`
- `market_context_high->equity_1h` score `-0.0166` n `213` status `ready` deltaP `5.2283` edge `0.0426` maxDD `-2.6402`
- `market_context_high->index_24h` score `-0.0171` n `185` status `ready` deltaP `2.7472` edge `0.1031` maxDD `-4.1604`
- `market_context_high->index_1h` score `-0.5179` n `213` status `ready` deltaP `0.6424` edge `0.0116` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `-0.6499` n `213` status `ready` deltaP `3.4052` edge `-0.0049` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.7609` n `213` status `ready` deltaP `2.3235` edge `0.0057` maxDD `-5.166`
- `market_context_high->crypto_major_24h` score `-0.7854` n `185` status `ready` deltaP `18.5746` edge `0.6693` maxDD `-62.3533`
- `market_context_high->fx_1h` score `-0.8087` n `213` status `ready` deltaP `-0.8132` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.5715` n `213` status `ready` deltaP `-6.1677` edge `-0.0017` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.6479` n `213` status `ready` deltaP `6.9965` edge `0.0783` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
