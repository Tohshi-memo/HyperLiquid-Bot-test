# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T16:07:49.509720+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14761`

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

- `news_risk_high->unknown_24h` score `51.8946` n `50` status `ready` deltaP `11.6319` edge `4.247` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.8086` n `50` status `ready` deltaP `37.8403` edge `1.5259` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `13.0059` n `50` status `ready` deltaP `27.3841` edge `0.9112` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.702` n `50` status `ready` deltaP `46.0903` edge `0.0888` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.6003` n `50` status `ready` deltaP `25.8403` edge `0.3039` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0235` n `50` status `ready` deltaP `46.878` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.0486` n `50` status `ready` deltaP `17.4251` edge `0.1735` maxDD `-0.8495`
- `market_context_high->unknown_4h` score `2.7204` n `145` status `ready` deltaP `20.9703` edge `0.1276` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.6455` n `50` status `ready` deltaP `29.8403` edge `0.0366` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.4702` n `128` status `ready` deltaP `5.3819` edge `0.2432` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5815` n `50` status `ready` deltaP `21.1018` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2062` n `50` status `ready` deltaP `17.2635` edge `0.0133` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.9252` n `148` status `ready` deltaP `9.7224` edge `0.0573` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.6487` n `50` status `ready` deltaP `17.9207` edge `0.0109` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5697` n `50` status `ready` deltaP `15.1976` edge `0.003` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1545` n `50` status `ready` deltaP `7.9581` edge `0.0007` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1077` n `50` status `ready` deltaP `5.5509` edge `-0.0006` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0389` n `50` status `ready` deltaP `7.6159` edge `-0.0009` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0903` n `50` status `ready` deltaP `5.1037` edge `-0.0019` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.4758` n `148` status `ready` deltaP `1.8045` edge `0.0002` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
