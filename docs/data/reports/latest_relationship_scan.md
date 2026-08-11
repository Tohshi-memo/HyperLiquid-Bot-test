# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T06:37:35.918981+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `40.769` n `129` status `ready` deltaP `-18.2814` edge `3.7647` maxDD `-9.6329`
- `market_context_high->commodity_24h` score `1.9708` n `129` status `ready` deltaP `13.755` edge `0.1948` maxDD `-5.7814`
- `market_context_high->commodity_1h` score `0.7033` n `180` status `ready` deltaP `9.7173` edge `0.0281` maxDD `-0.7418`
- `market_context_high->commodity_4h` score `0.6454` n `169` status `ready` deltaP `10.3267` edge `0.0564` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.5158` n `129` status `ready` deltaP `17.2487` edge `0.0319` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.1809` n `180` status `ready` deltaP `2.9042` edge `-0.0002` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.2681` n `169` status `ready` deltaP `3.3288` edge `0.0039` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.9869` n `180` status `ready` deltaP `-7.2488` edge `-0.0146` maxDD `-2.0884`
- `market_context_high->index_1h` score `-1.2931` n `180` status `ready` deltaP `-7.0758` edge `-0.0029` maxDD `-0.948`
- `market_context_high->index_4h` score `-1.3294` n `169` status `ready` deltaP `-2.1831` edge `-0.0068` maxDD `-1.4875`
- `market_context_high->equity_1h` score `-1.4412` n `180` status `ready` deltaP `-6.8662` edge `-0.0113` maxDD `-6.8818`
- `market_context_high->crypto_alt_1h` score `-1.6921` n `180` status `ready` deltaP `-9.1084` edge `-0.0377` maxDD `-6.4812`
- `market_context_high->metal_4h` score `-2.3876` n `169` status `ready` deltaP `-11.4164` edge `-0.0536` maxDD `-6.1111`
- `market_context_high->metal_24h` score `-2.6278` n `129` status `ready` deltaP `-0.232` edge `-0.085` maxDD `-2.9283`
- `market_context_high->crypto_major_1h` score `-3.401` n `180` status `ready` deltaP `-7.3952` edge `-0.0437` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-3.973` n `169` status `ready` deltaP `-12.5467` edge `-0.1148` maxDD `-15.8728`
- `market_context_high->index_24h` score `-4.5002` n `129` status `ready` deltaP `-14.8172` edge `-0.0667` maxDD `-6.7627`
- `market_context_high->crypto_alt_4h` score `-6.902` n `169` status `ready` deltaP `-14.1696` edge `-0.1459` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-7.2373` n `129` status `ready` deltaP `-16.3541` edge `-0.2417` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-8.8741` n `129` status `ready` deltaP `-11.0981` edge `-0.1857` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
