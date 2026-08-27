# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T19:07:35.584782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14777`

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

- `news_risk_high->unknown_24h` score `52.1502` n `50` status `ready` deltaP `11.6319` edge `4.2683` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.6774` n `50` status `ready` deltaP `37.8403` edge `1.5983` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.969` n `50` status `ready` deltaP `26.622` edge `0.9132` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.8088` n `50` status `ready` deltaP `46.0903` edge `0.0977` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5187` n `50` status `ready` deltaP `25.8403` edge `0.2971` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9979` n `50` status `ready` deltaP `46.5732` edge `0.0317` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.0463` n `50` status `ready` deltaP `16.976` edge `0.1763` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.7258` n `128` status `ready` deltaP `5.3819` edge `0.2645` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.6287` n `50` status `ready` deltaP `29.8403` edge `0.0352` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.5259` n `148` status `ready` deltaP `19.7842` edge `0.1193` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5695` n `50` status `ready` deltaP `20.9521` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1427` n `50` status `ready` deltaP `16.6647` edge `0.012` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.9228` n `148` status `ready` deltaP `9.2733` edge `0.0601` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8277` n `50` status `ready` deltaP `18.9878` edge `0.0187` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5471` n `50` status `ready` deltaP `14.8982` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.139` n `50` status `ready` deltaP `7.6587` edge `0.0007` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0617` n `50` status `ready` deltaP `4.8024` edge `-0.0015` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1063` n `50` status `ready` deltaP `7.4634` edge `-0.0055` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1439` n `50` status `ready` deltaP `4.4939` edge `-0.0023` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4503` n `148` status `ready` deltaP `6.3283` edge `-0.0082` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
