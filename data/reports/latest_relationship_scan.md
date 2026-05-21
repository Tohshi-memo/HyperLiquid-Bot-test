# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T23:45:09.448260+00:00`
- Price records: `672`
- Market context records: `1473`
- Flow alert records: `6148`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.21` n `171` status `ready` deltaP `28.9748` edge `1.1093` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0558` n `171` status `ready` deltaP `27.7412` edge `0.9329` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.9989` n `171` status `ready` deltaP `15.2686` edge `0.9815` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.5026` n `171` status `ready` deltaP `13.56` edge `0.5175` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2768` n `171` status `ready` deltaP `20.2851` edge `0.3298` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.5525` n `219` status `ready` deltaP `7.196` edge `0.1644` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2862` n `171` status `ready` deltaP `12.3538` edge `0.0464` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1531` n `219` status `ready` deltaP `1.8237` edge `0.0351` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.1597` n `219` status `ready` deltaP `11.4823` edge `0.2421` maxDD `-19.5565`
- `market_context_high->index_1h` score `-0.1711` n `219` status `ready` deltaP `2.8567` edge `0.0132` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.4218` n `219` status `ready` deltaP `1.2669` edge `0.0653` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.4994` n `219` status `ready` deltaP `2.1225` edge `0.0466` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5012` n `219` status `ready` deltaP `0.2509` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-1.0347` n `219` status `ready` deltaP `5.3945` edge `0.1487` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.0489` n `219` status `ready` deltaP `-4.1869` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1436` n `219` status `ready` deltaP `-0.6699` edge `0.0013` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2512` n `219` status `ready` deltaP `4.5628` edge `-0.0011` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.5882` n `219` status `ready` deltaP `-0.7745` edge `0.0085` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8017` n `219` status `ready` deltaP `7.837` edge `0.0668` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0517` n `219` status `ready` deltaP `-11.6432` edge `-0.0702` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
