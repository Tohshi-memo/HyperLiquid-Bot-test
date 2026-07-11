# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T07:52:26.069753+00:00`
- Price records: `672`
- Market context records: `6370`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11118`

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

- `news_risk_high->crypto_alt_24h` score `14.5095` n `32` status `ready` deltaP `39.2361` edge `0.9623` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3136` n `32` status `ready` deltaP `52.4306` edge `0.1766` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3511` n `32` status `ready` deltaP `17.5347` edge `0.5189` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.0307` n `32` status `ready` deltaP `34.8958` edge `0.1238` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9998` n `32` status `ready` deltaP `41.3872` edge `0.062` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3859` n `32` status `ready` deltaP `28.7425` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5442` n `32` status `ready` deltaP `15.0262` edge `0.1445` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.919` n `32` status `ready` deltaP `11.4708` edge `0.0875` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4983` n `214` status `ready` deltaP `15.2752` edge `0.0417` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2535` n `220` status `ready` deltaP `-6.6249` edge `0.1661` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.151` n `214` status `ready` deltaP `8.7631` edge `0.0218` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.3484` n `32` status `ready` deltaP `5.9319` edge `-0.0341` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.4028` n `220` status `ready` deltaP `3.5139` edge `0.0027` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.5148` n `135` status `ready` deltaP `16.551` edge `0.0805` maxDD `-11.8809`
- `market_context_high->commodity_24h` score `-0.6172` n `135` status `ready` deltaP `-4.294` edge `0.1359` maxDD `-6.2457`
- `market_context_high->index_1h` score `-0.6401` n `220` status `ready` deltaP `-1.9515` edge `0.0029` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6502` n `220` status `ready` deltaP `0.1061` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7091` n `32` status `ready` deltaP `-2.3952` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.719` n `32` status `ready` deltaP `0.5208` edge `-0.0085` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.9179` n `214` status `ready` deltaP `6.7643` edge `0.0483` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
