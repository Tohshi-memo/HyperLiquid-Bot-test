# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T07:52:31.519783+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4221`

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

- `market_context_high->unknown_24h` score `1368.2517` n `98` status `ready` deltaP `2.9514` edge `114.0013` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.0164` n `98` status `ready` deltaP `43.4134` edge `1.9628` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.6639` n `98` status `ready` deltaP `29.3013` edge `1.7688` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3045` n `98` status `ready` deltaP `1.8789` edge `0.0086` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.6781` n `98` status `ready` deltaP `15.3557` edge `0.1636` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.6864` n `98` status `ready` deltaP `10.2477` edge `0.0052` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.9337` n `98` status `ready` deltaP `-1.4093` edge `0.1707` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9764` n `98` status `ready` deltaP `-3.822` edge `-0.001` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2703` n `98` status `ready` deltaP `-2.5571` edge `0.0045` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3795` n `98` status `ready` deltaP `-8.8965` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5877` n `98` status `ready` deltaP `-4.5172` edge `0.1848` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.349` n `98` status `ready` deltaP `-2.2852` edge `0.0062` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7116` n `98` status `ready` deltaP `-10.369` edge `-0.0225` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8672` n `98` status `ready` deltaP `-15.2236` edge `-0.0327` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2756` n `98` status `ready` deltaP `-0.1894` edge `-0.0531` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.657` n `98` status `ready` deltaP `-25.9115` edge `-0.0111` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7936` n `98` status `ready` deltaP `-18.8138` edge `-0.0098` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4484` n `98` status `ready` deltaP `-24.5146` edge `-0.1112` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.3785` n `98` status `ready` deltaP `-9.4778` edge `-0.0928` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9559` n `98` status `ready` deltaP `-16.563` edge `-0.2838` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
