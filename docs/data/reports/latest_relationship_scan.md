# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T23:22:35.903381+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.0809` n `145` status `ready` deltaP `20.4064` edge `0.0348` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.768` n `176` status `ready` deltaP `10.8093` edge `0.0634` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.5815` n `180` status `ready` deltaP `8.0938` edge `0.0288` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0466` n `176` status `ready` deltaP `7.3032` edge `0.0074` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0504` n `180` status `ready` deltaP `5.7452` edge `0.0004` maxDD `-0.613`
- `market_context_high->index_24h` score `-1.0878` n `145` status `ready` deltaP `-3.9443` edge `0.0512` maxDD `-6.149`
- `market_context_high->index_4h` score `-1.1818` n `176` status `ready` deltaP `-6.6242` edge `-0.0169` maxDD `-1.5693`
- `market_context_high->index_1h` score `-1.2203` n `180` status `ready` deltaP `-7.0758` edge `-0.0056` maxDD `-0.9135`
- `market_context_high->metal_1h` score `-1.2552` n `180` status `ready` deltaP `-4.8137` edge `-0.0089` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-1.299` n `145` status `ready` deltaP `2.5482` edge `0.0072` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.3207` n `180` status `ready` deltaP `-5.6487` edge `-0.0215` maxDD `-6.4794`
- `market_context_high->crypto_alt_1h` score `-2.9124` n `180` status `ready` deltaP `-11.5436` edge `-0.046` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.0936` n `176` status `ready` deltaP `-6.7212` edge `-0.0366` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.8541` n `180` status `ready` deltaP `-11.0479` edge `-0.0571` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.3848` n `176` status `ready` deltaP `-15.7567` edge `-0.1462` maxDD `-15.8728`
- `market_context_high->equity_24h` score `-4.6709` n `145` status `ready` deltaP `-3.7889` edge `0.0226` maxDD `-36.6937`
- `market_context_high->crypto_major_24h` score `-4.7772` n `145` status `ready` deltaP `-6.5296` edge `-0.1313` maxDD `-26.3434`
- `market_context_high->commodity_24h` score `-5.4584` n `145` status `ready` deltaP `1.5801` edge `-0.0439` maxDD `-39.9805`
- `market_context_high->crypto_alt_4h` score `-7.2051` n `176` status `ready` deltaP `-15.7982` edge `-0.1603` maxDD `-20.1177`
- `market_context_high->crypto_alt_24h` score `-8.0155` n `145` status `ready` deltaP `-12.8226` edge `-0.2166` maxDD `-22.27`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
