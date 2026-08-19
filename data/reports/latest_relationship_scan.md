# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T17:13:35.695092+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8829`

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

- `market_context_high->equity_4h` score `2.3861` n `96` status `ready` deltaP `12.3729` edge `0.2052` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8596` n `96` status `ready` deltaP `15.3007` edge `0.0831` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9474` n `96` status `ready` deltaP `16.0616` edge `0.0106` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.7309` n `96` status `ready` deltaP `15.1931` edge `0.0172` maxDD `-1.273`
- `market_context_high->crypto_major_24h` score `0.7218` n `96` status `ready` deltaP `4.3402` edge `0.152` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.4181` n `96` status `ready` deltaP `7.6389` edge `0.186` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.3288` n `96` status `ready` deltaP `18.2291` edge `-0.0435` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.1762` n `96` status `ready` deltaP `8.562` edge `0.0231` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.1066` n `96` status `ready` deltaP `7.4102` edge `-0.0178` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.0874` n `96` status `ready` deltaP `8.4095` edge `0.0054` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0873` n `96` status `ready` deltaP `3.8735` edge `0.0056` maxDD `-0.4291`
- `market_context_high->crypto_major_4h` score `-0.225` n `96` status `ready` deltaP `8.2571` edge `0.0283` maxDD `-3.1677`
- `market_context_high->fx_1h` score `-0.3362` n `96` status `ready` deltaP `-1.4721` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.6598` n `96` status `ready` deltaP `0.5801` edge `-0.0083` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6676` n `96` status `ready` deltaP `2.0833` edge `-0.015` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.676` n `96` status `ready` deltaP `-0.6351` edge `0.0026` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-0.8033` n `96` status `ready` deltaP `6.0976` edge `0.0194` maxDD `-5.4926`
- `market_context_high->commodity_1h` score `-0.9266` n `96` status `ready` deltaP `-8.1899` edge `-0.0076` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.6331` n `96` status `ready` deltaP `-6.5972` edge `0.0372` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.6505` n `96` status `ready` deltaP `-19.9652` edge `-0.0128` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
