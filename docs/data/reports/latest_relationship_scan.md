# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T23:52:18.530689+00:00`
- Price records: `672`
- Market context records: `1474`
- Flow alert records: `6150`
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

- `market_context_high->crypto_alt_24h` score `13.2172` n `171` status `ready` deltaP `28.9748` edge `1.1099` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0594` n `171` status `ready` deltaP `27.7412` edge `0.9332` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0013` n `171` status `ready` deltaP `15.2686` edge `0.9817` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.5062` n `171` status `ready` deltaP `13.56` edge `0.5178` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2804` n `171` status `ready` deltaP `20.2851` edge `0.3301` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.5513` n `219` status `ready` deltaP `7.196` edge `0.1643` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2874` n `171` status `ready` deltaP `12.3538` edge `0.0465` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1663` n `219` status `ready` deltaP `1.674` edge `0.035` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1723` n `219` status `ready` deltaP `2.8567` edge `0.0131` maxDD `-1.7205`
- `market_context_high->crypto_alt_4h` score `-0.1743` n `219` status `ready` deltaP `11.3299` edge `0.2419` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.423` n `219` status `ready` deltaP `1.2669` edge `0.0652` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.5012` n `219` status `ready` deltaP `0.2509` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5018` n `219` status `ready` deltaP `2.1225` edge `0.0464` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-1.0359` n `219` status `ready` deltaP `5.3945` edge `0.1486` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.0489` n `219` status `ready` deltaP `-4.1869` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1448` n `219` status `ready` deltaP `-0.6699` edge `0.0012` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2524` n `219` status `ready` deltaP `4.5628` edge `-0.0012` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.5894` n `219` status `ready` deltaP `-0.7745` edge `0.0084` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8029` n `219` status `ready` deltaP `7.837` edge `0.0667` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0525` n `219` status `ready` deltaP `-11.6432` edge `-0.0703` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
