# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T04:22:33.026725+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5134`

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

- `market_context_high->unknown_1h` score `106.5228` n `104` status `ready` deltaP `-0.1554` edge `8.9194` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `72.1768` n `95` status `ready` deltaP `2.4743` edge `6.0294` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.9485` n `61` status `ready` deltaP `29.8042` edge `0.7273` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2913` n `65` status `ready` deltaP `32.3992` edge `0.5786` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `9.1303` n `61` status `ready` deltaP `25.5038` edge `0.6528` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `6.045` n `65` status `ready` deltaP `20.2439` edge `0.5032` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `4.184` n `95` status `ready` deltaP `17.9862` edge `0.2991` maxDD `-3.294`
- `news_risk_high->equity_24h` score `4.0897` n `65` status `ready` deltaP `14.8531` edge `0.2518` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3805` n `65` status `ready` deltaP `23.6111` edge `0.1243` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8865` n `65` status `ready` deltaP `31.7613` edge `0.055` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.6874` n `65` status `ready` deltaP `20.4245` edge `0.1488` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.6103` n `65` status `ready` deltaP `10.7646` edge `0.1813` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.1249` n `65` status `ready` deltaP `26.216` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9753` n `65` status `ready` deltaP `18.1637` edge `0.0851` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5463` n `95` status `ready` deltaP `26.2388` edge `0.0296` maxDD `-0.3868`
- `market_context_high->crypto_major_1h` score `1.473` n `104` status `ready` deltaP `11.9185` edge `0.0988` maxDD `-2.4406`
- `news_risk_high->crypto_alt_1h` score `1.3508` n `65` status `ready` deltaP `4.4196` edge `0.135` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.2013` n `61` status `ready` deltaP `4.6135` edge `0.0896` maxDD `-0.6196`
- `market_context_high->fx_24h` score `1.1235` n `61` status `ready` deltaP `15.847` edge `0.0801` maxDD `-1.703`
- `market_context_high->crypto_alt_4h` score `0.9248` n `95` status `ready` deltaP `3.4018` edge `0.2333` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
