# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T01:07:29.791219+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->fx_24h` score `1.1145` n `145` status `ready` deltaP `20.4064` edge `0.0376` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9084` n `169` status `ready` deltaP `11.9939` edge `0.0672` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6056` n `180` status `ready` deltaP `8.4997` edge `0.0281` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0625` n `169` status `ready` deltaP `6.7587` edge `0.0069` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0973` n `180` status `ready` deltaP `4.9335` edge `-0.0002` maxDD `-0.613`
- `market_context_high->metal_1h` score `-1.2948` n `180` status `ready` deltaP `-5.2195` edge `-0.0095` maxDD `-2.0884`
- `market_context_high->index_1h` score `-1.3398` n `180` status `ready` deltaP `-7.0758` edge `-0.0057` maxDD `-1.0359`
- `market_context_high->equity_1h` score `-1.4707` n `180` status `ready` deltaP `-6.0545` edge `-0.0205` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.581` n `145` status `ready` deltaP `2.5482` edge `-0.0163` maxDD `-2.9283`
- `market_context_high->index_24h` score `-1.8198` n `145` status `ready` deltaP `-7.5587` edge `0.0182` maxDD `-6.7558`
- `market_context_high->index_4h` score `-1.942` n `169` status `ready` deltaP `-7.8276` edge `-0.0192` maxDD `-1.5693`
- `market_context_high->crypto_alt_1h` score `-2.7652` n `180` status `ready` deltaP `-10.326` edge `-0.043` maxDD `-6.4874`
- `market_context_high->metal_4h` score `-3.2644` n `169` status `ready` deltaP `-8.2868` edge `-0.0404` maxDD `-6.1111`
- `market_context_high->commodity_24h` score `-3.6854` n `145` status `ready` deltaP `5.1945` edge `0.0277` maxDD `-31.7855`
- `market_context_high->crypto_major_1h` score `-3.8264` n `180` status `ready` deltaP `-10.642` edge `-0.0575` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.5617` n `169` status `ready` deltaP `-17.3131` edge `-0.1585` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-5.8655` n `145` status `ready` deltaP `-10.144` edge `-0.1648` maxDD `-30.5644`
- `market_context_high->crypto_alt_4h` score `-7.1098` n `169` status `ready` deltaP `-14.9823` edge `-0.1578` maxDD `-20.1177`
- `market_context_high->equity_24h` score `-7.8074` n `145` status `ready` deltaP `-7.4033` edge `-0.1815` maxDD `-48.274`
- `market_context_high->unknown_24h` score `-7.9931` n `145` status `ready` deltaP `-14.5772` edge `-0.3235` maxDD `-9.6329`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
