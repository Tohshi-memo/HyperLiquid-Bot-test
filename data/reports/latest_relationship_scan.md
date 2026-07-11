# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T01:52:23.847252+00:00`
- Price records: `672`
- Market context records: `6344`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.2531` n `32` status `ready` deltaP `43.0556` edge `0.9988` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.125` n `32` status `ready` deltaP `50.8681` edge `0.1713` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3821` n `32` status `ready` deltaP `16.8403` edge `0.5275` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1777` n `32` status `ready` deltaP `43.5213` edge `0.0626` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.5893` n `32` status `ready` deltaP `31.5972` edge `0.109` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3763` n `32` status `ready` deltaP `28.5928` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5216` n `32` status `ready` deltaP `14.8765` edge `0.1426` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9439` n `32` status `ready` deltaP `11.7702` edge `0.0887` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5821` n `196` status `ready` deltaP `12.9387` edge `0.0419` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.1609` n `207` status `ready` deltaP `-7.182` edge `0.1621` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0689` n `196` status `ready` deltaP `6.4118` edge `0.0223` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.4153` n `207` status `ready` deltaP `3.378` edge `0.002` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.567` n `207` status `ready` deltaP `-0.6567` edge `0.0` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.631` n `134` status `ready` deltaP `14.7362` edge `0.0777` maxDD `-11.8809`
- `market_context_high->commodity_24h` score `-0.6495` n `134` status `ready` deltaP `-4.2703` edge `0.1316` maxDD `-6.2457`
- `market_context_high->fx_1h` score `-0.7045` n `207` status `ready` deltaP `-0.5135` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7125` n `32` status `ready` deltaP `0.3472` edge `-0.0065` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.7192` n `196` status `ready` deltaP `4.9621` edge `0.0446` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.7465` n `32` status `ready` deltaP `-3.1437` edge `-0.025` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.8355` n `32` status `ready` deltaP `5.3331` edge `-0.0707` maxDD `-0.7581`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
