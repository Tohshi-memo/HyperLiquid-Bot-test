# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T15:37:25.206070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11324`

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

- `news_risk_high->unknown_24h` score `44.8782` n `61` status `ready` deltaP `9.9186` edge `3.7711` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `20.1203` n `61` status `ready` deltaP `31.4663` edge `1.7965` maxDD `-22.0332`
- `market_context_high->unknown_24h` score `8.944` n `104` status `ready` deltaP `20.2591` edge `0.6835` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.4228` n `80` status `ready` deltaP `11.5854` edge `0.517` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.542` n `104` status `ready` deltaP `32.8525` edge `0.2614` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6092` n `80` status `ready` deltaP `5.2246` edge `0.2183` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.518` n `80` status `ready` deltaP `36.3415` edge `0.0225` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.3959` n `119` status `ready` deltaP `18.098` edge `0.1222` maxDD `-0.7887`
- `news_risk_high->equity_24h` score `1.2356` n `61` status `ready` deltaP `20.0678` edge `0.3004` maxDD `-18.3954`
- `market_context_high->unknown_1h` score `1.0356` n `131` status `ready` deltaP `9.4803` edge `0.0712` maxDD `-1.5148`
- `risk_on_high->crypto_alt_1h` score `0.8561` n `31` status `ready` deltaP `15.197` edge `0.056` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.8561` n `31` status `ready` deltaP `15.197` edge `0.056` maxDD `-2.1381`
- `news_risk_high->fx_1h` score `0.7603` n `80` status `ready` deltaP `14.491` edge `0.0056` maxDD `-0.108`
- `news_risk_high->metal_24h` score `0.719` n `61` status `ready` deltaP `32.4112` edge `0.0101` maxDD `-7.0529`
- `risk_on_high->metal_1h` score `0.595` n `31` status `ready` deltaP `9.3442` edge `0.0087` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `0.595` n `31` status `ready` deltaP `9.3442` edge `0.0087` maxDD `-0.0463`
- `news_risk_high->commodity_1h` score `0.4081` n `80` status `ready` deltaP `11.9012` edge `0.005` maxDD `-0.5618`
- `news_risk_high->index_24h` score `0.3281` n `61` status `ready` deltaP `16.0547` edge `0.011` maxDD `-2.0772`
- `news_risk_high->crypto_major_24h` score `0.2903` n `61` status `ready` deltaP `16.4219` edge `0.2927` maxDD `-24.8633`
- `market_context_high->crypto_major_4h` score `0.137` n `119` status `ready` deltaP `19.0638` edge `0.2294` maxDD `-20.9394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
