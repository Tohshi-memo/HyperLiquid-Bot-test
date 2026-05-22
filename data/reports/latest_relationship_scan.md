# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T00:07:19.922726+00:00`
- Price records: `672`
- Market context records: `1475`
- Flow alert records: `6153`
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

- `market_context_high->crypto_alt_24h` score `13.1272` n `171` status `ready` deltaP `28.9748` edge `1.1024` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0018` n `171` status `ready` deltaP `27.7412` edge `0.9284` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0157` n `171` status `ready` deltaP `15.2686` edge `0.9829` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.4654` n `171` status `ready` deltaP `13.56` edge `0.5144` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2708` n `171` status `ready` deltaP `20.2851` edge `0.3293` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.5558` n `218` status `ready` deltaP `7.1017` edge `0.1653` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.3239` n `171` status `ready` deltaP `12.765` edge `0.0468` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `-0.1656` n `218` status `ready` deltaP `11.3336` edge `0.2426` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.173` n `218` status `ready` deltaP `1.6645` edge `0.0345` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1914` n `218` status `ready` deltaP `2.6933` edge `0.0126` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.438` n `218` status `ready` deltaP `1.1244` edge `0.0649` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.5035` n `218` status `ready` deltaP `2.0711` edge `0.0466` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5127` n `218` status `ready` deltaP `0.0288` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-1.0295` n `218` status `ready` deltaP `5.369` edge `0.1493` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.0624` n `218` status `ready` deltaP `-4.4319` edge `-0.0096` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1144` n `218` status `ready` deltaP `-0.4395` edge `0.0022` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2603` n `218` status `ready` deltaP `4.524` edge `-0.0016` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.5947` n `218` status `ready` deltaP `-0.8405` edge `0.0084` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8058` n `218` status `ready` deltaP `7.801` edge `0.0667` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0372` n `218` status `ready` deltaP `-11.4693` edge `-0.0695` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
