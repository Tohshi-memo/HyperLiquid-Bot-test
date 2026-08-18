# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T06:07:30.419544+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11645`

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

- `market_context_high->crypto_major_24h` score `2.556` n `73` status `ready` deltaP `6.1181` edge `0.293` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.7924` n `73` status `ready` deltaP `12.6469` edge `0.2006` maxDD `-4.666`
- `market_context_high->metal_4h` score `0.6805` n `95` status `ready` deltaP `13.7532` edge `0.0226` maxDD `-1.273`
- `market_context_high->equity_1h` score `0.6467` n `100` status `ready` deltaP `6.6228` edge `0.0428` maxDD `-0.6449`
- `market_context_high->index_1h` score `0.4001` n `100` status `ready` deltaP `10.012` edge `0.0057` maxDD `-0.1281`
- `market_context_high->unknown_1h` score `0.3763` n `100` status `ready` deltaP `9.4551` edge `-0.009` maxDD `-0.4807`
- `market_context_high->crypto_major_4h` score `0.3608` n `95` status `ready` deltaP `8.9185` edge `0.0889` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-0.0659` n `95` status `ready` deltaP `8.5045` edge `0.0874` maxDD `-6.2038`
- `market_context_high->unknown_24h` score `-0.1403` n `73` status `ready` deltaP `12.1911` edge `-0.0706` maxDD `-0.4562`
- `market_context_high->metal_1h` score `-0.1557` n `100` status `ready` deltaP `2.0` edge `0.0054` maxDD `-0.4291`
- `market_context_high->commodity_4h` score `-0.1687` n `95` status `ready` deltaP `7.2561` edge `0.0226` maxDD `-2.4692`
- `market_context_high->metal_24h` score `-0.2827` n `73` status `ready` deltaP `3.6419` edge `0.0582` maxDD `-3.4975`
- `market_context_high->fx_4h` score `-0.3039` n `95` status `ready` deltaP `1.717` edge `0.0003` maxDD `-0.3904`
- `market_context_high->fx_1h` score `-0.3642` n `100` status `ready` deltaP `-1.8024` edge `0.0015` maxDD `-0.2273`
- `market_context_high->crypto_alt_1h` score `-0.3879` n `100` status `ready` deltaP `1.8503` edge `0.0181` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.5444` n `95` status `ready` deltaP `0.9483` edge `0.0095` maxDD `-0.2281`
- `market_context_high->equity_4h` score `-0.5962` n `95` status `ready` deltaP `-1.5196` edge `0.0509` maxDD `-2.5696`
- `market_context_high->crypto_major_1h` score `-0.6105` n `100` status `ready` deltaP `-0.0479` edge `0.0087` maxDD `-2.9317`
- `market_context_high->commodity_1h` score `-0.8156` n `100` status `ready` deltaP `-6.1497` edge `-0.0023` maxDD `-1.5684`
- `market_context_high->index_24h` score `-2.1125` n `73` status `ready` deltaP `-3.8437` edge `-0.1095` maxDD `-4.8566`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
